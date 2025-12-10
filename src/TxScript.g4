grammar TxScript;

contractExpr : 'contract' name=UPPER '{' decl=declsExpr '}' properties=rules;

propertiesExpr : (propertyExpr)*;

propertyExpr : 'property' name=LABEL '{' phi=qslf '}';

declsExpr : (declExpr)+;
declExpr : 
child=fieldExpr                                                                                     # fieldDecl
    // | 'immutable' child=fieldExpr                                                                   # constFieldDecl
    | 'constraint' name=LABEL '(' args=argsExpr  ')' '{' cmds=cmdExpr '}'                           # constrDecl
    | 'function' name=LABEL '(' args=argsExpr ')' 'payable' ('public')? ('external')? '{' cmds=cmdExpr '}' # payableFunDecl
    | 'function' name=LABEL '(' args=argsExpr ')' ('public')? ('external')? '{' cmds=cmdExpr '}'    # nonPayableFunDecl
    | 'constructor' '(' args=argsExpr ')' 'payable'  '{' cmds=cmdExpr '}'                           # payableConstructorDecl
    | 'constructor' '(' args=argsExpr ')' '{' cmds=cmdExpr '}'                                      # nonPayableConstructorDecl
;

fieldExpr :
'int' (const='immutable')? var=LABEL (';')?                                                         # intDecl
    | 'uint' (const='immutable')? var=LABEL (';')?                                                  # uintDecl
    | 'bool' (const='immutable')? var=LABEL (';')?                                                  # boolDecl
    | 'string' (const='immutable')? var=LABEL (';')?                                                # strDecl
    | 'address' (const='immutable')? var=LABEL (';')?                                               # addrDecl
    | 'hash' (const='immutable')? var=LABEL (';')?                                                  # hashDecl
    | 'secret' (const='immutable')? var=LABEL (';')?                                                # secretDecl
    | 'mapping (address => int)' (const='immutable')? var=LABEL (';')?                              # mapAddrDeclInt 
;

argsExpr : (argExpr)*;
argExpr : 
    ty=('int'|'uint'|'bool'|'address'|'string'|'hash'|'secret') var=LABEL (',')?                    # arg
    | ty='mapping (address => int)' var=LABEL (',')?                                                # argMap
;

cmdExpr :
    'skip'                                                              # skipCmd
    | 'require' '(' child=expression ')'                                # requireCmd
    | 'if' '(' condition=expression ')' '{' ifcmd=cmdExpr '}' 'else' '{' elsecmd=cmdExpr '}'    # ifelseCmd
    | 'if' '(' condition=expression ')' '{' ifcmd=cmdExpr '}'           # ifCmd
    | var=LABEL '[' index=expression ']' '=' child=expression           # assignMapCmd
    | var=LABEL '=' child=expression                                    # assignCmd
    | sender=expression '!' amount=expression                                # sendCmd
    | <assoc=right> seq1=cmdExpr ';' seq2=cmdExpr                       # seqCmd
    | '(' cmdExpr ')'                                                   # groupCmd
;

expression :
 child=constantExpr                                                     # constExpr
 | mapVar=LABEL '[' index=expression ']'                                # mapExpr
//  | child=LABEL                                                          # variableExpr
//  | '#' child=expression                                                 # walletExpr
 | 'sha256' '(' child=expression ')'                                    # sha256Expr
 | ('length' | 'len') '(' child=expression ')'                          # lengthExpr
 | 'payable' '(' child=expression ')'                                   # payableExpr
 | left=expression op=('*' | '/' | '%') right=expression                # multDivModExpr
 | left=expression op=('+' | '-') right=expression                      # sumSubExpr
 | left=expression ('==') right=expression                              # eqExpr
 | left=expression ('!=') right=expression                              # neqExpr
 | left=expression ('<') right=expression                               # lessExpr
 | left=expression ('>') right=expression                               # greaterExpr
 | left=expression ('<=') right=expression                              # lessEqExpr
 | left=expression ('>=') right=expression                              # greaterEqExpr
 | ('not'|'!') child=expression                                         # notExpr
 | left=expression ('and' | '&&') right=expression                      # andExpr
 | left=expression ('or' | '||') right=expression                       # orExpr
 | 'old' '(' child=expression ')'                                       # oldExpr
 | '(' child=expression ')'                                             # groupExpr
;

qslf : 
  'Forall' ag=LABEL '[' where=expression '->' 'Exists' tx=LABEL '[' nTrans=NUMBER ',' sender=LABEL ']' '[' body=expression ']' ']'
;

rules : (ruleExpr)*;

ruleExpr :
  'rule' name=UPPER '{' phi=formulaExpr '}'
;

formulaExpr :
  expr=expression                                                       # exprFormulaExpr
  | '!' child=formulaExpr                                               # notFormulaExpr
  | left=formulaExpr ('and' | '&&') right=formulaExpr                   # andFormulaExpr
  | left=formulaExpr ('or' | '||') right=formulaExpr                    # orFormulaExpr
  | left=formulaExpr ('implies' | '->') right=formulaExpr               # impliesFormulaExpr
  | 'forall' variables=varsFormulaExpr ':' typenames=typeExpr '.' child=formulaExpr      # forallFormulaExpr
  | 'exists' variables=varsFormulaExpr ':' typenames=typeExpr '.' child=formulaExpr      # existsFormulaExpr
  | '<<' expr=expression ':' cname=UPPER '.' fname=LABEL '(' args=argsFormulaExpr ')' '$' value=expression '>>' child=formulaExpr     # complexExprFormulaExpr
  | '(' child=formulaExpr ')'                                           # groupFormulaExpr
;

typeExpr : 
  'address'           # typeAddress
  | 'int'             # typeInt
  | 'uint'            # typeUInt
  | 'bool'            # typeBool
  | 'method'          # typeMethod
  | 'calldataargs'    # typeCallDataArgs
;

varsFormulaExpr : (varFormulaExpr)*;
varFormulaExpr : 
    child=LABEL (',')?                                                  
;

argsFormulaExpr : (argFormulaExpr)*;
argFormulaExpr : 
    child=expression (',')?                                             
;

constantExpr :
  v=NUMBER                                                              # numberConstant
  | v=(LABEL | UPPER)                                                   # strConstant
  | v=('true'|'True')                                                   # trueConstant
  | v=('false'|'False')                                                 # falseConstant
;


LABEL : [_a-z.][_a-zA-Z0-9.]*;

UPPER : [A-Z.][_a-zA-Z0-9]*;

NUMBER : ('-')? DIGIT | ('-')? (DIGIT_NOT_ZERO DIGIT+);
REAL : NUMBER '.' (DIGIT+) | NUMBER '.' (DIGIT+);

TYPE : 'int' | 'uint' | 'float' | 'bool' | 'address' | 'hash' | 'secret';

WS: [ \r\n\t]+ -> channel (HIDDEN);
fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');

COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);