from antlr4 import *
from TxScriptLexer import *
from TxScriptParser import *
from TxScriptVisitor import *

class Z3Visitor(TxScriptVisitor):
    def __init__(self, N, A):
        self.__proc = set()
        self.__add_last_cmd = False
        self.__args_map = {}
        # N = upper bound on the length of trace
        self.__N = N
        # A = upper bound on the number of actors (A+1)
        self.__A = A

    # Visit a parse tree produced by TxScriptParser#contractExpr.
    def visitContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        decl = self.visit(ctx.decl)
        proc = ''
        for p in self.__proc:
            proc += 'Proc.declare(\'{name}\')\n'.format(name=p.text)
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

# Contract's balance
w = [Int("w_%s" % (i)) for i in range(N+1)]
w_q = Int("wq")

Proc = Datatype('Proc')
{proc}
Proc = Proc.create()

# Called procedure
f = [Const("f_%s" % (i), Proc) for i in range(N+1)]
f_q = Const("f_q", Proc)

# users' wallets
aw = [[Int("aw_%s_%s" % (i, j)) for j in range(A+1)] for i in range(N+1)]
aw_q = [Int("awq_%s" % j) for j in range(A+1)]

# msg.sender
xa = [Int("xa_%s" % (i)) for i in range(N+1)]
xa_q = Int("xa_q")

# msg.value
xn = [Int("xn_%s" % (i)) for i in range(N+1)]
xn_q = Int("xn_q")

# List of ids hard coded
hard_coded_list = [0]

# This param should be computed automatically
# Maximum functions depth
M = 2

# Temporary contract balance. Used inside functions to model internal states
t_w = [[Int("t_w_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
t_w_q = [Int("t_wq_%s" % (m)) for m in range(M)] 

# Temporary users wallets
t_aw = [[[Int("t_aw_%s_%s_%s" % (i, m, j)) for j in range(A+1)]
         for m in range(M)] for i in range(N+1)]

t_aw_q = [[Int("t_awq_%s_%s" % (m, j)) for j in range(A+1)]
         for m in range(M)]

s = Solver()

# initial state
s.add(w[0] >= 0)
# s.add(w[0] == 1)

def valid_tx(xa1, xn1, w1, w2):
    return And(xa1 >= 0, xa1 <= A, xn1 > 0)

def next_state_tx(aw1, aw2, w1, w2):
    return And(w2 == w1,
               And([aw2[j] == aw1[j] for j in range(A+1)]))

def send(sender_id, amount, w_b, w_a, aw_b, aw_a): # '_b' and '_a' mean 'before' and 'after'
    return And(w_a == w_b - amount,
                  And([If(j == sender_id,
                          aw_a[j] == aw_b[j] + amount,
                          aw_a[j] == aw_b[j]) for j in range(A+1)]))

{decl}


def user_is_legit(xa1):
    return And(xa1 >= 0, xa1 <= A)


def user_has_not_already_played(xa, xa1, f, i):
    return Not(Or([And(xa[k] == xa1, f[k] == Proc.pay) for k in range(i)]))


def user_is_not_hard_coded(xa1):
    return Not(Or([xa1 == hc_i for hc_i in hard_coded_list]))


def user_is_fresh(xa, xa1, f, i):
    return And(user_is_not_hard_coded(xa1), user_has_not_already_played(xa, xa1, f, i))

# transition rules


def step_trans(f1, xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, i):
    return And(valid_tx(xa1, xn1, w1, w2),
               And([aw1[j] >= 0 for j in range(A+1)]),
               If(f1 == Proc.pay,
                  pay(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w),
                  #   The only other possible transition is f[i] == Proc.deposit
                  deposit(xn1, w1, w2, aw1, aw2)
                  #new_state_tx(aw1, aw2, w1, w2)
                  ))


for i in range(N):
    new_state = step_trans(f[i], xa[i], xn[i], aw[i],
                           aw[i+1], w[i], w[i+1], t_aw[i], t_w[i], i)

    s.add(new_state)


# print(s)

def p(i):
    t_awq_list = [t_awq_m_j for t_awq_m in t_aw_q for t_awq_m_j in t_awq_m]
    #print([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ])
    return And(w[i] > 0,
               Exists([xa_q], And(user_is_legit(xa_q), user_is_fresh(xa, xa_q, f,  i),
                      ForAll([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw_q, t_w_q, i)), w_q > 0)))))
                      #ForAll([xn_q, f_q, w_q, *aw_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw[i], t_w[i], i)), w_q > 0)))))

queries = [p(i) for i in range(N)]

# queries = [ p(0) ]

for i, q in enumerate(queries):
    timeStart = time.time()
    # print("q : ", q)
    print("p " + str(i) + " : ", end='')
    # sq = s
    # sq.add(q)
    # print("\\n\\nsq:", sq, "\\n\\n")
    res = s.check(q)
    if res == sat:
        print(" sat (=> not liquid)")
        m = s.model()
        # print(m)
        #printState(m)
        # exit()
    else:
        print(" unsat (=> liquid)")

    timeTot = time.time() - timeStart
    print("Solving time: " + str(timeTot) + "s")
                      
'''.format(N=self.__N, A=self.__A, proc=proc, decl=decl)
        return res


    # Visit a parse tree produced by TxScriptParser#declsExpr.
    def visitDeclsExpr(self, ctx:TxScriptParser.DeclsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#intDecl.
    def visitIntDecl(self, ctx:TxScriptParser.IntDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#strDecl.
    def visitStrDecl(self, ctx:TxScriptParser.StrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#constrDecl.
    def visitConstrDecl(self, ctx:TxScriptParser.ConstrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#funDecl.
    def visitFunDecl(self, ctx:TxScriptParser.FunDeclContext):
        self.__proc.add(ctx.name)
        self.__args_map = {}
        args = self.visit(ctx.args)
        self.__add_last_cmd = True
        body = self.visit(ctx.cmds)
        res ='''
def {name}(xa1, {args}, awNow, awNext, wNow, wNext, t_aw, t_w):
    {body}
'''.format(name=ctx.name.text, args=','.join(args), body=body)
        return res


    # Visit a parse tree produced by TxScriptParser#argsExpr.
    def visitArgsExpr(self, ctx:TxScriptParser.ArgsExprContext):
        args = set()
        i = 1
        for arg in ctx.argExpr():
            args.add('xn' + str(i))
            self.__args_map[arg.var.text] = 'xn' + str(i)
            i += 1
        return args


    # Visit a parse tree produced by TxScriptParser#arg.
    def visitArg(self, ctx:TxScriptParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sendCmd.
    def visitSendCmd(self, ctx:TxScriptParser.SendCmdContext):
        sender = ctx.sender.text
        if sender == 'sender':
            res = 'send(xa1, {amount}, wNow, t_w[0], awNow, t_aw[0])'.format(amount=self.visit(ctx.amount))
            return res
        else:
            raise Exception('Not handled, yet')


    # Visit a parse tree produced by TxScriptParser#requireCmd.
    def visitRequireCmd(self, ctx:TxScriptParser.RequireCmdContext):
        return 'If(\n\tNot(' + self.visit(ctx.child) + '), \n\t\tnext_state_tx(awNow, awNext, wNow, wNext), \n\t\t{subs})'


    # Visit a parse tree produced by TxScriptParser#skipCmd.
    def visitSkipCmd(self, ctx:TxScriptParser.SkipCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#groupCmd.
    def visitGroupCmd(self, ctx:TxScriptParser.GroupCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#assignCmd.
    def visitAssignCmd(self, ctx:TxScriptParser.AssignCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#ifelseCmd.
    def visitIfelseCmd(self, ctx:TxScriptParser.IfelseCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#seqCmd.
    def visitSeqCmd(self, ctx:TxScriptParser.SeqCmdContext):
        seq1 = self.visit(ctx.seq1)
        seq2 = self.visit(ctx.seq2)
        if self.__add_last_cmd:
            seq2 = 'And({seq2}, next_state_tx(t_aw[1], awNext, t_w[1], wNext))'.format(seq2=seq2)
            self.__add_last_cmd = False
        aux = seq1.format(subs=seq2)
        if aux == seq1:
            return 'And(\n\t{seq1},\n\t{seq2})'.format(seq1=seq1, seq2=seq2)
        else:
            return aux
    

    # Visit a parse tree produced by TxScriptParser#walletExpr.
    def visitWalletExpr(self, ctx:TxScriptParser.WalletExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#groupExpr.
    def visitGroupExpr(self, ctx:TxScriptParser.GroupExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#greaterEqExpr.
    def visitGreaterEqExpr(self, ctx:TxScriptParser.GreaterEqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#lessExpr.
    def visitLessExpr(self, ctx:TxScriptParser.LessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#neqExpr.
    def visitNeqExpr(self, ctx:TxScriptParser.NeqExprContext):
        return self.visitChildren(ctx)


    # # Visit a parse tree produced by TxScriptParser#variableExpr.
    # def visitVariableExpr(self, ctx:TxScriptParser.VariableExprContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#greaterExpr.
    def visitGreaterExpr(self, ctx:TxScriptParser.GreaterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#eqExpr.
    def visitEqExpr(self, ctx:TxScriptParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#notExpr.
    def visitNotExpr(self, ctx:TxScriptParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#sumSubEqExpr.
    def visitSumSubEqExpr(self, ctx:TxScriptParser.SumSubEqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + ctx.op.text + right


    # Visit a parse tree produced by TxScriptParser#lessEqExpr.
    def visitLessEqExpr(self, ctx:TxScriptParser.LessEqExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '<=' + right


    # Visit a parse tree produced by TxScriptParser#constExpr.
    def visitConstExpr(self, ctx:TxScriptParser.ConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#multDivEqExpr.
    def visitMultDivEqExpr(self, ctx:TxScriptParser.MultDivEqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#andExpr.
    def visitAndExpr(self, ctx:TxScriptParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return ctx.v.text


    # Visit a parse tree produced by TxScriptParser#strConstant.
    def visitStrConstant(self, ctx:TxScriptParser.StrConstantContext):
        if ctx.v.text == 'balance':
            return 'wNow'
        if ctx.v.text in self.__args_map:
            return self.__args_map[ctx.v.text]
        return ctx.v.text


    # Visit a parse tree produced by TxScriptParser#trueConstant.
    def visitTrueConstant(self, ctx:TxScriptParser.TrueConstantContext):
        return ctx.v.text


    # Visit a parse tree produced by TxScriptParser#falseConstant.
    def visitFalseConstant(self, ctx:TxScriptParser.FalseConstantContext):
        return ctx.v.text
