grammar TxScript;

contractExpr : 'contract' name=LABELUPPER '{' decl=declsExpr '}' properties=propertiesExpr;

propertiesExpr : (propertyExpr)*;

propertyExpr : 'property' name=LABEL '{' phi=qslf '}';

declsExpr : (declExpr)+;
declExpr : 
'int' var=LABEL                                                                                     # intDecl
    | 'bool' var=LABEL                                                                              # boolDecl
    | 'string' var=LABEL                                                                            # strDecl
    | 'address' var=LABEL                                                                           # addrDecl
    | '(' 'address' '->' 'int' ')' var=LABEL                                                        # mapAddrDeclInt 
    | 'constraint' name=LABEL '(' args=argsExpr  ')' '{' cmds=cmdExpr '}'                           # constrDecl
    | 'function' name=LABEL '(' args=argsExpr ')' 'payable' '{' cmds=cmdExpr '}'                    # payableFunDecl
    | 'function' name=LABEL '(' args=argsExpr ')' '{' cmds=cmdExpr '}'                              # nonPayableFunDecl
    | 'constructor' '(' args=argsExpr ')' 'payable'  '{' cmds=cmdExpr '}'                           # payableConstructorDecl
    | 'constructor' '(' args=argsExpr ')' '{' cmds=cmdExpr '}'                                      # nonPayableConstructorDecl
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
 | left=expression ('or' | '||') right=expression                       # orExpr
 | 'not' child=expression                                               # notExpr
 | '(' child=expression ')'                                             # groupExpr
;

qslf : 
  'Forall' ag=LABEL '[' where=expression '->' 'Exists' tx=LABEL '[' nTrans=NUMBER ',' sender=LABEL ']' '[' body=expression ']' ']'
;
// canWithdrawExpr : 
//   'can_withdraw' '('ag=constantExpr ',' body=expression ')'             # baseWithdrawExpr
//   | left=canWithdrawExpr ('and' | '&&') right=canWithdrawExpr           # andWithdrawExpr
//   | left=canWithdrawExpr ('or' | '||') right=canWithdrawExpr            # orWithdrawExpr
// ;

// qslf :
//  child=constantExpr                                                     # qslfAtomExpr
//  | functor=LABEL '(' args=qslfArgsExpr ')'                              # qslfFunctionExpr
//  | ('E' | 'Exists') 'a' var=NUMBER child=qslf                           # qslfExistsAgentExpr
//  | ('E' | 'Exists') 's' var=NUMBER child=qslf                           # qslfExistsStrategyExpr
//  | ('A' | 'Forall') 'a' var=NUMBER child=qslf                           # qslfForallAgentExpr
//  | ('A' | 'Forall') 's' var=NUMBER child=qslf                           # qslfForallStrategyExpr
//  | '(' 'a' var=NUMBER ',' 's' var=NUMBER ')' child=qslf                 # qslfBindingExpr
//  | ('X' | 'Next') child=qslf                                            # qslfNextExpr
//  | ('G' | 'Globally') child=qslf                                        # qslfGloballyExpr
//  | ('F' | 'Eventually') child=qslf                                      # qslfEventuallyExpr
//  | left=qslf ('and' | '&&') right=qslf                                  # qslfAndExpr
//  | left=qslf ('or' | '||') right=qslf                                   # qslfOrExpr
//  | left=qslf ('implies' | '->') right=qslf                              # qslfImpliesExpr
//  | left=expression op=('*' | '/') right=expression                      # qslfMultDivEqExpr
//  | left=expression op=('+' | '-') right=expression                      # qslfSumSubEqExpr
//  | left=expression ('==') right=expression                              # qslfEqExpr
//  | left=expression ('!=') right=expression                              # qslfNeqExpr
//  | left=expression ('<') right=expression                               # qslfLessExpr
//  | left=expression ('>') right=expression                               # qslfGreaterExpr
//  | left=expression ('<=') right=expression                              # qslfLessEqExpr
//  | left=expression ('>=') right=expression                              # qslfGreaterEqExpr
//  | 'not' child=expression                                               # qslfNotExpr
//  | '(' child=expression ')'                                             # qslfGroupExpr
// ;

// qslfArgsExpr : 
//   child=qslf                                                            # qslfSingleArgExpr
//   | left=qslf ',' right=qslf                                            # qslfMultiArgExpr
// ;

constantExpr :
  v=NUMBER                                                              # numberConstant
  | v=LABEL                                                             # strConstant
  | v=('true'|'True')                                                   # trueConstant
  | v=('false'|'False')                                                 # falseConstant
;


LABEL : [_a-z.][_a-zA-Z0-9.]*('['[_a-z.][_a-zA-Z0-9.]*']')?;
LABELUPPER : [_a-zA-Z][_a-zA-Z0-9]*;

NUMBER : ('-')? DIGIT | ('-')? (DIGIT_NOT_ZERO DIGIT+);
REAL : NUMBER '.' (DIGIT+) | NUMBER '.' (DIGIT+);

TYPE : 'int' | 'float' | 'bool' | 'address';

WS: [ \r\n\t]+ -> channel (HIDDEN);
fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');

COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);