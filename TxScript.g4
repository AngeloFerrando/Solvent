grammar TxScript;


contractExpr : 'contract' name=LABELUPPER '{' decl=declsExpr '}';

declsExpr : (declExpr)+;
declExpr : 
'int' var=LABEL                                                                      # intDecl
    | 'bool' var=LABEL                                                               # boolDecl
    | 'string' var=LABEL                                                             # strDecl
    | 'address' var=LABEL                                                            # addrDecl
    | '(' 'address' '->' 'int' ')' var=LABEL                                         # mapAddrDeclInt 
    | 'constraint' name=LABEL '(' args=argsExpr  ')' '{' cmds=cmdExpr '}'            # constrDecl
    | 'function' name=LABEL '(' args=argsExpr ')' 'payable' '{' cmds=cmdExpr '}'     # payableFunDecl
    | 'function' name=LABEL '(' args=argsExpr ')' '{' cmds=cmdExpr '}'               # nonPayableFunDecl
    | 'constructor' '(' args=argsExpr ')' '{' cmds=cmdExpr '}'                       # constructorDecl
;

argsExpr : (argExpr)*;
argExpr : 
    var=LABEL                                                           # arg
;

cmdExpr :
    'skip'                                                              # skipCmd
    | 'require' '(' child=expression ')'                                # requireCmd
    | 'if' '(' condition=expression ')' '{' ifcmd=cmdExpr '}' 'else' '{' elsecmd=cmdExpr '}'    # ifelseCmd
    | 'if' '(' condition=expression ')' '{' ifcmd=cmdExpr '}'           # ifCmd
    | var=LABEL '=' child=expression                                    # assignCmd
    | var=LABEL '[' index=expression ']' '=' child=expression           # assignMapCmd
    | sender=LABEL '!' amount=expression                                # sendCmd
    | <assoc=right> seq1=cmdExpr ';' seq2=cmdExpr                       # seqCmd
    | '(' cmdExpr ')'                                                   # groupCmd
;

expression :
 child=constantExpr                                                     # constExpr
 | mapVar=LABEL '[' index=expression ']'                                # mapExpr
//  | child=LABEL                                                          # variableExpr
//  | '#' child=expression                                                 # walletExpr
 | left=expression op=('*' | '/') right=expression                      # multDivEqExpr
 | left=expression op=('+' | '-') right=expression                      # sumSubEqExpr
 | left=expression ('==') right=expression                              # eqExpr
 | left=expression ('!=') right=expression                              # neqExpr
 | left=expression ('<') right=expression                               # lessExpr
 | left=expression ('>') right=expression                               # greaterExpr
 | left=expression ('<=') right=expression                              # lessEqExpr
 | left=expression ('>=') right=expression                              # greaterEqExpr
 | left=expression ('and' | '&&') right=expression                      # andExpr
 | 'not' child=expression                                               # notExpr
 | '(' child=expression ')'                                             # groupExpr
;

constantExpr :
  v=NUMBER                                                              # numberConstant
  | v=LABEL                                                             # strConstant
  | v=('true'|'True')                                                   # trueConstant
  | v=('false'|'False')                                                 # falseConstant
;


LABEL : [_a-z.][_a-zA-Z0-9.]*;
LABELUPPER : [_a-zA-Z][_a-zA-Z0-9]*;

NUMBER : ('-')? DIGIT | ('-')? (DIGIT_NOT_ZERO DIGIT+);
REAL : NUMBER '.' (DIGIT+) | NUMBER '.' (DIGIT+);

TYPE : 'int' | 'float' | 'bool' | 'address';

WS: [ \r\n\t]+ -> channel (HIDDEN);
fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');

COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);