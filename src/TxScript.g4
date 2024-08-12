grammar TxScript;

contractExpr : 'contract' name=LABELUPPER '{' decl=declsExpr '}' properties=propertiesExpr;

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
    | 'bool' (const='immutable')? var=LABEL (';')?                                                  # boolDecl
    | 'string' (const='immutable')? var=LABEL (';')?                                                # strDecl
    | 'address' (const='immutable')? var=LABEL (';')?                                               # addrDecl
    | 'hash' (const='immutable')? var=LABEL (';')?                                                  # hashDecl
    | 'secret' (const='immutable')? var=LABEL (';')?                                                # secretDecl
    | 'mapping (address => int)' (const='immutable')? var=LABEL (';')?                              # mapAddrDeclInt 
;

argsExpr : (argExpr)*;
argExpr : 
    ty=('int'|'bool'|'address'|'string'|'hash'|'secret') var=LABEL (',')?                           # arg
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


LABEL : [_a-z.][_a-zA-Z0-9.]*;
// LABELP : [_a-z.][_a-zA-Z0-9.]*('['[_a-z.][_a-zA-Z0-9.]*']')?;
LABELUPPER : [_a-zA-Z][_a-zA-Z0-9]*;

NUMBER : ('-')? DIGIT | ('-')? (DIGIT_NOT_ZERO DIGIT+);
REAL : NUMBER '.' (DIGIT+) | NUMBER '.' (DIGIT+);

TYPE : 'int' | 'float' | 'bool' | 'address' | 'hash' | 'secret';

WS: [ \r\n\t]+ -> channel (HIDDEN);
fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');

COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);