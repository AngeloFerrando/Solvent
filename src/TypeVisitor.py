import copy
from antlr4 import *
from TxScriptLexer import *
from TxScriptParser import *
from TxScriptVisitor import *

class TypeError(Exception):
    def __init__(self, ctx, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message + f' (line {ctx.start.line}, column {ctx.start.column})')

class TypeVisitor(TxScriptVisitor):

    def __init__(self):
        self.__const = False
        self.__globals = []
        self.__globals_const = {}
        self.__maps = set()
        self.__prefix = ''
        self.__prop_name = ''
        self.__prop_names = set()
        self.__args_map = {}
        self.__old = 0
        self.__function_args_types = {}
        self.__vars = {}

    # Visit a parse tree produced by TxScriptParser#contractExpr.
    def visitContractExpr(self, ctx:TxScriptParser.ContractExprContext):
        self.visit(ctx.decl)
        self.visit(ctx.properties)


    # Visit a parse tree produced by TxScriptParser#constFieldDecl.
    # def visitConstFieldDecl(self, ctx:TxScriptParser.ConstFieldDeclContext):
    #     self.__const = True
    #     self.visit(ctx.child)
    #     self.__const = False


    # Visit a parse tree produced by TxScriptParser#declsExpr.
    def visitDeclsExpr(self, ctx:TxScriptParser.DeclsExprContext):
        self.visitChildren(ctx)
            
    

    # Visit a parse tree produced by TxScriptParser#propertiesExpr.
    def visitPropertiesExpr(self, ctx:TxScriptParser.PropertiesExprContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#propertyExpr.
    def visitPropertyExpr(self, ctx:TxScriptParser.PropertyExprContext):
        self.__prop_name = ctx.name.text
        self.__prop_names.add(self.__prop_name)
        self.visit(ctx.phi)


    # Visit a parse tree produced by TxScriptParser#secretDecl.
    def visitSecretDecl(self, ctx:TxScriptParser.SecretDeclContext):
        self.__globals.append((ctx.var.text, 'Secret'))
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const


    # Visit a parse tree produced by TxScriptParser#hashDecl.
    def visitHashDecl(self, ctx:TxScriptParser.HashDeclContext):
        self.__globals.append((ctx.var.text, 'Hash'))
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const

    # Visit a parse tree produced by TxScriptParser#intDecl.
    def visitIntDecl(self, ctx:TxScriptParser.IntDeclContext):
        self.__globals.append((ctx.var.text, 'Int'))
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const

    
    # Visit a parse tree produced by TxScriptParser#uintDecl.
    def visitUintDecl(self, ctx:TxScriptParser.UintDeclContext):
        self.__globals.append((ctx.var.text, 'Uint'))
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const


    # Visit a parse tree produced by TxScriptParser#boolDecl.
    def visitBoolDecl(self, ctx:TxScriptParser.BoolDeclContext):
        self.__globals.append((ctx.var.text, 'Bool'))
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const


    # Visit a parse tree produced by TxScriptParser#strDecl.
    def visitStrDecl(self, ctx:TxScriptParser.StrDeclContext):
        self.__globals.append((ctx.var.text, 'String'))
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const


    # Visit a parse tree produced by TxScriptParser#addrDecl.
    def visitAddrDecl(self, ctx:TxScriptParser.AddrDeclContext):
        self.__globals.append((ctx.var.text, 'Address'))
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const


    # Visit a parse tree produced by TxScriptParser#mapAddrDecl.
    def visitMapAddrDeclInt(self, ctx:TxScriptParser.MapAddrDeclIntContext):
        self.__globals.append((ctx.var.text, ('MapAddr', 'Int')))
        self.__maps.add(ctx.var.text)
        self.__globals_const[ctx.var.text] = True if ctx.const else False #self.__const


    # Visit a parse tree produced by TxScriptParser#constrDecl.
    def visitConstrDecl(self, ctx:TxScriptParser.ConstrDeclContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#nonPayableConstructorDecl.
    def visitNonPayableConstructorDecl(self, ctx:TxScriptParser.NonPayableConstructorDeclContext):
        self.__prefix = 'constructor'
        self.visitFun(ctx)
    

    # Visit a parse tree produced by TxScriptParser#payableConstructorDecl.
    def visitPayableConstructorDecl(self, ctx:TxScriptParser.PayableConstructorDeclContext):
        self.__prefix = 'constructor'
        self.visitFun(ctx)


    # Visit a parse tree produced by TxScriptParser#payableFunDecl.
    def visitPayableFunDecl(self, ctx:TxScriptParser.PayableFunDeclContext):
        self.__prefix = ctx.name.text + '_func'
        self.visitFun(ctx)


    # Visit a parse tree produced by TxScriptParser#nonPayableFunDecl.
    def visitNonPayableFunDecl(self, ctx:TxScriptParser.NonPayableFunDeclContext):
        self.__prefix = ctx.name.text + '_func'
        self.visitFun(ctx)


    # Visit a parse tree produced by TxScriptParser#funDecl.
    def visitFun(self, ctx):
        self.__function_args_types[self.__prefix] = []
        self.visit(ctx.args)
        self.visit(ctx.cmds)


    # Visit a parse tree produced by TxScriptParser#argsExpr.
    def visitArgsExpr(self, ctx:TxScriptParser.ArgsExprContext):
        for arg in ctx.argExpr():
            name = self.__prefix + '_' + arg.var.text
            type = arg.ty.text
            if type in ['int', 'uint', 'bool', 'address', 'string', 'hash', 'secret']:
                type = type.capitalize()
            else:
                type = ('MapAddr', 'Int')
            self.__args_map[name] = type
            self.__function_args_types[self.__prefix].append(type)


    # Visit a parse tree produced by TxScriptParser#sendCmd.
    def visitSendCmd(self, ctx:TxScriptParser.SendCmdContext):
        # sender = ctx.sender.text
        sender = self.visit(ctx.sender)
        
        if sender != 'sender' and sender != 'msg.sender' and sender != 'xa1':
            for (v, t) in self.__globals:
                if sender == v and t != 'Address':
                    raise TypeError(ctx, 'Send command requires an address (i.e., the receiver)')
            if sender in self.__args_map and self.__args_map[sender] != 'Address':
                raise TypeError(ctx, 'Send command requires an address (i.e., the receiver)')
            
        amount = self.visit(ctx.amount)
        if amount != 'Int' and amount != 'Uint':
            raise TypeError(ctx, 'Send command requires an integer amount to be sent')

    # Visit a parse tree produced by TxScriptParser#requireCmd.
    def visitRequireCmd(self, ctx:TxScriptParser.RequireCmdContext):
        if self.visit(ctx.child) != 'Bool':
            raise TypeError(ctx, 'Require command requires a boolean condition')


    # Visit a parse tree produced by TxScriptParser#assignCmd.
    def visitAssignCmd(self, ctx:TxScriptParser.AssignCmdContext):
        left = ctx.var.text
        if left in self.__globals_const and self.__globals_const[left] and self.__prefix != 'constructor':
            raise TypeError(ctx, f'{left} is immutable, so values cannot be assigned to it outside the constructor')
        
        t_left = self.get_type(ctx, left)
        
        t_right = self.visit(ctx.child)

        if t_left != t_right and not (t_left in ['Int', 'Uint'] and t_right in ['Int', 'Uint']):
            raise TypeError(ctx, f'Assignment requires the same types ({t_left} != {t_right})')

    def get_type(self, ctx, var):
        if var == 'lastReverted':
            return 'Bool'
        if var == 'a0':
            return 'Address'
        var = var.replace('app_tx_st.', '').replace('st.', '')
        var = var.replace('<tx>st.', '').replace('st.', '')
        if '.balance' in var:
            ag = var[:var.index('.balance')]
            for (v, t) in self.__globals:
                if ag == v and t == 'Address':
                    break
            else:
                if ag != 'xa':
                    raise TypeError(ctx, f'{ag} has not been defined in the contract or is not an address and used as such')
            var = var.replace(ag + '.', '')
        t_var = None
        for (v, t) in self.__globals:
            if var == v:
                t_var = t
                break
        else:
            if var + '_func' in self.__function_args_types:
                t_var = 'Method'
            elif var == 'this':
                t_var = 'Address'
            elif self.__prefix+'_'+var in self.__args_map:
                t_var = self.__args_map[self.__prefix+'_'+var]
            elif var == 'app_tx_st.balance' or var == '<tx>st.balance' or var == 'st.balance' or var == 'balance':
                t_var = 'Int'
            elif var == 'block.number':
                t_var = 'Int'
            if var == 'msg.value' or var == 'value':
                t_var = 'Int'
            if var == 'msg.sender' or var == 'sender' or var == 'xa':
                t_var = 'Address'
            if var in self.__vars:
                t_var = self.__vars[var]
        if not t_var:
            raise TypeError(ctx, f'{var} has not been defined in the contract')
        return t_var
        
    

    # Visit a parse tree produced by TxScriptParser#assignMapCmd.
    def visitAssignMapCmd(self, ctx:TxScriptParser.AssignMapCmdContext):
        left = ctx.var.text
        if 'balance' in left:
            t_left = ('MapAddr', 'Int')
        else:
            t_left = self.get_type(ctx, left)
        if t_left != ('MapAddr', 'Int'):
            raise TypeError(ctx, f'Map assignment requires a map ({t_left} is given)')

        t_index = self.visit(ctx.index)
        if t_index != 'Address':
            raise TypeError(ctx, f'Index of map has to be an address ({t_index} is given)')

        t_right = self.visit(ctx.child)
        if t_right != 'Int' and t_right != 'Uint':
            raise TypeError(ctx, f'Value to assign to map has to be an integer ({t_right} is given)')
        


    # Visit a parse tree produced by TxScriptParser#ifCmd.
    def visitIfCmd(self, ctx:TxScriptParser.IfCmdContext):
        t_cond = self.visit(ctx.condition)
        if t_cond != 'Bool':
            raise TypeError(ctx, f'If condition has to be a boolean ({t_cond} is given)')
        self.visit(ctx.ifcmd)
    

    # Visit a parse tree produced by TxScriptParser#ifelseCmd.
    def visitIfelseCmd(self, ctx:TxScriptParser.IfelseCmdContext):
        t_cond = self.visit(ctx.condition)
        if t_cond != 'Bool':
            raise TypeError(ctx, f'If condition has to be a boolean ({t_cond} is given)')
        self.visit(ctx.ifcmd)
        self.visit(ctx.elsecmd)


    # Visit a parse tree produced by TxScriptParser#seqCmd.
    def visitSeqCmd(self, ctx:TxScriptParser.SeqCmdContext):
        self.visit(ctx.seq1)
        self.visit(ctx.seq2)        


    # Visit a parse tree produced by TxScriptParser#groupExpr.
    def visitGroupExpr(self, ctx:TxScriptParser.GroupExprContext):
        return self.visit(ctx.child)


    # Visit a parse tree produced by TxScriptParser#greaterEqExpr.
    def visitGreaterEqExpr(self, ctx:TxScriptParser.GreaterEqExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if (t_left != 'Int' and t_left != 'Uint') or (t_right != 'Int' and t_right != 'Uint'):
            raise TypeError(ctx, f'>= requires both operands to be integers ({t_left} and {t_right} are given)')
        return 'Bool'
        


    # Visit a parse tree produced by TxScriptParser#lessExpr.
    def visitLessExpr(self, ctx:TxScriptParser.LessExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if (t_left != 'Int' and t_left != 'Uint') or (t_right != 'Int' and t_right != 'Uint'):
            raise TypeError(ctx, f'< requires both operands to be integers ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#neqExpr.
    def visitNeqExpr(self, ctx:TxScriptParser.NeqExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if t_left != t_right and (t_left not in ['Int', 'Uint', 'Address'] or t_right not in ['Int', 'Uint', 'Address']):
            raise TypeError(ctx, f'!= requires both operands to be same type ({t_left} and {t_right} are given)')
        return 'Bool'
        

    # Visit a parse tree produced by TxScriptParser#greaterExpr.
    def visitGreaterExpr(self, ctx:TxScriptParser.GreaterExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if (t_left != 'Int' and t_left != 'Uint') or (t_right != 'Int' and t_right != 'Uint'):
            raise TypeError(ctx, f'> requires both operands to be integers ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#eqExpr.
    def visitEqExpr(self, ctx:TxScriptParser.EqExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if t_left != t_right and (t_left not in ['Int', 'Uint', 'Address'] or t_right not in ['Int', 'Uint', 'Address']):
            raise TypeError(ctx, f'== requires both operands to be the same type ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#notExpr.
    def visitNotExpr(self, ctx:TxScriptParser.NotExprContext):
        t_child = self.visit(ctx.child)
        if t_child != 'Bool':
            raise TypeError(ctx, f'not requires a boolean operand ({t_child} is given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#sumSubExpr.
    def visitSumSubExpr(self, ctx:TxScriptParser.SumSubExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if (t_left != 'Int' and t_left != 'Uint') or (t_right != 'Int' and t_right != 'Uint'):
            raise TypeError(ctx, f'+/- requires both operands to be integers ({t_left} and {t_right} are given)')
        return 'Int'


    # Visit a parse tree produced by TxScriptParser#lessEqExpr.
    def visitLessEqExpr(self, ctx:TxScriptParser.LessEqExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if (t_left != 'Int' and t_left != 'Uint') or (t_right != 'Int' and t_right != 'Uint'):
            raise TypeError(ctx, f'<= requires both operands to be integers ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#multDivModExpr.
    def visitMultDivModExpr(self, ctx:TxScriptParser.MultDivModExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if (t_left != 'Int' and t_left != 'Uint') or (t_right != 'Int' and t_right != 'Uint'):
            raise TypeError(ctx, f'* and / require both operands to be integers ({t_left} and {t_right} are given)')
        return 'Int'


    # Visit a parse tree produced by TxScriptParser#andExpr.
    def visitAndExpr(self, ctx:TxScriptParser.AndExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if t_left != 'Bool' or t_right != 'Bool':
            raise TypeError(ctx, f'And operator requires both operands to be boolean ({t_left} and {t_right} are given)')
        return 'Bool'
    

    # Visit a parse tree produced by TxScriptParser#orExpr.
    def visitOrExpr(self, ctx:TxScriptParser.OrExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if t_left != 'Bool' or t_right != 'Bool':
            raise TypeError(ctx, f'Or operator requires both operands to be boolean ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#lengthExpr.
    def visitLengthExpr(self, ctx:TxScriptParser.LengthExprContext):
        t_child = self.visit(ctx.child)
        if t_child != 'Secret':
            raise TypeError(ctx, f'Length function requires a Secret operand ({t_child} is given)')
        return 'Int'
    

    # Visit a parse tree produced by TxScriptParser#sha256Expr.
    def visitSha256Expr(self, ctx:TxScriptParser.Sha256ExprContext):
        t_child = self.visit(ctx.child)
        if t_child != 'Secret':
            raise TypeError(ctx, f'Sha256 function requires a Secret operand ({t_child} is given)')
        return 'Hash'
    

        # Visit a parse tree produced by TxScriptParser#payableExpr.
    def visitPayableExpr(self, ctx:TxScriptParser.PayableExprContext):
        t_child = self.visit(ctx.child)
        if t_child != 'Address':
            raise TypeError(ctx, f'payable function requires an Address operand ({t_child} is given)')
        return 'Hash'
    

    # Visit a parse tree produced by TxScriptParser#qslf.
    def visitQslf(self, ctx:TxScriptParser.QslfContext):
        agent = ctx.ag.text + '_q'
        sender = ctx.sender.text
        if sender != 'sender' and sender != 'msg.sender' and sender != 'xa1':
            for (v, t) in self.__globals:
                if sender == v and t != 'Address':
                    raise TypeError(ctx, f'Participant operand in property requires to be an address ({t} is given)')
            if sender in self.__args_map and self.__args_map[sender] != 'Address':
                raise TypeError(ctx, f'Participant operand in property requires to be an address ({self.__args_map[sender]} is given)')
        
        t_condition = self.visit(ctx.where)
        if t_condition != 'Bool':
            raise TypeError(ctx, f'The property condition must be a boolean ({t_condition} is given)')

        t_body = self.visit(ctx.body)
        if t_condition != 'Bool':
            raise TypeError(ctx, f'The property body must be a boolean ({t_condition} is given)')


    # Visit a parse tree produced by TxScriptParser#numberConstant.
    def visitNumberConstant(self, ctx:TxScriptParser.NumberConstantContext):
        return 'Int'
    

    # Visit a parse tree produced by TxScriptParser#mapExpr.
    def visitMapExpr(self, ctx:TxScriptParser.MapExprContext):
        t_index = self.visit(ctx.index)
        if t_index != 'Address':
            raise TypeError(ctx, f'The index of a map must be an address ({t_index} is given)') 
        if 'balance' in ctx.mapVar.text:
            t_map = ('MapAddr', 'Int') 
        else:
            t_map = self.get_type(ctx, ctx.mapVar.text)
        if t_map != ('MapAddr', 'Int'):
            raise TypeError(ctx, f'{ctx.mapVar.text} is not a map but is accessed as one') 
        return 'Int'


    # Visit a parse tree produced by TxScriptParser#strConstant.
    def visitStrConstant(self, ctx:TxScriptParser.StrConstantContext):
        return self.get_type(ctx, ctx.v.text)


    # Visit a parse tree produced by TxScriptParser#trueConstant.
    def visitTrueConstant(self, ctx:TxScriptParser.TrueConstantContext):
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#falseConstant.
    def visitFalseConstant(self, ctx:TxScriptParser.FalseConstantContext):
        return 'Bool'
    
    # Visit a parse tree produced by TxScriptParser#rules.
    def visitRules(self, ctx:TxScriptParser.RulesContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#ruleExpr.
    def visitRuleExpr(self, ctx:TxScriptParser.RuleExprContext):
        self.__old = 0
        self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#andFormulaExpr.
    def visitAndFormulaExpr(self, ctx:TxScriptParser.AndFormulaExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if t_left != 'Bool' or t_right != 'Bool':
            raise TypeError(ctx, f'And operator requires both operands to be boolean ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#forallFormulaExpr.
    def visitForallFormulaExpr(self, ctx:TxScriptParser.ForallFormulaExprContext):
        for var in ctx.variables.varFormulaExpr():
            self.__vars[var.child.text] = self.visit(ctx.typenames)
        t = self.visit(ctx.child)
        if t != 'Bool':
            raise TypeError('Forall requires boolean operand')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#existsFormulaExpr.
    def visitExistsFormulaExpr(self, ctx:TxScriptParser.ExistsFormulaExprContext):
        for var in ctx.variables.varFormulaExpr():
            self.__vars[var.child.text] = self.visit(ctx.typenames)
        t = self.visit(ctx.child)
        if t != 'Bool':
            raise TypeError('Exists requires boolean operand')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#exprFormulaExpr.
    def visitExprFormulaExpr(self, ctx:TxScriptParser.ExprFormulaExprContext):
        return self.visit(ctx.expr)


    # Visit a parse tree produced by TxScriptParser#notFormulaExpr.
    def visitNotFormulaExpr(self, ctx:TxScriptParser.NotFormulaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TxScriptParser#complexExprFormulaExpr.
    def visitComplexExprFormulaExpr(self, ctx:TxScriptParser.ComplexExprFormulaExprContext):
        if self.visit(ctx.expr) != 'Address':
            raise TypeError(ctx, f'{ctx.expr} needs to have type address')
        if ctx.fname.text+'_func' not in self.__function_args_types and ctx.fname.text not in self.__vars:
            raise TypeError(ctx, f'{ctx.fname.text} does not exist')
        if self.visit(ctx.value) != 'Int' and self.visit(ctx.value) != 'Uint':
            raise TypeError(ctx, f'{ctx.value} needs to have integer type')
        if ctx.fname.text+'_func' in self.__function_args_types and self.__function_args_types[ctx.fname.text+'_func'] and not ctx.args.argFormulaExpr():
            raise TypeError(ctx, f'Function {ctx.fname.text} requires arguments, but none are given')
        if ctx.fname.text+'_func' in self.__vars and self.__vars[ctx.fname.text+'_func'] != 'Method':
            raise TypeError(ctx, f'{ctx.fname.text} is not a method')
        index = 0
        if ctx.fname.text+'_func' in self.__function_args_types:
            for arg in ctx.args.argFormulaExpr():
                if index >= len(self.__function_args_types[ctx.fname.text+'_func']):
                    raise TypeError(ctx, f'Function {ctx.fname.text} requires {len(self.__function_args_types[ctx.fname.text+"_func"])} arguments, but {index+1} are given')
                ty = self.visit(arg.child)
                if ty != self.__function_args_types[ctx.fname.text+'_func'][index] and ty != 'CallDataArgs' and not (ty in ['Int', 'Uint'] and self.__function_args_types[ctx.fname.text+'_func'][index] in ['Int', 'Uint']):
                    raise TypeError(ctx, f'argument {arg} should be {self.__function_args_types[ctx.fname.text+"_func"][index]}, as expected by function {ctx.fname.text+"_func"}, instead is {ty}')
                index += 1
        self.__old += 1
        return self.visit(ctx.child)


    # Visit a parse tree produced by TxScriptParser#orFormulaExpr.
    def visitOrFormulaExpr(self, ctx:TxScriptParser.OrFormulaExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if t_left != 'Bool' or t_right != 'Bool':
            raise TypeError(ctx, f'And operator requires both operands to be boolean ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#impliesFormulaExpr.
    def visitImpliesFormulaExpr(self, ctx:TxScriptParser.ImpliesFormulaExprContext):
        t_left = self.visit(ctx.left)
        t_right = self.visit(ctx.right)
        if t_left != 'Bool' or t_right != 'Bool':
            raise TypeError(ctx, f'And operator requires both operands to be boolean ({t_left} and {t_right} are given)')
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#groupFormulaExpr.
    def visitGroupFormulaExpr(self, ctx:TxScriptParser.GroupFormulaExprContext):
        return self.visit(ctx.child)


    # # Visit a parse tree produced by TxScriptParser#typeExpr.
    # def visitTypeExpr(self, ctx:TxScriptParser.TypeExprContext):
    #     return self.get_type(ctx, ctx.)


    # Visit a parse tree produced by TxScriptParser#varsFormulaExpr.
    def visitVarsFormulaExpr(self, ctx:TxScriptParser.VarsFormulaExprContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by TxScriptParser#typeAddress.
    def visitTypeAddress(self, ctx:TxScriptParser.TypeAddressContext):
        return 'Address'


    # Visit a parse tree produced by TxScriptParser#typeInt.
    def visitTypeInt(self, ctx:TxScriptParser.TypeIntContext):
        return 'Int'


    # Visit a parse tree produced by TxScriptParser#typeUint.
    def visitTypeUInt(self, ctx:TxScriptParser.TypeUIntContext):
        return 'Uint'


    # Visit a parse tree produced by TxScriptParser#typeBool.
    def visitTypeBool(self, ctx:TxScriptParser.TypeBoolContext):
        return 'Bool'


    # Visit a parse tree produced by TxScriptParser#typeMethod.
    def visitTypeMethod(self, ctx:TxScriptParser.TypeMethodContext):
        return 'Method'


    # Visit a parse tree produced by TxScriptParser#typeCallDataArgs.
    def visitTypeCallDataArgs(self, ctx:TxScriptParser.TypeCallDataArgsContext):
        return 'CallDataArgs'


    # # Visit a parse tree produced by TxScriptParser#varFormulaExpr.
    # def visitVarFormulaExpr(self, ctx:TxScriptParser.VarFormulaExprContext):
    #     return self.visitChildren(ctx)


    # # Visit a parse tree produced by TxScriptParser#argsFormulaExpr.
    # def visitArgsFormulaExpr(self, ctx:TxScriptParser.ArgsFormulaExprContext):
    #     types = []
    #     for arg in ctx.argFormulaExpr():
    #         types.append(self.visit(arg.child))
    #     return types


    # Visit a parse tree produced by TxScriptParser#argFormulaExpr.
    def visitArgFormulaExpr(self, ctx:TxScriptParser.ArgFormulaExprContext):
        return self.visit(ctx.child)
    
    # Visit a parse tree produced by TxScriptParser#oldExpr.
    def visitOldExpr(self, ctx:TxScriptParser.OldExprContext):
        if self.__old <= 0:
            raise TypeError(ctx, 'old(_) can only be used when nested inside a <> expression') 
        return self.visit(ctx.child)