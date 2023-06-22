from antlr4 import *
from TxScriptLexer import *
from TxScriptParser import *
from TxScriptVisitor import *

class Z3Visitor(TxScriptVisitor):
    def __init__(self):
        self.__N = None
        self.__Agents = None
        self.__Tokens = None
        self.__globalVars = []
        self.__phiVars = set()
        self.__vectors = []
        self.__equation = None
        self.__mapInput = {}
        self.__mapAgent = {}
        self.__i = 0
        self.__j = 0

        ###
        # self.__tokensAgentsGive = {}
        # self.__tokensWalletsGet = {}
        self.__input = []
        # self.__nextStateAgents = {}
        # self.__nextStateTokens = {}


    # Visit a parse tree produced by TxScriptParser#contractExpr.
    def visitContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        self.__N = int(ctx.resBound.text)
        self.__Agents = int(ctx.agentBound.text)
        self.__Tokens = int(ctx.tokenBound.text)
        if ctx.gVars:
            self.visit(ctx.gVars)
        # for i in range(0, self.__Agents):
        #     self.__nextStateAgents['ag' + str(i)] = []
        # for i in range(0, self.__Tokens):
        #     self.__nextStateTokens['tk' + str(i)] = []
        formulas = self.visit(ctx.phis)
        selector, equation = self.visit(ctx.child)
        initGlobalVars = []
        for (ty, name, val) in self.__globalVars:
            initGlobalVars.append('{name}(0) == {val}'.format(name=name, val=val))
        # just for now until we add it in the DSL
        # for i in range(0, self.__Agents):
        #     for j in range(0, self.__Tokens):
        #         initGlobalVars.append('ag{ag}{tk}(0) == 5'.format(ag=i, tk=j))
        for j in range(0, self.__Tokens):
            initGlobalVars.append('tk{tk}(0) == 0'.format(tk=j))

        parseFunction = '''def parse(m):
    out = ''
    for i in range(0, {N}):
        out += '|' \n'''.format(N=self.__N+1)
        for j in range(0, self.__Tokens):
            parseFunction += '''        out += 'T{j}:' + str(m.eval(tk{j}(i))) + ' | ' \n'''.format(j=j)
        for i in range(1, self.__Agents+1):
            for j in range(0, self.__Tokens):
                parseFunction += '''        out += 'A{i}' + '[' + str(m.eval(ag{i}{j}(i))) + ':T{j}' + ']' + ' | ' \n'''.format(i=i,j=j)
        parseFunction += '''        out += '\\n' \n'''
        parseFunction += '''    return out'''
        
        parseFunctionOld = '''def parse(model):
    tokens = dict()
    for tk in range(0, {Tk}):
        tokens['tk' + str(tk)] = dict()
        eq = model.index('=', model.index('tk' + str(tk)))
        assignments = model[eq+3:model.index(']', eq)]
        for assignment in assignments.split(','):
            key = assignment[0:assignment.index('->')].strip()
            value = assignment[assignment.index('->')+2:].strip()
            tokens['tk' + str(tk)][key] = value
    agents = dict()
    for ag in range(1, {Ag}):
        for tk in range(0, {Tk}):
            agents['ag' + str(ag) + str(tk)] = dict()
            eq = model.index('=', model.index('ag' + str(ag) + str(tk)))
            assignments = model[eq+3:model.index(']', eq)]
            for assignment in assignments.split(','):
                key = assignment[0:assignment.index('->')].strip()
                value = assignment[assignment.index('->')+2:].strip()
                agents['ag' + str(ag) + str(tk)][key] = value
    sender = dict()
    eq = model.index('=', model.index('Sender'))
    assignments = model[eq+3:model.index(']', eq)]
    for assignment in assignments.split(','):
        key = assignment[0:assignment.index('->')].strip()
        value = assignment[assignment.index('->')+2:].strip()
        sender[key] = value
    time = dict()
    eq = model.index('=', model.index('Time'))
    assignments = model[eq+3:model.index(']', eq)]
    for assignment in assignments.split(','):
        key = assignment[0:assignment.index('->')].strip()
        value = assignment[assignment.index('->')+2:].strip()
        time[key] = value
    f = dict()
    eq = model.index('=', model.index('f'))
    assignments = model[eq+3:model.index(']', eq)]
    for assignment in assignments.split(','):
        key = assignment[0:assignment.index('->')].strip()
        value = assignment[assignment.index('->')+2:].strip()
        f[key] = value
    out = ''
    for i in range(0, {N}):
        out += '{name} '
        for tk in range(0, {Tk}):
            if str(i) in tokens['tk' + str(tk)]:
                out += '[' + tokens['tk' + str(tk)][str(i)] + ':' + 'T' + str(tk) + '] |'
            else:
                out += '[' + tokens['tk' + str(tk)]['else'] + ':' + 'T' + str(tk) + '] |'
        for ag in range(1, {Ag}):
            for tk in range(0, {Tk}):
                if str(i) in agents['ag' + str(ag) + str(tk)]:
                    out += 'A' + str(ag) + '[' + agents['ag' + str(ag) + str(tk)][str(i)] + ':' + 'T'+ str(tk) + '] |'
                else:
                    out += 'A' + str(ag) + '[' + agents['ag' + str(ag) + str(tk)]['else'] + ':' + 'T'+ str(tk) + '] |'
        out += '\\n'
        if str(i) in f:
            if int(f[str(i)]) >= len([{actions}]):
                out += '--> skip \\n'
            else:
                out += '--> ' + [{actions}][int(f[str(i)])] + '('
                if str(i) in sender:
                    out += 'A' + sender[str(i)] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)) + ')' + '@' + str(i) + '\\n'
                else:
                    out += 'A' + sender['else'] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)) + ')' + '@' + str(i) + '\\n'
        else:
            if int(f['else']) >= len([{actions}]):
                out += '--> skip \\n'
            else:
                out += '--> ' + [{actions}][int(f['else'])] + '('
                if str(i) in sender:
                    out += 'A' + sender[str(i)] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)).replace('tk', '') + ')' + '@' + str(i) + '\\n'
                else:
                    out += 'A' + sender['else'] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)).replace('tk', '') + ')' + '@' + str(i) + '\\n'
    return out

def getConsumerDown(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) > int(elems[j][str(i+1)]):
            return j
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) > int(elems[j][str(i+1)]):
            return j
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) > int(elems[j]['else']):
           return j
    return None
def getConsumerUp(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) < int(elems[j][str(i+1)]):
            return j
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) < int(elems[j][str(i+1)]):
            return j
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) < int(elems[j]['else']):
           return j
    return None
def getConsumerDownV(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) > int(elems[j][str(i+1)]):
            return int(elems[j][str(i)]) - int(elems[j][str(i+1)])
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) > int(elems[j][str(i+1)]):
            return int(elems[j]['else']) - int(elems[j][str(i+1)])
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) > int(elems[j]['else']):
            return int(elems[j][str(i)]) - int(elems[j]['else'])
    return None
def getConsumerUpV(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) < int(elems[j][str(i+1)]):
            return int(elems[j][str(i+1)]) - int(elems[j][str(i)])
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) < int(elems[j][str(i+1)]):
            return int(elems[j][str(i+1)]) - int(elems[j]['else'])
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) < int(elems[j]['else']):
           return int(elems[j]['else']) - int(elems[j][str(i)])
    return None'''.format(name=ctx.name.text, N=self.__N, Tk=self.__Tokens, Ag=self.__Agents+1, actions=','.join(['\'play\''])) # to be updated with actual actions
        return '''
from z3 import *
import time

N = {N}

{selector}

s = Solver()

s.add(And({initGlobalVars}))

for i in range(N):
    s.add({equation})

timeStart = time.time()

queries = [
    {phis}
]

{parse}

for q in queries:
    print(str(q) + " : ", end = '')
    if s.check(q)==sat:
        print(" sat")
        print(parse(s.model()))
    else:
        print(" unsat")

timeTot = time.time() - timeStart
print("Solving time: " + str(timeTot) + "s")
        '''.format(N=self.__N, selector=selector, equation=equation, phis=',\n\t'.join(formulas), initGlobalVars=', '.join(initGlobalVars), parse=parseFunction)


    # Visit a parse tree produced by TxScriptParser#proceduresExpr.
    def visitProceduresExpr(self, ctx:TxScriptParser.ProceduresExprContext):
        equations = []
        for procedure in ctx.procedureExpr():
            equations.append(self.visit(procedure))
            self.__j = self.__j + 1
        aux = None
        # foundA = [False for i in range(0, len(self.__input))]
        # foundT = [False for i in range(0, len(self.__input))]
        for i in range(0, len(ctx.procedureExpr())):
            equation = None
            for ag in range(1, self.__Agents+1):
                for tk in range(0, self.__Tokens):
                    # i = 0
                    aux = None
                    for (a, t, m, eq) in self.__input[i]:
                        foundA = False
                        foundT = False
                        equationAux = equations[i][2].format(ag=ag, tk=tk)
                        a = a.format(ag=ag, tk=tk)
                        t = t.format(ag=ag, tk=tk)
                        equationAux = equationAux.replace(a+'(i)', '('+a+'(i)-'+self.__mapInput[m]+'(i))')
                        equationAux = equationAux.replace(t+'(i)', '('+t+'(i)+'+self.__mapInput[m]+'(i))')
                        # if (a+'(i+1)') in equationAux or (a+'(i)') in equationAux:
                        #     foundA= True
                        # if (t+'(i+1)') in equationAux or (t+'(i)') in equationAux:
                        #     foundT = True
                        # # i = i + 1
                        # if not foundA or not foundT:
                        #     equationAux = eq.format(ag=ag, tk=tk) + ', ' + equationAux
                        equationAux = a + '(i)>=' + self.__mapInput[m] + '(i), ' + equationAux
                        equationAux = 'Time(i)>={start}, Time(i)<{end}, '.format(start=equations[i][0], end=equations[i][1]) + equationAux
                        if aux:
                            aux = aux + ', ' + equationAux
                        else:
                            aux = equationAux
                    for ag1 in range(1, self.__Agents+1):
                        for tk1 in range(0, self.__Tokens):
                            if 'ag{ag}{tk}(i+1)=='.format(ag=ag1, tk=tk1) not in aux:
                                aux = aux + ', ag{ag}{tk}(i+1)==ag{ag}{tk}(i)'.format(ag=ag1, tk=tk1)
                    for tk1 in range(0, self.__Tokens):
                        if 'tk{tk}(i+1)=='.format(tk=tk1) not in aux:
                            aux = aux + ', tk{tk}(i+1)==tk{tk}(i)'.format(tk=tk1)
                    # for j in self.__mapInput.keys():
                    #     if '{xs}(i+1)==' not in aux:
                    #         aux = aux + ',' + '{xs}(i+1)=={xs}(i)'.format(xs=self.__mapInput[j])
                    for (_, name, _) in self.__globalVars:
                        if '{name}(i+1)=='.format(name=name) not in aux:
                            aux = aux + ', {name}(i+1)=={name}(i)'.format(name=name)
                    condition = 'And(f(i)=={i}, Sender(i)=={ag})'.format(i=i, ag=ag)
                    if equation:
                        equation = equation + ', If(' + condition + ', ' + 'And(' + aux + ')'
                    else:
                        equation = 'If(' + condition + ', ' + 'And(' + aux + ')'
        equation = equation + ', And('
        first = True
        for ag in range(1, self.__Agents+1):
            for tk in range(0, self.__Tokens):
                if first:
                    first = False
                else:
                    equation = equation + ', '
                equation = equation + 'ag{ag}{tk}(i+1)==ag{ag}{tk}(i)'.format(ag=ag, tk=tk)
        for tk in range(0, self.__Tokens):
            equation = equation + ', tk{tk}(i+1)==tk{tk}(i)'.format(tk=tk)
        # for j in self.__mapInput.keys():
        #     equation = equation + ',' + '{xs}(i+1)=={xs}(i)'.format(xs=self.__mapInput[j])
        for (_, name, _) in self.__globalVars:
            equation = equation + ', ' + '{name}(i+1)=={name}(i)'.format(name=name)
        equation = equation + ')'
        for j in range(0, len(ctx.procedureExpr())*self.__Agents*self.__Tokens):
            equation = equation + ')'
        # for i in range(1, len(ctx.procedureExpr())):
        #     aux = None
        #     for ag in range(0, self.__Agents):
        #         for tk in range(0, self.__Tokens):
        #             if aux:
        #                 aux = 'And(' + aux + ', ' + equations[i][2].format(ag=ag, tk=tk) + ')'
        #             else:
        #                 aux = equations[i][2].format(ag=ag, tk=tk)
        #     aux = 'And(' + 'Time(i)>={start}, Time(i)<{end}, '.format(start=equations[i][0], end=equations[i][1]) + aux + ')'
        #     equation = 'And(f(i)=={i}, '.format(i=i) + aux + ')'
        #     equation = 'Or(' + equation + ',' + aux + ')'
        # equation = 'for i in range(N):\n\t'.format(N = self.__N) + equation
        # selector = 'f = IntVector(\'f\', {n})'.format(n = self.__N) #len(ctx.procedureExpr()))
        selector = 'f = Function(\'f\', IntSort(), IntSort())'
        # selector = selector + '\n' + 'Time = IntVector(\'Time\', {n})'.format(n = self.__N)
        selector = selector + '\n' + 'Time = Function(\'Time\', IntSort(), IntSort())'
        selector = selector + '\n' + 'Sender = Function(\'Sender\', IntSort(), IntSort())'
        for v in self.__phiVars:
            selector = selector + '\n' + '{v} = Int(\'{v}\')'.format(v=v)
        for (ty, name, val) in self.__globalVars:
            if ty == 'int':
                # selector = selector + '\n' + '{name} = IntVector(\'{name}\', {n})'.format(name=name, n=self.__N)
                selector = selector + '\n' + '{name} = Function(\'{name}\', IntSort(), IntSort())'.format(name=name)
            elif ty == 'bool':
                # selector = selector + '\n' + '{name} = BoolVector(\'{name}\', {n})'.format(name=name, n=self.__N)
                  selector = selector + '\n' + '{name} = Function(\'{name}\', IntSort(), BoolSort())'.format(name=name)
            else:
                # selector = selector + '\n' + '{name} = RealVector(\'{name}\', {n})'.format(name=name, n=self.__N)
                selector = selector + '\n' + '{name} = Function(\'{name}\', IntSort(), RealSort())'.format(name=name)
            # selector = selector + '\n' + '{name}[0] = {val}'.format(name=name, val=val)
        for i in range(1, self.__Agents+1):
            for j in range(0, self.__Tokens):
              # selector = selector + '\n' + 'ag{i}{j} = IntVector(\'ag{i}{j}\', {n})'.format(i = i, j=j, n = self.__N)
                selector = selector + '\n' + 'ag{i}{j} = Function(\'ag{i}{j}\', IntSort(), IntSort())'.format(i = i, j=j)
        for i in range(0, self.__Tokens):
            # selector = selector + '\n' + 'tk{i} = IntVector(\'tk{i}\', {n})'.format(i = i, n = self.__N)
              selector = selector + '\n' + 'tk{i} = Function(\'tk{i}\', IntSort(), IntSort())'.format(i = i)
        for i in self.__mapInput.keys():
            # selector = selector + '\n' + '{xs} = IntVector(\'{xs}\', {n})'.format(xs=self.__mapInput[i], n = self.__N)
              selector = selector + '\n' + '{xs} = Function(\'{xs}\', IntSort(), IntSort())'.format(xs=self.__mapInput[i])
        self.__vectors.append(selector)

        # i = 0
        # for (a, t, m, eq) in self.__input:
        #     if not foundA[i] or not foundT[i]:
        #         equation = eq + ', ' + equation
        #     i = i+1

        return selector, equation


    # Visit a parse tree produced by TxScriptParser#procedureExpr.
    def visitProcedureExpr(self, ctx:TxScriptParser.ProcedureExprContext):
        start = 0 if ctx.start.text == '_' else int(ctx.start.text)
        end = self.__N if ctx.end.text == '_' else int(ctx.end.text)
        preconditions = self.visit(ctx.preconditions)
        pArgs = self.visit(ctx.pArgs)
        body = self.visit(ctx.body)
        return (start, end, preconditions + ', ' + body) # TBC
        # TBD


    # Visit a parse tree produced by TxScriptParser#preconditionsExpr.
    def visitPreconditionsExpr(self, ctx:TxScriptParser.PreconditionsExprContext):
        equation = None
        for precondition in ctx.expression():
            if equation:
                equation = equation + ', ' + self.visit(precondition)
            else:
                equation = self.visit(precondition)
        return equation


    # Visit a parse tree produced by TxScriptParser#LessEq.
    def visitLessEq(self, ctx:TxScriptParser.LessEqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '<=' + right


    # Visit a parse tree produced by TxScriptParser#SumSubEq.
    def visitSumSubEq(self, ctx:TxScriptParser.SumSubEqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + ctx.op.text + right


    # Visit a parse tree produced by TxScriptParser#constant.
    def visitConstant(self, ctx:TxScriptParser.ConstantContext):
        return self.visit(ctx.child)


    # Visit a parse tree produced by TxScriptParser#null.
    def visitNull(self, ctx:TxScriptParser.NullContext):
        return


    # Visit a parse tree produced by TxScriptParser#Wallet.
    def visitWallet(self, ctx:TxScriptParser.WalletContext):
        # assuming for now just variable xt
        child = self.visit(ctx.child)
        return child + '(i)'


    # Visit a parse tree produced by TxScriptParser#variable.
    def visitVariable(self, ctx:TxScriptParser.VariableContext):
        if ctx.child.text == 'xt':
            return 'tk{tk}'
        if ctx.child.text not in self.__mapInput:
            self.__mapInput[ctx.child.text] = ctx.child.text + str(self.__i)
            self.__i = self.__i + 1
        return self.__mapInput[ctx.child.text] + '(i)'


    # Visit a parse tree produced by TxScriptParser#GreaterEq.
    def visitGreaterEq(self, ctx:TxScriptParser.GreaterEqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '>=' + right


    # Visit a parse tree produced by TxScriptParser#Greater.
    def visitGreater(self, ctx:TxScriptParser.GreaterContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '>' + right


    # Visit a parse tree produced by TxScriptParser#NEq.
    def visitNEq(self, ctx:TxScriptParser.NEqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '!=' + right


    # Visit a parse tree produced by TxScriptParser#MultDivEq.
    def visitMultDivEq(self, ctx:TxScriptParser.MultDivEqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + ctx.op.text + right


    # Visit a parse tree produced by TxScriptParser#Eq.
    def visitEq(self, ctx:TxScriptParser.EqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '==' + right


    # Visit a parse tree produced by TxScriptParser#Less.
    def visitLess(self, ctx:TxScriptParser.LessContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left + '<' + right


    # Visit a parse tree produced by TxScriptParser#variableArg.
    def visitVariableArg(self, ctx:TxScriptParser.VariableArgContext):
        if ctx.variable.text not in self.__mapInput:
            self.__mapInput[ctx.variable.text] = ctx.variable.text + str(self.__i)
            self.__i = self.__i + 1
        return self.__mapInput[ctx.variable.text]
        # self.__mapInput[ctx.variable.text] = self.__i
        # self.__i = self.__i + 1


    # Visit a parse tree produced by TxScriptParser#inputToken.
    def visitInputToken(self, ctx:TxScriptParser.InputTokenContext):
        # for now we only consider the scenario where all three are variables (a?x:t)
        amount = ctx.data.text
        if self.__j >= len(self.__input):
            self.__input.append(set())
        self.__input[self.__j].add(('ag{ag}{tk}', 'tk{tk}', amount, 'And(' + 'ag{ag}{tk}(i)>=' + amount + ', And(' + 'tk{tk}(i+1)==tk{tk}(i)+' + amount + '(i), ' + 'ag{ag}{tk}(i+1)==ag{ag}{tk}(i)-' + amount + '(i)))'))
        # return ''


    # Visit a parse tree produced by TxScriptParser#sequence.
    def visitSequence(self, ctx:TxScriptParser.SequenceContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return 'And(' + left + ', ' + right + ')'


    # Visit a parse tree produced by TxScriptParser#ifstatement.
    def visitIfstatement(self, ctx:TxScriptParser.IfstatementContext):
        condition = self.visit(ctx.condition)
        first = self.visit(ctx.first)
        second = self.visit(ctx.second)
        return 'If(' + condition + ', ' + first + ', ' + second + ')'


    # Visit a parse tree produced by TxScriptParser#outputToken.
    def visitOutputToken(self, ctx:TxScriptParser.OutputTokenContext):
        # for now we assume all variables (a!x:t)
        amount = self.visit(ctx.data)
        # for i in range(0, self.__Agents):
        #     self.__nextStateAgents['ag' + str(i)].append('+' + amount)
        # for i in range(0, self.__Tokens):
        #     self.__nextStateTokens['tk' + str(i)].append('-' + amount)
        # return ''
        return 'And(' + 'tk{tk}(i+1)==tk{tk}(i)-' + amount + ', ' + 'ag{ag}{tk}(i+1)==ag{ag}{tk}(i)+' + amount + ')'


    # Visit a parse tree produced by TxScriptParser#skipBody.
    def visitSkipBody(self, ctx:TxScriptParser.SkipBodyContext):
        return 'And(ag{ag}{tk}(i+1)==ag{ag}{tk}(i), tk{tk}(i+1)==tk{tk}(i))'
        # return 'True'


    # Visit a parse tree produced by TxScriptParser#assignmentBody.
    def visitAssignmentBody(self, ctx:TxScriptParser.AssignmentBodyContext):
        child = self.visit(ctx.child)
        if ctx.variable.text not in self.__mapInput:
            self.__mapInput[ctx.variable.text] = self.__i
            self.__i = self.__i + 1
        return self.__mapInput[ctx.variable.text] + '(i)==' + child



    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return ctx.v.text


    # Visit a parse tree produced by TxScriptParser#agentOrTokenConstant.
    def visitAgentOrTokenConstant(self, ctx:TxScriptParser.AgentOrTokenConstantContext):
        return ctx.v.text

# Visit a parse tree produced by TxScriptParser#firstOrderFormulasExpr.
    def visitFirstOrderFormulasExpr(self, ctx:TxScriptParser.FirstOrderFormulasExprContext):
        formulas = []
        for phi in ctx.firstOrderFormulaExpr():
            formulas.append(self.visit(phi))
        return formulas


    # Visit a parse tree produced by TxScriptParser#functionFormula.
    def visitFunctionFormula(self, ctx:TxScriptParser.FunctionFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#NEqFormula.
    def visitNEqFormula(self, ctx:TxScriptParser.NEqFormulaContext):
        return self.visit(ctx.left) + '!=' + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#MultDivEqFormula.
    def visitMultDivEqFormula(self, ctx:TxScriptParser.MultDivEqFormulaContext):
        return self.visit(ctx.left) + '*' + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#LessEqFormula.
    def visitLessEqFormula(self, ctx:TxScriptParser.LessEqFormulaContext):
        return self.visit(ctx.left) + '<=' + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#atomFormula.
    def visitAtomFormula(self, ctx:TxScriptParser.AtomFormulaContext):
        return ctx.child.text

    # Visit a parse tree produced by TxScriptParser#atomFormula.
    def visitAtomFormulaN(self, ctx:TxScriptParser.AtomFormulaNContext):
        if ctx.child.text not in self.__mapInput:
            self.__mapInput[ctx.child.text] = ctx.child.text + str(self.__i)
            self.__i = self.__i + 1
        return self.__mapInput[ctx.child.text] + '(' + ctx.n.text + ')'

    # Visit a parse tree produced by TxScriptParser#andFormula.
    def visitAndFormula(self, ctx:TxScriptParser.AndFormulaContext):
        return 'And(' + self.visit(ctx.left) + ',' + self.visit(ctx.right) + ')'


    # Visit a parse tree produced by TxScriptParser#notFormula.
    def visitNotFormula(self, ctx:TxScriptParser.NotFormulaContext):
        return 'Not(' + self.visit(ctx.child) + ')'


    # Visit a parse tree produced by TxScriptParser#existsFormula.
    def visitExistsFormula(self, ctx:TxScriptParser.ExistsFormulaContext):
        self.__phiVars.add(ctx.var.text)
        return 'Exists(' + ctx.var.text + ',' + self.visit(ctx.child) + ')'


    # Visit a parse tree produced by TxScriptParser#orFormula.
    def visitOrFormula(self, ctx:TxScriptParser.OrFormulaContext):
        return 'Or(' + self.visit(ctx.left) + ',' + self.visit(ctx.right) + ')'


    # Visit a parse tree produced by TxScriptParser#GreaterEqFormula.
    def visitGreaterEqFormula(self, ctx:TxScriptParser.GreaterEqFormulaContext):
        return self.visit(ctx.left) + '>=' + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#SumSubEqFormula.
    def visitSumSubEqFormula(self, ctx:TxScriptParser.SumSubEqFormulaContext):
        return self.visit(ctx.left) + ctx.op.text + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#forallFormula.
    def visitForallFormula(self, ctx:TxScriptParser.ForallFormulaContext):
        self.__phiVars.add(ctx.var.text)
        return 'ForAll(' + ctx.var.text + ',' + self.visit(ctx.child) + ')'


    # Visit a parse tree produced by TxScriptParser#GreaterFormula.
    def visitGreaterFormula(self, ctx:TxScriptParser.GreaterFormulaContext):
        return self.visit(ctx.left) + '>' + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#EqFormula.
    def visitEqFormula(self, ctx:TxScriptParser.EqFormulaContext):
        return self.visit(ctx.left) + '==' + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#LessFormula.
    def visitLessFormula(self, ctx:TxScriptParser.LessFormulaContext):
        return self.visit(ctx.left) + '<' + self.visit(ctx.right)


    # Visit a parse tree produced by TxScriptParser#impliesFormula.
    def visitImpliesFormula(self, ctx:TxScriptParser.ImpliesFormulaContext):
        return 'Implies(' + self.visit(ctx.left) + ',' + self.visit(ctx.right) + ')'

    # Visit a parse tree produced by TxScriptParser#sumFormula.
    def visitSumFormula(self, ctx:TxScriptParser.SumFormulaContext):
        equation = self.visit(ctx.child)
        sums = []
        for i in range(int(ctx.varMin.text), int(ctx.varMax.text)):
            sums.append(equation.replace(ctx.var.text, str(i)))
        return '(' + '+'.join(sums) + ')'

    # Visit a parse tree produced by TxScriptParser#impliesFormula.
    def visitGroupFormula(self, ctx:TxScriptParser.ImpliesFormulaContext):
        return self.visit(ctx.child)

    # Visit a parse tree produced by TxScriptParser#tokenijn.
    def visitToken0jn(self, ctx:TxScriptParser.TokenijnContext):
        return 'tk{j}({n})'.format(j=ctx.j.text, n=ctx.n.text)

    # Visit a parse tree produced by TxScriptParser#tokenijn.
    def visitTokenijn(self, ctx:TxScriptParser.TokenijnContext):
        if ctx.i.text == '0':
            return 'tk{j}({n})'.format(j=ctx.j.text, n=ctx.n.text)
        else:
            return 'ag{i}{j}({n})'.format(i=ctx.i.text, j=ctx.j.text, n=ctx.n.text)

    def visitGVarn(self, ctx:TxScriptParser.TokenijnContext):
        return '{name}({n})'.format(name=ctx.x.text, n=ctx.n.text)

    # Visit a parse tree produced by TxScriptParser#globalVarsExpr.
    def visitGlobalVarsExpr(self, ctx:TxScriptParser.GlobalVarsExprContext):
        for gVar in ctx.globalVarExpr():
            self.__globalVars.append(self.visit(gVar))

    # Visit a parse tree produced by TxScriptParser#globalVarExpr.
    def visitGlobalVarExpr(self, ctx:TxScriptParser.GlobalVarExprContext):
        return (ctx.ty.text, ctx.name.text, ctx.val.text)
