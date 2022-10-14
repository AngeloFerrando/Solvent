grammar TxScript;

contractExpr : 'contract' name=LABEL '{' 'resources_bound' ':' resBound=NUMBER 'agents_bound' ':' agentBound=NUMBER 'tokens_bound' ':' tokenBound=NUMBER  child=proceduresExpr '}';

proceduresExpr : (child=procedureExpr)+;

procedureExpr : '@pre' preconditions=preconditionsExpr LABEL'(' pArgs=pArgsExpr ')' '{' body=bodyExpr '}';

preconditionsExpr : (child=expression)+;

expression :
 child='null'                                               # null
 | child=constantExpr                                       # constant
 | child=LABEL                                              # variable
 | '#' child=expression                                     # Wallet
 | left=expression op=('*' | '/') right=expression          # MultDivEq
 | left=expression op=('+' | '-') right=expression          # SumSubEq
 | left=expression ('==') right=expression                  # Eq
 | left=expression ('!=') right=expression                  # NEq
 | left=expression ('<') right=expression                   # Less
 | left=expression ('>') right=expression                   # Greater
 | left=expression ('<=') right=expression                  # LessEq
 | left=expression ('>=') right=expression                  # GreaterEq
;

pArgsExpr :
 variable=LABEL                                             # variableArg
 | agent=LABEL '?' data=LABEL ':' token=LABEL               # inputToken
;

bodyExpr :
 child='skip'                                                # skipBody
 | variable=LABEL ':=' child=expression                      # assignmentBody
 | agent=expression '!' data=expression ':' token=expression # outputToken
 | left=bodyExpr ';' right=bodyExpr                          # sequence
 | 'if' condition=expression 'then' first=bodyExpr 'else' second=bodyExpr # ifstatement
;

constantExpr :
 v=NUMBER                                                   # numberConstant
 | v= LABELUPPER                                            # agentOrTokenConstant
;


LABEL : [_a-zA-Z][_a-zA-Z0-9]*;
LABELUPPER : [A-Z][_a-zA-Z0-9]*;

NUMBER : ('-')? DIGIT | ('-')? (DIGIT_NOT_ZERO DIGIT+);
REAL : NUMBER '.' (DIGIT+) | NUMBER '.' (DIGIT+);

WS: [ \r\n\t]+ -> channel (HIDDEN);
fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');
