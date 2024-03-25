import copy
from antlr4 import *
from TxScriptLexer import *
from TxScriptParser import *
from TxScriptVisitor import *

class Z3Visitor(TxScriptVisitor):
    def __init__(self, N, A, Trace_Based, can_transations_arrive_any_time):
        self.__proc = set()
        self.__proc_args = {}
        self.__add_last_cmd = False
        self.__prefix = ''
        self.__args_map = {}
        self.__nesting_w = 0
        self.__nesting_aw = 0
        self.__max_nesting = 0
        self.__globals = []
        self.__globals_index = {}
        self.__globals_const = {}
        self.__globals_modifier = -1
        self.__visit_properties = False
        self.__visit_properties_body = False
        self.__const = False
        self.__tx_sender = 'xa'
        self.__prop_nested_i = set()
        self.__n_transactions = 1
        self.__max_n_transactions = 1
        self.__prop_transactions = {}
        self.__pi = 1
        self.__prop_name = ''
        self.__prop_names = set()
        self.__maps = set()
        # N = upper bound on the length of trace
        self.__N = N
        # A = upper bound on the number of actors (A+1)
        self.__A = A
        self.__Trace_Based = Trace_Based
        self.__can_transations_arrive_any_time = can_transations_arrive_any_time

    # Visit a parse tree produced by TxScriptParser#contractExpr.
    def visitContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        decls = self.visit(ctx.decl)
        decls = [decl for decl in decls if decl is not None]
        self.__visit_properties = True
        props = self.visit(ctx.properties)
        self.__visit_properties = False
        self.__nesting_w = 1
        self.__nesting_aw = 1
        self.__t_curr_w = 't_w[0]'
        self.__t_new_w = 't_w[1]'
        self.__t_curr_a = 'awNow'
        self.__t_new_a = 't_aw[0]'
        # self.__proc.add(ctx.name.text)
        # self.__prefix = ctx.name.text
        for k in self.__globals_index:
            self.__globals_index[k] = 0

        # if not any('constructor' in decl for decl in decls):
        #     decls.append('\ndef constructor(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num{global_args}):\n\treturn next_state_tx(awNow, awNext, wNow, wNext{global_args_next_state_tx})'.format(
        #         global_args = (', ' + ', '.join([g.text+'Now, '+g.text+'Next, t_'+g.text for (g, _) in self.__globals])) if self.__globals else '', 
        #         # global_args_assign = (', '.join([g.text+'Next == '+g.text+'Next' for (g, _) in self.__globals]) + ', ') if self.__globals else ''), 
        #         global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
        #     ))
        if self.__can_transations_arrive_any_time and not any('coinbase' in decl for decl in decls):
            decls.append('\ndef coinbase(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num{global_args}):\n\treturn And(t_w[0] == wNow + xn1, next_state_tx(awNow, awNext, t_w[0], wNext{global_args_next_state_tx}))'.format(
                global_args = (', ' + ', '.join([g.text+'Now, '+g.text+'Next, t_'+g.text for (g, _) in self.__globals])) if self.__globals else '', 
                # global_args_assign = (', '.join([g.text+'Next == '+g.text+'Next' for (g, _) in self.__globals]) + ', ') if self.__globals else ''), 
                global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
            ))
            self.__proc.add('coinbase')
            self.__proc_args['coinbase'] = None
        proc = ''
        for p in self.__proc:
            if p == 'constructor': continue
            proc += 'Proc.declare(\'{name}\')\n'.format(name=p)
        args = ['{a} = [Int("{a}_%s" % (i)) for i in range(N+1)]'.format(a=self.__args_map[a]) for a in self.__args_map]
        for i in range(0, self.__max_n_transactions):
            args += ['{a}_q{i} = Int("{a}{i}_q")'.format(i=i, a=self.__args_map[a]) for a in self.__args_map]
        step_trans_args = [self.__args_map[a] for a in self.__args_map if 'constructor' not in self.__args_map[a]]
        t_aw_qs = ''
        for i in range(0, self.__max_n_transactions):
            t_aw_qs += f't_aw_q{i} = [[Int("t_awq{i}_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]\n'
        # block_num_qs = ''
        xn_qs = ''
        f_qs = ''
        w_qs = ''
        aw_qs = ''
        t_w_qs = ''
        for i in range(0, self.__max_n_transactions):
            # block_num_qs += f'block_num_q{i} = Int("block_num_q{i}")\n'
            xn_qs += f'xn_q{i} = Int("xn_q{i}")\n'
            f_qs += f'f_q{i} = Const("f_q{i}", Proc)\n'
            w_qs += f'w_q{i} = Int("wq{i}")\n'
            aw_qs += f'aw_q{i} = [Int("awq{i}_%s" % j) for j in range(A+1)]\n'
            t_w_qs += f't_w_q{i} = [Int("t_wq{i}_%s" % (m)) for m in range(M)]\n'
        functions_call = ''
        n_tabs = 0
        keys = list(self.__proc_args.keys())
        if 'constructor' in keys: keys.remove('constructor')
        if keys:
            aux = 1
            if 'coinbase' in keys:
                functions_call += '\tIf(f1 == Proc.coinbase, And(xa1 == -1, \n'
                n_tabs += 1
                functions_call += '\t'*n_tabs + 'coinbase' + '(xa1, xn1, ' + (','.join(self.__proc_args['coinbase'])+', ' if self.__proc_args['coinbase'] else '') + 'aw1, aw2, w1, w2, t_aw, t_w, block_num1' + ((', ' + ', '.join([g.text+'Now, '+g.text+'Next, t_'+g.text for (g, _) in self.__globals])) if self.__globals else '') + ')),\n'
                keys.remove('coinbase')
                aux += 1
            functions_call += 'And(xa1 >= 0, xa1 <= A, '
            for p in keys[:-1]:
                functions_call += '\t'*n_tabs + 'If(f1 == Proc.' + p + ',\n'
                n_tabs += 1
                functions_call += '\t'*n_tabs + p + '(xa1, xn1, ' + (','.join(self.__proc_args[p])+', ' if self.__proc_args[p] else '') + 'aw1, aw2, w1, w2, t_aw, t_w, block_num1' + ((', ' + ', '.join([g.text+'Now, '+g.text+'Next, t_'+g.text for (g, _) in self.__globals])) if self.__globals else '') + '),\n'
            n_tabs += 1
            functions_call += '\t'*n_tabs + keys[-1] + '(xa1, xn1, ' + (','.join(self.__proc_args[keys[-1]])+', ' if self.__proc_args[keys[-1]] else '') + 'aw1, aw2, w1, w2, t_aw, t_w, block_num1' + ((', ' + ', '.join([g.text+'Now, '+g.text+'Next, t_'+g.text for (g, _) in self.__globals])) if self.__globals else '') + ')'
            functions_call += ')'*(len(keys) + aux)
        contract_globals = ''
        for (g_var,g_type) in self.__globals:
            if g_type == 'Address':
                g_type = 'Int'
            if type(g_type) is tuple:
                contract_globals += '''
{g} = [[{ty}("{g}_%s_%s" % (i, j)) for j in range(A+1)] for i in range(N+1)]
t_{g} = [[[{ty}("t_{g}_%s_%s_%s" % (i, m, j)) for j in range(A+1)] for m in range(M)] for i in range(N+1)]'''.format(g=g_var.text, ty=g_type[1])
                for i in range(0, self.__max_n_transactions):
                    contract_globals += '''
{g}_q{i} = [{ty}("{g}q{i}_%s" % j) for j in range(A+1)]
t_{g}_q{i} = [[{ty}("t_{g}q{i}_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]'''.format(i=i, g=g_var.text, ty=g_type[1])
            else:
                contract_globals += '''
{g} = [{ty}("{g}_%s" % (i)) for i in range(N+1)]
t_{g} = [[{ty}("t_{g}_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]'''.format(g=g_var.text, ty=g_type)
                for i in range(0, self.__max_n_transactions):
                    contract_globals += '''
{g}_q{i} = {ty}("{g}q{i}")
t_{g}_q{i} = [{ty}("t_{g}q{i}_%s" % (m)) for m in range(M)]'''.format(i=i, g=g_var.text, ty=g_type)

        check_ranges = ''
        for (g_var,g_type) in self.__globals:
            if g_type == 'Address':
                check_ranges += f'{g_var.text}Next >= 0, {g_var.text}Next <= A, '

        prop_queries = 'queries = {}\n'
        for n in self.__prop_names:
            q = ','.join([f'p_{n}_{i}(i)' for i in range(1, self.__prop_transactions[n]+1)])
            prop_queries += f'queries[\'{n}\'] = [[{q}] for i in range(1, N+1)]\n'

        res = '''
from z3 import *
import time


def stringOfXA(m, i):
    return "A" + str(m.eval(xa[i]))


def stringOfTx(m, i):
    contract = "C4"
    sender = stringOfXA(m, i)
    method = str(m.eval(f[i]))
    args = str(m.eval(xn[i]))
    return "-- " + sender + ": " + contract + "." + method + "(" + args + ") -->"


def stringOfWal(m, i):
    s = ""
    for j in range(A+1):
        s += "A" + str(j) + "[" + str(m.eval(aw[i][j])) + ":T] | "
    return s


def stringOfContr(m, i):
    contract = "C4"
    return contract + "[" + str(m.eval(w[i])) + ":T] "


def stringOfSuccess(m, i):
    s = "| success:"
    return s + str(m.eval(success[i]))


def printState(m):
    for i in range(N):
        print(stringOfWal(m, i), end='')
        print(stringOfContr(m, i), end='')
        print(stringOfSuccess(m, i), end='')
        print()
        print(stringOfTx(m, i), end='')
        print()
    print(stringOfWal(m, N), end='')
    print(stringOfContr(m, N), end='')
    print()


timeStart = time.time()

# N = upper bound on the length of trace
N = {N}

# A = upper bound on the number of actors (A+1)
A = {A}

# Maximum functions depth
M = 50

# Contract's balance
w = [Int("w_%s" % (i)) for i in range(N+1)]
{w_qs}

# Block number
block_num = [Int("block_num_%s" % (i)) for i in range(N+1)]

Proc = Datatype('Proc')
{proc}
Proc = Proc.create()

# Contract's state variables
{contract_globals}

# Called procedure
f = [Const("f_%s" % (i), Proc) for i in range(N+1)]
{f_qs}

# users' wallets
aw = [[Int("aw_%s_%s" % (i, j)) for j in range(A+1)] for i in range(N+1)]
{aw_qs}

# msg.sender
xa = [Int("xa_%s" % (i)) for i in range(N+1)]
xa_q = Int("xa_q")

# msg.value
xn = [Int("xn_%s" % (i)) for i in range(N+1)]
{xn_qs}

# functions args
{args}

# List of ids hard coded
hard_coded_list = [0]

# Temporary contract balance. Used inside functions to model internal states
t_w = [[Int("t_w_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
{t_w_qs} 

# Temporary users wallets
t_aw = [[[Int("t_aw_%s_%s_%s" % (i, m, j)) for j in range(A+1)]
         for m in range(M)] for i in range(N+1)]

{t_aw_qs}

s = Solver()

def next_state_tx(aw1, aw2, w1, w2{global_args_next_state_tx}):
    return And(w2 == w1,
               And([aw2[j] == aw1[j] for j in range(A+1)])
               {global_args_next_state_tx_eval}
               {global_args_next_state_tx_map_eval})

def send(sender_id, amount, w_b, w_a, aw_b, aw_a): # '_b' and '_a' mean 'before' and 'after'
    return And(w_a == w_b - amount,
                  And([If(j == sender_id,
                          aw_a[j] == aw_b[j] + amount,
                          aw_a[j] == aw_b[j]) for j in range(A+1)]))

{decls}


def user_is_legit(xa1):
    return And(xa1 >= 0, xa1 <= A)


def user_has_not_already_played(xa, xa1, f, i):
    return Not(Or([And(xa[k] == xa1, f[k] == Proc.pay) for k in range(i)]))


def user_is_not_hard_coded(xa1):
    return Not(Or([xa1 == hc_i for hc_i in hard_coded_list]))


def user_is_fresh(xa, xa1, f, i):
    return And(user_is_not_hard_coded(xa1), user_has_not_already_played(xa, xa1, f, i))

# transition rules

def step_trans(f1, xa1, xn1, {step_trans_args} aw1, aw2, w1, w2, t_aw, t_w, block_num1, block_num2, i{global_args}):
    return And(And(xn1 >= 0, w2 >= 0),
               And([aw1[j] >= 0 for j in range(A+1)]),
               block_num2 >= block_num1,
               {check_ranges}
               {functions_call}

# initial state
{initial_balance}
               
new_state = And(And(xa[0] >= 0, xa[0] <= A, xn[0] >= 0),
               And([aw[0][j] >= 0 for j in range(A+1)]),
                  constructor(xa[0], xn[0], {constr_args_0} aw[0], aw[1], w[0], w[1], t_aw[0], t_w[0], block_num[0]{global_args_0}))
s.add(new_state)
for i in range(1, N):
    new_state = step_trans(f[i], xa[i], xn[i], {step_trans_args_i} aw[i],
                           aw[i+1], w[i], w[i+1], t_aw[i], t_w[i], block_num[i], block_num[i+1], i{global_args_i})
    s.add(new_state)


# print(s)

# def p(i):
#     t_awq_list = [t_awq_m_j for t_awq_m in t_aw_q for t_awq_m_j in t_awq_m]
#     #print([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ])
#     return And(w[i] > 0,
#                Exists([xa_q], And(user_is_legit(xa_q), user_is_fresh(xa, xa_q, f,  i),
#                       ForAll([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list{func_args_q}{global_args_q} ], Or(Not(step_trans(f_q, xa_q, xn_q{func_args_q}, aw[i], aw_q, w[i], w_q, t_aw_q, t_w_q, i{global_args_phi})), w_q > 0)))))
#                       #ForAll([xn_q, f_q, w_q, *aw_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw[i], t_w[i], i)), w_q > 0)))))


{props}

{queries}

for prop in {props_name}:
    for i, q in enumerate(queries[prop]):
        for j in range(0, len(q)):
            qj = q[j]
            s2 = Solver()
            s2.add(s.assertions())
            s2.add(qj)
            text = s2.to_smt2()
            text = '(set-logic ALL)\\n' + text
            filename = 'out/smt2/%s/{tracestate}based/%s/output_%s.smt2'%(prop, str(i).zfill(len(str(len(queries[prop])))), str(j).zfill(len(str(len(q)))))
            if not os.path.exists('out/smt2/'):
                os.makedirs('out/smt2/')
            if not os.path.exists('out/smt2/%s/'%(prop)):
                os.makedirs('out/smt2/%s/'%(prop))
            if not os.path.exists('out/smt2/%s/{tracestate}based/'%(prop)):
                os.makedirs('out/smt2/%s/{tracestate}based/'%(prop))
            if not os.path.exists('out/smt2/%s/{tracestate}based/%s/'%(prop, str(i).zfill(len(str(len(queries[prop])))))):
                os.makedirs('out/smt2/%s/{tracestate}based/%s/'%(prop, str(i).zfill(len(str(len(queries[prop]))))))
            with open(filename, 'w') as my_file:
                my_file.write(text)

# timeStart = time.time()
# for prop in {props_name}:
#     print('Property [' + prop + ']')
#     for i, q in enumerate(queries[prop]):
#         liquid = False
#         for j in range(0, len(q)):
#             qj = q[j] 
#             resj = s.check(qj)
#             if resj == unsat:
#                 liquid = True
#                 break
#         if not liquid:
#             break
#     if not liquid: print("not liquid [in {n_trans} steps]")
#     else: print("liquid [in {n_trans} steps]")
#     timeTot = time.time() - timeStart
#     print("Solving time: " + str(timeTot) + "s")
               
'''.format(
        N=self.__N if self.__Trace_Based else 1, 
        A=self.__A, 
        initial_balance='s.add(w[0] >= 0)' if self.__can_transations_arrive_any_time or not self.__Trace_Based else 's.add(w[0] == 0)',
        tracestate='trace' if self.__Trace_Based else 'state',
        proc=proc, 
        decls='\n'.join(decls), 
        args='\n'.join(args), 
        t_aw_qs = t_aw_qs,
        # block_num_qs = block_num_qs,
        xn_qs = xn_qs,
        f_qs = f_qs,
        w_qs = w_qs,
        aw_qs = aw_qs,
        t_w_qs = t_w_qs,
        check_ranges = check_ranges,
        step_trans_args=', '.join(step_trans_args)+',' if step_trans_args else '', 
        step_trans_args_i=', '.join([s+'[i]' for s in step_trans_args])+',' if step_trans_args else '',
        global_args_next_state_tx = (', ' + ', '.join([g.text+'Now, '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else '',
        global_args_next_state_tx_eval = (', ' + ', '.join([g.text+'Now=='+g.text+'Next' for (g, _) in self.__globals if g.text not in self.__maps])) if [g for (g, _) in self.__globals if g.text not in self.__maps] else '',
        global_args_next_state_tx_map_eval = (', ' + ', '.join([f'And([{g.text}Now[j] == {g.text}Next[j] for j in range(A+1)])' for (g, _) in self.__globals if g.text in self.__maps])) if [g for (g, _) in self.__globals if g.text in self.__maps] else '',
        global_args = (', ' + ', '.join([g.text+'Now, '+g.text+'Next, t_'+g.text for (g, _) in self.__globals])) if self.__globals else '', 
        global_args_i = (', ' + ', '.join([g.text+'[i], '+g.text+'[i+1]'+', t_'+g.text+'[i]' for (g, _) in self.__globals])) if self.__globals else '', 
        global_args_0 = (', ' + ', '.join([g.text+'[0], '+g.text+'[1]'+', t_'+g.text+'[0]' for (g, _) in self.__globals])) if self.__globals else '', 
        global_args_phi = (', ' + ', '.join([g.text+'[i], '+g.text+'_q, t_'+g.text+'_q' for (g, _) in self.__globals])) if self.__globals else '', 
        global_args_q = (', ' + ', '.join([g.text+'_q, *t_'+g.text+'_q' for (g, _) in self.__globals])) if self.__globals else '',
        func_args_q = (', ' + ', '.join([s+'_q' for s in step_trans_args]) if step_trans_args else ''),
        functions_call=functions_call,
        constr_args = (','.join(self.__proc_args['constructor'])+', ' if 'constructor' in self.__proc_args and self.__proc_args['constructor'] else ''),
        constr_args_0 = (','.join([s+'[0]' for s in self.__proc_args['constructor']])+', ' if 'constructor' in self.__proc_args and self.__proc_args['constructor'] else ''),
        contract_globals = contract_globals, 
        # max_nesting = self.__max_nesting,
        props = '\n'.join(props),
        # pis = ','.join([f'p{i}(i)' for i in range(1, self.__n_transactions+1)]),
        queries = prop_queries,
        props_name = '{' + ','.join(['\''+n+'\'' for n in self.__prop_names]) + '}',
        n_trans = self.__max_n_transactions 
    )
        return res 


    # Visit a parse tree produced by TxScriptParser#constFieldDecl.
    def visitConstFieldDecl(self, ctx:TxScriptParser.ConstFieldDeclContext):
        self.__const = True
        self.visit(ctx.child)
        self.__const = False


    # Visit a parse tree produced by TxScriptParser#declsExpr.
    def visitDeclsExpr(self, ctx:TxScriptParser.DeclsExprContext):
        decls = []
        for decl in ctx.declExpr():
            decls.append(self.visit(decl))
            self.__max_nesting = max(self.__nesting_w, self.__max_nesting)
            self.__max_nesting = max(self.__nesting_aw, self.__max_nesting)
        return decls
    

    # Visit a parse tree produced by TxScriptParser#propertiesExpr.
    def visitPropertiesExpr(self, ctx:TxScriptParser.PropertiesExprContext):
        props = []
        for prop in ctx.propertyExpr():
            props.append(self.visit(prop))
        return props


    # Visit a parse tree produced by TxScriptParser#propertyExpr.
    def visitPropertyExpr(self, ctx:TxScriptParser.PropertyExprContext):
        self.__prop_name = ctx.name.text
        self.__prop_names.add(self.__prop_name)
        return self.visit(ctx.phi)


    # Visit a parse tree produced by TxScriptParser#intDecl.
    def visitIntDecl(self, ctx:TxScriptParser.IntDeclContext):
        self.__globals.append((ctx.var, 'Int'))
        self.__globals_index[ctx.var.text] = 0
        self.__globals_const[ctx.var.text] = self.__const


    # Visit a parse tree produced by TxScriptParser#boolDecl.
    def visitBoolDecl(self, ctx:TxScriptParser.BoolDeclContext):
        self.__globals.append((ctx.var, 'Bool'))
        self.__globals_index[ctx.var.text] = 0
        self.__globals_const[ctx.var.text] = self.__const


    # Visit a parse tree produced by TxScriptParser#strDecl.
    def visitStrDecl(self, ctx:TxScriptParser.StrDeclContext):
        self.__globals.append((ctx.var, 'String'))
        self.__globals_index[ctx.var.text] = 0
        self.__globals_const[ctx.var.text] = self.__const


    # Visit a parse tree produced by TxScriptParser#addrDecl.
    def visitAddrDecl(self, ctx:TxScriptParser.AddrDeclContext):
        self.__globals.append((ctx.var, 'Address'))
        self.__globals_index[ctx.var.text] = 0
        self.__globals_const[ctx.var.text] = self.__const


    # Visit a parse tree produced by TxScriptParser#mapAddrDecl.
    def visitMapAddrDeclInt(self, ctx:TxScriptParser.MapAddrDeclIntContext):
        self.__globals.append((ctx.var, ('MapAddr', 'Int')))
        self.__globals_index[ctx.var.text] = 0
        self.__maps.add(ctx.var.text)
        self.__globals_const[ctx.var.text] = self.__const


    # Visit a parse tree produced by TxScriptParser#constrDecl.
    def visitConstrDecl(self, ctx:TxScriptParser.ConstrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#nonPayableConstructorDecl.
    def visitNonPayableConstructorDecl(self, ctx:TxScriptParser.NonPayableConstructorDeclContext):
        self.__nesting_w = 0
        self.__nesting_aw = 0
        self.__t_curr_w = 'wNow'
        self.__t_new_w = 't_w[0]'
        self.__t_curr_a = 'awNow'
        self.__t_new_a = 't_aw[0]'
        self.__proc.add('constructor')
        self.__prefix = 'constructor'
        for k in self.__globals_index:
            self.__globals_index[k] = 0
        return self.visitFun(ctx, 'And(xn1 == 0')
    

    # Visit a parse tree produced by TxScriptParser#payableConstructorDecl.
    def visitPayableConstructorDecl(self, ctx:TxScriptParser.PayableConstructorDeclContext):
        self.__nesting_w = 1
        self.__nesting_aw = 0
        self.__t_curr_w = 't_w[0]'
        self.__t_new_w = 't_w[1]'
        self.__t_curr_a = 'awNow'
        self.__t_new_a = 't_aw[0]'
        self.__proc.add('constructor')
        self.__prefix = 'constructor'
        for k in self.__globals_index:
            self.__globals_index[k] = 0
        return self.visitFun(ctx, 'And(t_w[0] == wNow + xn1')


    # Visit a parse tree produced by TxScriptParser#payableFunDecl.
    def visitPayableFunDecl(self, ctx:TxScriptParser.PayableFunDeclContext):
        self.__nesting_w = 1
        self.__nesting_aw = 0
        self.__t_curr_w = 't_w[0]'
        self.__t_new_w = 't_w[1]'
        self.__t_curr_a = 'awNow'
        self.__t_new_a = 't_aw[0]'
        self.__proc.add(ctx.name.text + '_func')
        self.__prefix = ctx.name.text + '_func'
        for k in self.__globals_index:
            self.__globals_index[k] = 0
        return self.visitFun(ctx, 'And(t_w[0] == wNow + xn1')
        # return self.visitFun(ctx, 'And(t_w[0] == wNow + xn1, t_aw[0][xa1] == awNow - xn1, for (...)')


    # Visit a parse tree produced by TxScriptParser#nonPayableFunDecl.
    def visitNonPayableFunDecl(self, ctx:TxScriptParser.NonPayableFunDeclContext):
        self.__nesting_w = 0
        self.__nesting_aw = 0
        self.__t_curr_w = 'wNow'
        self.__t_new_w = 't_w[0]'
        self.__t_curr_a = 'awNow'
        self.__t_new_a = 't_aw[0]'
        self.__proc.add(ctx.name.text + '_func')
        self.__prefix = ctx.name.text + '_func'
        for k in self.__globals_index:
            self.__globals_index[k] = 0
        return self.visitFun(ctx, 'If(Not(xn1==0), next_state_tx(awNow, awNext, wNow, wNext{global_args_next_state_tx})'.format(
            global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
        ))


    # Visit a parse tree produced by TxScriptParser#funDecl.
    def visitFun(self, ctx, reqs):
        args = self.visit(ctx.args)
        self.__add_last_cmd = True
        body = self.visit(ctx.cmds)
        contract_variables = 'True'
        if self.__prefix == 'constructor':
            for (g, ty) in self.__globals:
                if self.__globals_index[g.text] == 0 and (self.__Trace_Based or self.__globals_const[g.text]):
                    self.__globals_index[g.text] = 1
                    if ty == 'Int' or ty == 'Address':
                        default = f', t_{g.text}[0]==0'
                    elif ty == 'Bool':
                        default = f', t_{g.text}[0]==False'
                    elif ty == 'String':
                        default = f', t_{g.text}[0]==\'\''
                    else:
                        default = ',' + ', '.join([f't_{g.text}[0][{i}]==0' for i in range(0, self.__A+1)])
                    contract_variables += default
                elif self.__Trace_Based or self.__globals_const[g.text]:
                    if ty == 'Address':
                        default = f', t_{g.text}[0]>=0, t_{g.text}[0]<=A'
                        contract_variables += default
        else:
            for g in self.__globals_const:
                if self.__globals_const[g]:
                    contract_variables += f', {g}Now=={g}Next'  
        self.__proc_args[self.__prefix] = args
        res ='''
def {name}(xa1, xn1, {args}awNow, awNext, wNow, wNext, t_aw, t_w, block_num{global_args}):
    return {reqs}, \n\tAnd({body}'''.format(
        name=self.__prefix, 
        args=(','.join(args)+', ' if args else ''), 
        body=body, 
        reqs=reqs,
        global_args = (', ' + ', '.join([g.text+'Now, '+g.text+'Next, t_'+g.text for (g, _) in self.__globals])) if self.__globals else '',
        # globals_update = (', \n\t\t' + ', '.join([('t_'+g.text+'['+str(self.__globals_index[g.text]-1)+']' if self.__globals_index[g.text]>0 else g.text+'Now') + ' == '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
    )
        skip = '{default}, next_state_tx({t_curr_a}, awNext, {t_curr_w}, wNext{global_args_next_state_tx})'.format(
            t_curr_a=self.__t_curr_a, 
            t_curr_w=self.__t_curr_w, 
            default=contract_variables,
            global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
        )
        if res.format(subs=skip) == res:
            return res + f', {skip}))'
        else:
            return res.format(subs=skip) + '))'


    # Visit a parse tree produced by TxScriptParser#argsExpr.
    def visitArgsExpr(self, ctx:TxScriptParser.ArgsExprContext):
        args = set()
        for arg in ctx.argExpr():
            args.add(self.__prefix + '_' + arg.var.text)
            self.__args_map[arg.var.text] = self.__prefix + '_' + arg.var.text
        return args


    # Visit a parse tree produced by TxScriptParser#arg.
    def visitArg(self, ctx:TxScriptParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sendCmd.
    def visitSendCmd(self, ctx:TxScriptParser.SendCmdContext):
        sender = ctx.sender.text
        self.__nesting_w += 1
        self.__nesting_aw += 1

        left = self.visit(ctx.amount)
        for el in self.__prop_nested_i:
            if el in left:
                send_chk = f'And([Or(j != {el}, '+f'{left} >= 0) for j in range(A+1)])'.replace(el, 'j')
                break
        else:
            send_chk = left + '>= 0'
        for el in self.__prop_nested_i:
            if el in left:
                send = f'And([Or(j != {el}, '+'send({sender}, {amount}, {t_curr_w}, {t_new_w}, {t_curr_a}, {t_new_a})) for j in range(A+1)])'
                break
        else:
            el = None
            send = 'send({sender}, {amount}, {t_curr_w}, {t_new_w}, {t_curr_a}, {t_new_a})'

        if sender == 'sender' or sender == 'msg.sender' or sender == 'xa1':
            res = send.format(
                amount=left, 
                t_curr_w=self.__t_curr_w, 
                t_new_w=self.__t_new_w, 
                t_curr_a=self.__t_curr_a, 
                t_new_a=self.__t_new_a,
                sender= 'xa1'
            )
        else:
            if sender in self.__globals_index:
                sender = sender + 'Now' if self.__globals_index[sender]+self.__globals_modifier < 0 else 't_'+sender + '['+str(self.__globals_index[sender]+self.__globals_modifier)+']'
            elif sender in self.__args_map:
                sender = self.__args_map[sender]
            res = send.format(
                sender=sender, 
                amount=left, 
                t_curr_w=self.__t_curr_w, 
                t_new_w=self.__t_new_w, 
                t_curr_a=self.__t_curr_a, 
                t_new_a=self.__t_new_a
            )
        if el:
            res = res[:res.index('send')+4] + res[res.index('send')+4:].replace(el, 'j')
        res = 'If(\n\tNot(' + send_chk + '), \n\t\tnext_state_tx(awNow, awNext, wNow, wNext'+((', ' + ', '.join([g.text+'Now, '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else '')+'), And(' + res + ', {subs}))'
        self.__t_curr_a = 't_aw[' + str(self.__nesting_aw-1) + ']'
        self.__t_new_a = 't_aw[' + str(self.__nesting_aw) + ']'
        self.__t_curr_w = 't_w[' + str(self.__nesting_w-1) + ']'
        self.__t_new_w = 't_w[' + str(self.__nesting_w) + ']'
        return res

    # Visit a parse tree produced by TxScriptParser#requireCmd.
    def visitRequireCmd(self, ctx:TxScriptParser.RequireCmdContext):
        if self.__prefix == 'constructor':
            return self.visit(ctx.child)
        else:
            return 'If(\n\tNot(' + self.visit(ctx.child) + '), \n\t\tnext_state_tx(awNow, awNext, wNow, wNext'+((', ' + ', '.join([g.text+'Now, '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else '')+'), And(\n\t\t{subs}))'


    # Visit a parse tree produced by TxScriptParser#skipCmd.
    def visitSkipCmd(self, ctx:TxScriptParser.SkipCmdContext):
        return 'next_state_tx({t_curr_a}, awNext, {t_curr_w}, wNext{global_args_next_state_tx})'.format(
            t_curr_a=self.__t_curr_a, 
            t_curr_w=self.__t_curr_w, 
            global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
        )


    # Visit a parse tree produced by TxScriptParser#groupCmd.
    def visitGroupCmd(self, ctx:TxScriptParser.GroupCmdContext):
        return self.visit(ctx.child)


    # Visit a parse tree produced by TxScriptParser#assignCmd.
    def visitAssignCmd(self, ctx:TxScriptParser.AssignCmdContext):
        left = ctx.var.text
        # self.__globals_modifier -= 1
        right = self.visit(ctx.child)
        # self.__globals_modifier += 1
        i = self.__globals_index[left]
        self.__globals_index[left] = i+1
        if self.__prefix == 'constructor' and not self.__Trace_Based and not self.__globals_const[left]:
            return 'True'
        aux = 0
        while '[' in right[aux:] and ']' in right[aux:] and right[right.index('[', aux)+1:right.index(']', aux)].isnumeric():
            aux = right.index(']', aux) + 1
            if aux >= len(right): break
        if aux != -1 and aux < len(right) and '[' in right[aux:] and ']' in right[aux:]:
            index = right[right.index('[', aux)+1:right.index(']', aux)]
            right = right.replace(index, 'j')
            return f'And([Or(j!={str(index)}, t_{left}[{str(i)}] == {right}) for j in range(A+1)])' 
        else:
            return 't_'+left+'['+str(i)+']' + ' == ' + right
    

    # Visit a parse tree produced by TxScriptParser#assignMapCmd.
    def visitAssignMapCmd(self, ctx:TxScriptParser.AssignMapCmdContext):
        left = ctx.var.text
        index = self.visit(ctx.index)
        self.__globals_modifier -= 1
        right = self.visit(ctx.child).replace(str(index), 'j')
        self.__globals_modifier += 1
        i = self.__globals_index[left]
        self.__globals_index[left] = i+1
        prev_i = f'{left}Now' if i == 0 else f't_{left}[{str(i-1)}]'
        return f'And(And([Or(j!={str(index)}, t_{left}[{str(i)}][j] == {right}) for j in range(A+1)]), And([Or(j=={str(index)}, t_{left}[{str(i)}][j] == {prev_i}[j]) for j in range(A+1)]))' 
        # return 'And('+ 'And(' + f'[t_{left}[{str(i)}][j] == {right} for j in range(A+1) if j == {str(index)}]' + ')' + ', ' + 'And(' + f'[t_{left}[{str(i)}][j] == {prev_i}[j] for j in range(A+1) if j != {str(index)}]' + ')' ')'
        # return 'And('+ 't_'+left+'['+str(i)+']'+'['+str(index)+']' + ' == ' + right + ', ' + 'And(' + f'[t_{left}[{str(i)}][j] == {prev_i}[j] for j in range(A+1) if j != {str(index)}]' + ')' ')'


    # Visit a parse tree produced by TxScriptParser#ifCmd.
    def visitIfCmd(self, ctx:TxScriptParser.IfCmdContext):
        cond = self.visit(ctx.condition)
        backup = self.__globals_index.copy()
        backup_add = self.__add_last_cmd
        self.__add_last_cmd = False
        ifcmd = self.visit(ctx.ifcmd)
        self.__globals_index = backup
        self.__add_last_cmd = backup_add
        self.__globals_index = backup
        return 'If({cond},{ifcmd},{elsecmd})'.format(
            cond = 'And'+'('+cond+')',
            ifcmd = 'And'+'('+ifcmd+')',
            elsecmd = 'True'
        )
    

    # Visit a parse tree produced by TxScriptParser#ifelseCmd.
    def visitIfelseCmd(self, ctx:TxScriptParser.IfelseCmdContext):
        cond = self.visit(ctx.condition)
        # backup = self.__globals_index.copy()
        backup_add = self.__add_last_cmd
        self.__add_last_cmd = False
        backup__t_curr_a = self.__t_curr_a
        backup__t_new_a = self.__t_new_a
        backup__t_curr_w = self.__t_curr_w
        backup__t_new_w = self.__t_new_w
        backup_nesting_w = self.__nesting_w
        backup_nesting_aw = self.__nesting_aw
        backup_global_index = copy.deepcopy(self.__globals_index)
        ifcmd = self.visit(ctx.ifcmd)
        # skip = 'next_state_tx({t_curr_a}, awNext, {t_curr_w}, wNext{global_args_next_state_tx})'.format(
        #     t_curr_a=self.__t_curr_a, 
        #     t_curr_w=self.__t_curr_w, 
        #     global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]-1+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
        # )
        if__t_curr_a = self.__t_curr_a
        if__t_new_a = self.__t_new_a
        if__t_curr_w = self.__t_curr_w
        if__t_new_w = self.__t_new_w
        if_nesting = self.__nesting_w
        if_globals_index = copy.deepcopy(self.__globals_index)
        self.__t_curr_a = backup__t_curr_a
        self.__t_new_a = backup__t_new_a
        self.__t_curr_w = backup__t_curr_w
        self.__t_new_w = backup__t_new_w
        self.__nesting_w = backup_nesting_w
        self.__nesting_aw = backup_nesting_aw
        self.__globals_index = backup_global_index
        elsecmd = self.visit(ctx.elsecmd)
        # skip = 'next_state_tx({t_curr_a}, awNext, {t_curr_w}, wNext{global_args_next_state_tx})'.format(
        #     t_curr_a=self.__t_curr_a, 
        #     t_curr_w=self.__t_curr_w, 
        #     global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]-1+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
        # )
        levelling_if_cmds = 'True'
        levelling_else_cmds = 'True'
        if if_nesting > self.__nesting_w:
            levelling_else_cmds += f', {if__t_curr_w}=={self.__t_curr_w}, {if__t_curr_a}=={self.__t_curr_a}'
            self.__t_curr_a = if__t_curr_a
            self.__t_new_a = if__t_new_a
            self.__t_curr_w = if__t_curr_w
            self.__t_new_w = if__t_new_w
            self.__nesting = if_nesting
        elif if_nesting < self.__nesting_w:
            levelling_if_cmds += f', {if__t_curr_w}=={self.__t_curr_w}, {if__t_curr_a}=={self.__t_curr_a}'
        for g in self.__globals_index:
            if if_globals_index[g] > self.__globals_index[g]:
                tg_now = f't_{g}[{self.__globals_index[g]}]' if self.__globals_index[g] > 0 else f'{g}Now'
                levelling_else_cmds += f', t_{g}[{if_globals_index[g]-1}]=={tg_now}'
                self.__globals_index[g] = if_globals_index[g]
            elif if_globals_index[g] < self.__globals_index[g]:
                tg_now = f't_{g}[{if_globals_index[g]}]' if if_globals_index[g] > 0 else f'{g}Now'
                levelling_if_cmds += f', {tg_now}==t_{g}[{self.__globals_index[g]-1}]'
        self.__add_last_cmd = backup_add
        # self.__globals_index = backup
        ifcmd_aux = ifcmd.format(subs=levelling_if_cmds)
        if ifcmd_aux == ifcmd:
            ifcmd += f', {levelling_if_cmds}'
        else:
            ifcmd = ifcmd_aux
        elsecmd_aux = elsecmd.format(subs=levelling_else_cmds)
        if elsecmd_aux == elsecmd:
            elsecmd += f', {levelling_else_cmds}'
        else:
            elsecmd = elsecmd_aux
        return 'If({cond},{ifcmd},{elsecmd})'.format(
            cond = 'And'+'('+cond+')',
            ifcmd = 'And'+'('+ifcmd+')',
            elsecmd = 'And'+'('+elsecmd+')'
        )


    # Visit a parse tree produced by TxScriptParser#seqCmd.
    def visitSeqCmd(self, ctx:TxScriptParser.SeqCmdContext):
        seq1 = self.visit(ctx.seq1)
        seq2 = self.visit(ctx.seq2)
        # if self.__add_last_cmd and not isinstance(ctx.seq2, TxScriptParser.SkipCmdContext):
        #     seq2 = 'And({seq2}, next_state_tx({t_curr_a}, awNext, {t_curr_w}, wNext{global_args_next_state_tx}))'.format(
        #         seq2=seq2, 
        #         t_curr_a=self.__t_curr_a, 
        #         t_curr_w=self.__t_curr_w,
        #         global_args_next_state_tx = (', ' + ', '.join([(g.text + 'Now' if self.__globals_index[g.text]+self.__globals_modifier < 0 else 't_'+g.text + '['+str(self.__globals_index[g.text]-1+self.__globals_modifier)+']')+', '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else ''
        #     )
        #     self.__add_last_cmd = False
        aux = seq1.format(subs='And('+seq2+',{subs})')
        if aux == seq1:
            return 'And(\n\t{seq1},\n\t{seq2})'.format(seq1=seq1, seq2=seq2)
        else:
            return aux


    # Visit a parse tree produced by TxScriptParser#groupExpr.
    def visitGroupExpr(self, ctx:TxScriptParser.GroupExprContext):
        return self.visit(ctx.child)


    # Visit a parse tree produced by TxScriptParser#greaterEqExpr.
    def visitGreaterEqExpr(self, ctx:TxScriptParser.GreaterEqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        # if not self.__visit_properties_body:
        for el in self.__prop_nested_i:
            if el in left or el in right:
                return f'And([Or(j != {el}, '+f'{left} >= {right}) for j in range(A+1)])'.replace(el, 'j')
        return left + '>=' + right
        # else:
        #     for el in self.__prop_nested_i:
        #         if el in left or el in right:
        #             return f'And([Or(j != {el}, '+f'{left} >= {right}) for j in range(A+1)])'.replace(el, 'j')        
        #     return f'Not({left} >= {right})'



    # Visit a parse tree produced by TxScriptParser#lessExpr.
    def visitLessExpr(self, ctx:TxScriptParser.LessExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        # if not self.__visit_properties_body:
        for el in self.__prop_nested_i:
            if el in left or el in right:
                return f'And([Or(j != {el}, '+f'{left} < {right}) for j in range(A+1)])'.replace(el, 'j')
        return left + '<' + right
        # else:
        #     for el in self.__prop_nested_i:
        #         if el in left or el in right:
        #             return f'And([Or(j != {el}, '+f'Not({left} < {right})) for j in range(A+1)])'.replace(el, 'j')        
        #     return f'Not({left} < {right})'


    # Visit a parse tree produced by TxScriptParser#neqExpr.
    def visitNeqExpr(self, ctx:TxScriptParser.NeqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '!=' + right


    # # Visit a parse tree produced by TxScriptParser#variableExpr.
    # def visitVariableExpr(self, ctx:TxScriptParser.VariableExprContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#greaterExpr.
    def visitGreaterExpr(self, ctx:TxScriptParser.GreaterExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        # if not self.__visit_properties_body:
        for el in self.__prop_nested_i:
            if el in left or el in right:
                return f'And([Or(j != {el}, '+f'{left} > {right}) for j in range(A+1)])'.replace(el, 'j')
        return left + '>' + right
        # else:
        #     for el in self.__prop_nested_i:
        #         if el in left or el in right:
        #             return f'And([Or(j != {el}, '+f'Not({left} > {right})) for j in range(A+1)])'.replace(el, 'j')        
        #     return f'Not({left} > {right})'


    # Visit a parse tree produced by TxScriptParser#eqExpr.
    def visitEqExpr(self, ctx:TxScriptParser.EqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if left == 'tx_sender':
            self.__tx_sender = right
            return 'True'
        if right == 'tx_sender':
            self.__tx_sender = left
            return 'True'
        
        # if not self.__visit_properties_body:
        #     return left + '==' + right
        # else:
        for el in self.__prop_nested_i:
            if el in left or el in right:
                return f'And([Or(j != {el}, '+f'{left} == {right}) for j in range(A+1)])'.replace(el, 'j')        
        return f'{left} == {right}'


    # Visit a parse tree produced by TxScriptParser#notExpr.
    def visitNotExpr(self, ctx:TxScriptParser.NotExprContext):
        return 'Not('+self.visit(ctx.child)+')'


    # Visit a parse tree produced by TxScriptParser#sumSubEqExpr.
    def visitSumSubEqExpr(self, ctx:TxScriptParser.SumSubEqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if left in self.__globals_index:
            if self.__globals_index[left]+self.__globals_modifier < 0:
                left = left + 'Now'
            else:
                left = 't_'+left + '['+str(self.__globals_index[left]+self.__globals_modifier)+']'
        if right in self.__globals_index:
            if self.__globals_index[right]+self.__globals_modifier < 0:
                right = right + 'Now'
            else:
                right = 't_'+right + '['+str(self.__globals_index[right]+self.__globals_modifier)+']'
        return left + ctx.op.text + right


    # Visit a parse tree produced by TxScriptParser#lessEqExpr.
    def visitLessEqExpr(self, ctx:TxScriptParser.LessEqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        # if not self.__visit_properties_body:
        for el in self.__prop_nested_i:
            if el in left or el in right:
                return f'And([Or(j != {el}, '+f'{left} <= {right}) for j in range(A+1)])'.replace(el, 'j')
        return left + '<=' + right
        # else:
        #     for el in self.__prop_nested_i:
        #         if el in left or el in right:
        #             return f'And([Or(j != {el}, '+f'Not({left} <= {right})) for j in range(A+1)])'.replace(el, 'j')        
        #     return f'Not({left} <= {right})'


    # Visit a parse tree produced by TxScriptParser#constExpr.
    def visitConstExpr(self, ctx:TxScriptParser.ConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#multDivEqExpr.
    def visitMultDivEqExpr(self, ctx:TxScriptParser.MultDivEqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if left in self.__globals_index:
            if self.__globals_index[left]+self.__globals_modifier < 0:
                left = left + 'Now'
            else:
                left = 't_'+left + '['+str(self.__globals_index[left]+self.__globals_modifier)+']'
        if right in self.__globals_index:
            if self.__globals_index[right]+self.__globals_modifier < 0:
                right = right + 'Now'
            else:
                right = 't_'+right + '['+str(self.__globals_index[right]+self.__globals_modifier)+']'
        res = left + ctx.op.text + right
        #  left out for now, it would require to keep track of the division and propagate their handling in the assign command
        # if ctx.op.text == '/':
        #     res = 'If(\n\tNot(' + right + ' != 0), \n\t\tnext_state_tx(awNow, awNext, wNow, wNext'+((', ' + ', '.join([g.text+'Now, '+g.text+'Next' for (g, _) in self.__globals])) if self.__globals else '')+'), And(' + res + ', {subs}))'        
        return res


    # Visit a parse tree produced by TxScriptParser#andExpr.
    def visitAndExpr(self, ctx:TxScriptParser.AndExprContext):
        return 'And(' + self.visit(ctx.left) + ',' + self.visit(ctx.right) + ')'
    

    # Visit a parse tree produced by TxScriptParser#orExpr.
    def visitOrExpr(self, ctx:TxScriptParser.OrExprContext):
        return 'Or(' + self.visit(ctx.left) + ',' + self.visit(ctx.right) + ')'


    # # Visit a parse tree produced by TxScriptParser#orWithdrawExpr.
    # def visitOrWithdrawExpr(self, ctx:TxScriptParser.OrWithdrawExprContext):
    #     return f'Or({self.visit(ctx.left)},{self.visit(ctx.right)})'


    # # Visit a parse tree produced by TxScriptParser#andWithdrawExpr.
    # def visitAndWithdrawExpr(self, ctx:TxScriptParser.AndWithdrawExprContext):
    #     return f'And({self.visit(ctx.left)},{self.visit(ctx.right)})'


    # # Visit a parse tree produced by TxScriptParser#baseWithdrawExpr.
    # def visitBaseWithdrawExpr(self, ctx:TxScriptParser.BaseWithdrawExprContext):
    #     index = self.visit(ctx.ag)
    #     arr_name = 'w'
    #     res = f'Not(w_q <= {arr_name}[{index}]-({self.visit(ctx.body)}))'
    #     if '[i]' in index:
    #         res_with_j = res.replace(f"{arr_name}[{index}]", f"{arr_name}[j]")
    #         return f"And([Or(j != {index}, {res_with_j}) for j in range(A+1)])"
    #     else:
    #         return res


    # Visit a parse tree produced by TxScriptParser#qslf.
    def visitQslf(self, ctx:TxScriptParser.QslfContext):
        agent = ctx.ag.text + '_q'
        self.__n_transactions  = int(ctx.nTrans.text)
        self.__max_n_transactions  = max(int(ctx.nTrans.text), self.__max_n_transactions)
        self.__prop_transactions[self.__prop_name] = self.__n_transactions 
        self.__tx_sender = 'xa_q' if ctx.sender.text == 'xa' else ctx.sender.text.replace('st.', '')+'[i]'
        condition = self.visit(ctx.where)
        step_trans_args = [self.__args_map[a] for a in self.__args_map if 'constructor' not in self.__args_map[a]]
        global_args_q = (', ' + ', '.join([(g.text+'_q{i}, *t_'+g.text+'_q{i}' if ty!=('MapAddr', 'Int') else '*'+g.text+'_q{i}, *t_'+g.text+'_q{i}_list') for (g, ty) in self.__globals])) if self.__globals else ''
        func_args_q = (', ' + ', '.join([s+'_q{i}' for s in step_trans_args]) if step_trans_args else '')
        global_args_phi0 = (', ' + ', '.join([g.text+'[i], '+g.text+'_q{i}, t_'+g.text+'_q{i}' for (g, _) in self.__globals])) if self.__globals else ''
        global_args_phi = (', ' + ', '.join([g.text+'_q{j}, '+g.text+'_q{i}, t_'+g.text+'_q{i}' for (g, _) in self.__globals])) if self.__globals else ''
        pi = ''
        for i in range(1, self.__n_transactions+1):  
            self.__pi = i
            self.__visit_properties_body = True
            body = self.visit(ctx.body)
            self.__visit_properties_body = False
            pi += self.createPi(i, agent, condition, body, global_args_q, func_args_q, global_args_phi0, global_args_phi)
        return pi

    def createPi(self, nTrans, agent, condition, body, global_args_q, func_args_q, global_args_phi0, global_args_phi):
        t_awq_lists = ''
        step_trans = ''
        forall_args = ''
        for i in range(0, nTrans):
            t_awq_lists += f't_awq_list{i} = [t_awq_m_j for t_awq_m in t_aw_q{i} for t_awq_m_j in t_awq_m]; '
            for (g,ty) in self.__globals:
                if ty==('MapAddr', 'Int'):
                    t_awq_lists += f't_{g.text}_q{i}_list = [t_{g.text}_q_m_j for t_{g.text}_q_m in t_{g.text}_q{i} for t_{g.text}_q_m_j in t_{g.text}_q_m]; '
            if forall_args: forall_args += ', '
            forall_args += f'xn_q{i}, f_q{i}, w_q{i}, *aw_q{i}, *t_w_q{i}, *t_awq_list{i}'+func_args_q.format(i=i)+global_args_q.format(i=i)
            if i == 0:
                step_trans += f'Not(step_trans(f_q{i}, {self.__tx_sender}, xn_q{i}'+func_args_q.format(i=i)+f', aw[i], aw_q{i}, w[i], w_q{i}, t_aw_q{i}, t_w_q{i}, block_num[i], block_num[i], i+{i}'+global_args_phi0.format(i=i)+')),\n'
            else:
                step_trans += f'Not(step_trans(f_q{i}, {self.__tx_sender}, xn_q{i}'+func_args_q.format(i=i)+f', aw_q{i-1}, aw_q{i}, w_q{i-1}, w_q{i}, t_aw_q{i}, t_w_q{i}, block_num[i], block_num[i], i+{i}'+global_args_phi.format(i=i,j=i-1)+')),\n'
        return f'''
def p_{self.__prop_name}_{nTrans}(i):
    {t_awq_lists}
    return And(
        Exists([{agent}], And(user_is_legit({agent}), {condition},
            ForAll([{forall_args}],  
                Or(
{step_trans}
Not({body})
        )))))'''


    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return ctx.v.text
    

    # Visit a parse tree produced by TxScriptParser#mapExpr.
    def visitMapExpr(self, ctx:TxScriptParser.MapExprContext):
        index = self.visit(ctx.index)
        if not self.__visit_properties:
            if ctx.mapVar.text in self.__globals_index:
                self.__prop_nested_i.add(index)
                if self.__globals_index[ctx.mapVar.text]+self.__globals_modifier < 0:
                    return ctx.mapVar.text + 'Now' + '['+index+']'
                else:
                    return 't_'+ctx.mapVar.text + '['+str(self.__globals_index[ctx.mapVar.text]+self.__globals_modifier)+']' + '['+index+']'
            return ctx.mapVar.text + '[' + index + ']'
        else:
            if 'app_tx_st' in ctx.mapVar.text:
                i = f'_q{self.__n_transactions-1-(self.__n_transactions-self.__pi)}'
            else:
                i = '[i]'
            if 'st.balance' in ctx.mapVar.text:
                ag = index.replace('_q', '')
                if ag == 'xa':
                    self.__prop_nested_i.add(ag+'_q')#(ag+'[i]')
                    return f'aw{i}[{ag}_q]'#f'aw{i}[{ag}[i]]'
                else:
                    if '[i]' not in ag:
                        ag = ag+'[i]'
                    self.__prop_nested_i.add(ag)#(ag+'[i]')
                    return f'aw{i}[{ag}]'#f'aw{i}[{ag}[i]]'
            if ctx.mapVar.text.replace('st.','') in self.__args_map:
                return self.__args_map[ctx.v.text]  
            if ctx.mapVar.text.replace('st.','') in self.__globals_index:  
                ag = index.replace('_q', '')
                if ag == 'xa':
                    self.__prop_nested_i.add(ag+'_q')#(ag+'[i]')
                    return ctx.mapVar.text.replace('st.','') + f'{i}' + '[' + ag + '_q]'
                else:
                    if '[i]' not in ag:
                        ag = ag+'[i]'
                    self.__prop_nested_i.add(ag)#(ag+'[i]')
                    return ctx.mapVar.text.replace('st.','') + f'{i}' + '['+ag+']'
            return ctx.mapVar.text.replace('st.', '') + '_q'


    # Visit a parse tree produced by TxScriptParser#strConstant.
    def visitStrConstant(self, ctx:TxScriptParser.StrConstantContext):
        if not self.__visit_properties:
            if ctx.v.text == 'balance':
                return self.__t_curr_w
            if ctx.v.text == 'block.number':
                return 'block_num'
            if ctx.v.text == 'msg.value' or ctx.v.text == 'value':
                return 'xn1'
            if ctx.v.text == 'msg.sender' or ctx.v.text == 'sender':
                return 'xa1'
            if ctx.v.text in self.__args_map:
                return self.__args_map[ctx.v.text]
            if ctx.v.text in self.__globals_index:
                if self.__globals_index[ctx.v.text]+self.__globals_modifier < 0:
                    return ctx.v.text + 'Now'
                else:
                    return 't_'+ctx.v.text + '['+str(self.__globals_index[ctx.v.text]+self.__globals_modifier)+']'
            return ctx.v.text
        else:
            if 'app_tx_st' in ctx.v.text:
                ctx.v.text = ctx.v.text.replace('app_tx_st', 'st')
                i = f'_q{self.__n_transactions-1-(self.__n_transactions-self.__pi)}'
            else:
                i = '[i]'
            if 'st.balance' in ctx.v.text and '[' in ctx.v.text and ']' in ctx.v.text:
                ag = ctx.v.text[ctx.v.text.index('[')+1:ctx.v.text.index(']')]
                if ag == 'xa':
                    self.__prop_nested_i.add(ag+'_q')#(ag+'[i]')
                    return f'aw{i}[{ag}_q]'#f'aw{i}[{ag}[i]]'
                else:
                    self.__prop_nested_i.add(ag+'[i]')#(ag+'[i]')
                    return f'aw{i}[{ag}[i]]'#f'aw{i}[{ag}[i]]'
            if 'st.balance' in ctx.v.text:
                return f'w{i}'
            if 'st.block.number' in ctx.v.text:
                return f'block_num{i}'
            if 'tx.msg.value' in ctx.v.text:
                return 'xn'+f'_q{self.__n_transactions-1-(self.__n_transactions-self.__pi)}'
            if 'tx.msg.sender' in ctx.v.text:
                return 'tx_sender'
            if ctx.v.text.replace('st.','') in self.__args_map:
                return self.__args_map[ctx.v.text]  
            if ctx.v.text.replace('st.','') in self.__globals_index:              
                return ctx.v.text.replace('st.','') + f'{i}'
            return ctx.v.text.replace('st.', '') + '_q'


    # Visit a parse tree produced by TxScriptParser#trueConstant.
    def visitTrueConstant(self, ctx:TxScriptParser.TrueConstantContext):
        return 'True'


    # Visit a parse tree produced by TxScriptParser#falseConstant.
    def visitFalseConstant(self, ctx:TxScriptParser.FalseConstantContext):
        return 'False'
    
