from antlr4 import *
from TxScriptLexer import *
from TxScriptParser import *
from TxScriptVisitor import *

class Z3Visitor(TxScriptVisitor):
    def __init__(self):
        self.__N = None
        self.__Agents = None
        self.__Tokens = None
        self.__vectors = []
        self.__equation = None
        self.__mapInput = {}
        self.__mapAgent = {}
        self.__i = 0
        ###
        # self.__tokensAgentsGive = {}
        # self.__tokensWalletsGet = {}
        self.__input = set()
        # self.__nextStateAgents = {}
        # self.__nextStateTokens = {}


    # Visit a parse tree produced by TxScriptParser#contractExpr.
    def visitContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        self.__N = int(ctx.resBound.text)
        self.__Agents = int(ctx.agentBound.text)
        self.__Tokens = int(ctx.tokenBound.text)
        # for i in range(0, self.__Agents):
        #     self.__nextStateAgents['ag' + str(i)] = []
        # for i in range(0, self.__Tokens):
        #     self.__nextStateTokens['tk' + str(i)] = []
        return (ctx.name.text, self.visit(ctx.child))


    # Visit a parse tree produced by TxScriptParser#proceduresExpr.
    def visitProceduresExpr(self, ctx:TxScriptParser.ProceduresExprContext):
        equations = []
        for procedure in ctx.procedureExpr():
            equations.append(self.visit(procedure))
        aux = None
        # foundA = [False for i in range(0, len(self.__input))]
        # foundT = [False for i in range(0, len(self.__input))]
        for ag in range(0, self.__Agents):
            for tk in range(0, self.__Tokens):
                # foundTK = False
                # equationAuxAg = None
                # for side_effect in self.__nextStateAgents['ag' + str(ag)]:
                #     if side_effect.startswith('+'):
                #         if side_effect[1:].startswith('tk'):
                #             foundTK = True
                #         if equationAuxAg:
                #             equationAuxAg = equationAuxAg + side_effect.format(ag=ag, tk=tk)
                #         else:
                #             equationAuxAg = side_effect.format(ag=ag, tk=tk)
                # for side_effect in self.__nextStateAgents['ag' + str(ag)]:
                #     if side_effect.startswith('-'):
                #         if side_effect[1:].startswith('ag') or side_effect[1:].startswith('tk') or not foundTK:
                #             if equationAuxAg:
                #                 equationAuxAg = equationAuxAg + side_effect.format(ag=ag, tk=tk)
                #             else:
                #                 equationAuxAg = side_effect.format(ag=ag, tk=tk)
                # equationAuxAg = 'ag{ag}[i+1]==ag{ag}[i]'.format(ag=ag) + equationAuxAg
                # foundTK = False
                # equationAuxTk = None
                # for side_effect in self.__nextStateTokens['tk' + str(tk)]:
                #     if side_effect.startswith('-'):
                #         if side_effect[1:].startswith('tk'):
                #             foundTK = True
                #         if equationAuxTk:
                #             equationAuxTk = equationAuxAg + side_effect.format(ag=ag, tk=tk)
                #         else:
                #             equationAuxTk = side_effect.format(ag=ag, tk=tk)
                # for side_effect in self.__nextStateTokens['tk' + str(tk)]:
                #     if side_effect.startswith('+'):
                #         if side_effect[1:].startswith('ag') or side_effect[1:].startswith('tk') or not foundTK:
                #             if equationAuxTk:
                #                 equationAuxTk = equationAuxTk + side_effect.format(ag=ag, tk=tk)
                #             else:
                #                 equationAuxTk = side_effect.format(ag=ag, tk=tk)
                # equationAuxTk = 'tk{tk}[i+1]==tk{tk}[i]'.format(tk=tk) + equationAuxTk
                # equationAux = 'And(' + equationAuxAg + ', ' + equationAuxTk + ')'
                i = 0
                for (a, t, m, eq) in self.__input:
                    foundA = False
                    foundT = False
                    equationAux = equations[0].format(ag=ag, tk=tk)
                    a = a.format(ag=ag)
                    t = t.format(tk=tk)
                    print(equationAux)
                    equationAux = equationAux.replace(a+'[i]', '('+a+'[i]-'+self.__mapInput[m]+'[i])')
                    equationAux = equationAux.replace(t+'[i]', '('+t+'[i]+'+self.__mapInput[m]+'[i])')
                    print(equationAux + '\n')
                    if (a+'[i+1]') in equationAux or (a+'[i]') in equationAux:
                        foundA= True
                    if (t+'[i+1]') in equationAux or (t+'[i]') in equationAux:
                        foundT = True
                    i = i + 1
                    if not foundA or not foundT:
                        equationAux = eq.format(ag=ag, tk=tk) + ', ' + equationAux
                if aux:
                    aux = 'Or(' + aux + ', ' + equationAux + ')'
                else:
                    aux = equationAux
        equation = 'And(f(i)==0, ' + aux + ')'
        for i in range(1, len(ctx.procedureExpr())):
            aux = None
            for ag in range(0, self.__Agents):
                for tk in range(0, self.__Tokens):
                    if aux:
                        aux = 'And(' + aux + ', ' + equations[i].format(ag=ag, tk=tk) + ')'
                    else:
                        aux = equations[i].format(ag=ag, tk=tk)
            equation = 'And(f(i)==1, ' + aux + ')'
            equation = 'Or(' + equation + ',' + aux + ')'
        equation = 'for i in range(N):\n\t'.format(N = self.__N) + equation
        selector = 'f = IntVector(\'f\', {n})'.format(n = len(ctx.procedureExpr()))
        for i in range(0, self.__Agents):
            selector = selector + '\n' + 'ag{i} = IntVector(\'ag{i}\', {n})'.format(i = i, n = self.__N)
        for i in range(0, self.__Tokens):
            selector = selector + '\n' + 'tk{i} = IntVector(\'tk{i}\', {n})'.format(i = i, n = self.__N)
        for i in self.__mapInput.keys():
            selector = selector + '\n' + '{xs} = IntVector(\'{xs}\', {n})'.format(xs=self.__mapInput[i], n = self.__N)
        self.__vectors.append(selector)

        # i = 0
        # for (a, t, m, eq) in self.__input:
        #     if not foundA[i] or not foundT[i]:
        #         equation = eq + ', ' + equation
        #     i = i+1

        return selector + '\n\n' + equation


    # Visit a parse tree produced by TxScriptParser#procedureExpr.
    def visitProcedureExpr(self, ctx:TxScriptParser.ProcedureExprContext):
        preconditions = self.visit(ctx.preconditions)
        pArgs = self.visit(ctx.pArgs)
        body = self.visit(ctx.body)
        return 'And(' + preconditions + ', ' + body + ')' # TBC
        # TBD


    # Visit a parse tree produced by TxScriptParser#preconditionsExpr.
    def visitPreconditionsExpr(self, ctx:TxScriptParser.PreconditionsExprContext):
        equation = None
        for precondition in ctx.expression():
            if equation:
                equation = 'And(' + equation + ', ' + self.visit(precondition) + ')'
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
        return child + '[i]'


    # Visit a parse tree produced by TxScriptParser#variable.
    def visitVariable(self, ctx:TxScriptParser.VariableContext):
        if ctx.child.text == 'xt':
            return 'tk{tk}'
        if ctx.child.text not in self.__mapInput:
            self.__mapInput[ctx.child.text] = ctx.child.text + str(self.__i)
            self.__i = self.__i + 1
        return self.__mapInput[ctx.child.text] + '[i]'


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
        # for i in range(0, self.__Agents):
        #     self.__nextStateAgents['ag' + str(i)].append('-' + amount)
        # for i in range(0, self.__Tokens):
        #     self.__nextStateTokens['tk' + str(i)].append('+' + amount)
        self.__input.add(('ag{ag}', 'tk{tk}', amount, 'And(' + 'tk{tk}[i+1]==tk{tk}[i]+' + amount + '[i], ' + 'ag{ag}[i+1]==ag{ag}[i]-' + amount + '[i])'))
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
        return 'And(' + 'tk{tk}[i+1]==tk{tk}[i]-' + amount + ', ' + 'ag{ag}[i+1]==ag{ag}[i]+' + amount + ')'


    # Visit a parse tree produced by TxScriptParser#skipBody.
    def visitSkipBody(self, ctx:TxScriptParser.SkipBodyContext):
        # equation = 'ag0' '[i+1] = ag0' + '[i]'
        # for ag in range(1, self.__Agents):
        #     equation = 'And(' + equation + ', ' + 'ag' + str(ag) + '[i+1] == ag' + str(ag) + '[i]' + ')'
        # for tk in range(0, self.__Tokens):
        #     equation = 'And(' + equation + ', ' + 'tk' + str(tk) + '[i+1] == tk' + str(tk) + '[i]' + ')'
        # for v in self.__mapInput.keys():
        #     equation = 'And(' + equation + ', ' + self.__mapInput[v] + '[i+1] == ' + self.__mapInput[v] + '[i]' + ')'
        # return equation
        return 'True'


    # Visit a parse tree produced by TxScriptParser#assignmentBody.
    def visitAssignmentBody(self, ctx:TxScriptParser.AssignmentBodyContext):
        child = self.visit(ctx.child)
        if ctx.variable.text not in self.__mapInput:
            self.__mapInput[ctx.variable.text] = self.__i
            self.__i = self.__i + 1
        return self.__mapInput[ctx.variable.text] + '[i]==' + child



    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return ctx.v.text


    # Visit a parse tree produced by TxScriptParser#agentOrTokenConstant.
    def visitAgentOrTokenConstant(self, ctx:TxScriptParser.AgentOrTokenConstantContext):
        return ctx.v.text
