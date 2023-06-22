grammar TxScript;

contractExpr : 'contract' name=LABELUPPER '{' 'resources_bound' ':' resBound=NUMBER 'agents_bound' ':' agentBound=NUMBER 'tokens_bound' ':' tokenBound=NUMBER ('global' ':' gVars=globalVarsExpr)?  child=proceduresExpr '}' phis=firstOrderFormulasExpr;

globalVarsExpr : (globalVarExpr)+;

globalVarExpr : ty=('int'|'float'|'bool') name=LABEL '=' val=(NUMBER|REAL|'true'|'false');

firstOrderFormulasExpr : ('query' '{' child=firstOrderFormulaExpr '}')*;

firstOrderFormulaExpr : 
  child=(LABEL|NUMBER)                                                         # atomFormula
  | child=LABEL ':' n=(LABEL|NUMBER)                                           # atomFormulaN
  | '{' '#' j=(LABEL|NUMBER) '}' n=(LABEL|NUMBER)                              # token0jn
  | '{' '#' i=(LABEL|NUMBER) ':' j=(LABEL|NUMBER) '}' n=(LABEL|NUMBER)         # tokenijn
  | '{' x=LABEL '}' n=(LABEL|NUMBER)                                           # gVarn
  | child=LABEL '(' (agent=LABEL ':' amount=LABEL '?' token=LABEL )? ')'       # functionFormula
  | ('not'|'!') child=firstOrderFormulaExpr                                    # notFormula
  | left=firstOrderFormulaExpr op=('*' | '/') right=firstOrderFormulaExpr      # MultDivEqFormula
  | left=firstOrderFormulaExpr op=('+' | '-') right=firstOrderFormulaExpr      # SumSubEqFormula
  | left=firstOrderFormulaExpr ('==') right=firstOrderFormulaExpr              # EqFormula
  | left=firstOrderFormulaExpr ('!=') right=firstOrderFormulaExpr              # NEqFormula
  | left=firstOrderFormulaExpr ('<') right=firstOrderFormulaExpr               # LessFormula
  | left=firstOrderFormulaExpr ('>') right=firstOrderFormulaExpr               # GreaterFormula
  | left=firstOrderFormulaExpr ('<=') right=firstOrderFormulaExpr              # LessEqFormula
  | left=firstOrderFormulaExpr ('>=') right=firstOrderFormulaExpr              # GreaterEqFormula
  | left=firstOrderFormulaExpr ('and'|'&') right=firstOrderFormulaExpr         # andFormula
  | left=firstOrderFormulaExpr ('or'|'|') right=firstOrderFormulaExpr          # orFormula
  | left=firstOrderFormulaExpr ('implies'|'->') right=firstOrderFormulaExpr    # impliesFormula
  | 'Exists' var=LABEL '.' child=firstOrderFormulaExpr                         # existsFormula
  | 'Forall' var=LABEL '.' child=firstOrderFormulaExpr                         # forallFormula
  | 'sum' '(' child=firstOrderFormulaExpr ',' var=LABEL 'in' '[' varMin=NUMBER ',' varMax=NUMBER ']' ')'  #sumFormula
  | '(' child=firstOrderFormulaExpr ')'                                        # groupFormula;

proceduresExpr : (child=procedureExpr)+;

procedureExpr : '@time' '[' start=(NUMBER|'_') ',' end=(NUMBER|'_') ']' '@pre' preconditions=preconditionsExpr action=LABEL'(' pArgs=pArgsExprs ')' '{' body=bodyExpr '}';

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

pArgsExprs : (pArgsExpr)+;

pArgsExpr :
 variable=LABEL                                             # variableArg
 | agent=LABEL '?' data=LABEL ':' token=LABEL               # inputToken
;

bodyExpr :
 child='skip'                                                # skipBody
 | variable=LABELUPPER ':=' child=expression                 # assignmentBody
 | agent=expression '!' data=expression ':' token=expression # outputToken
 | left=bodyExpr ';' right=bodyExpr                          # sequence
 | 'if' condition=expression 'then' first=bodyExpr 'else' second=bodyExpr # ifstatement
;

constantExpr :
 v=NUMBER                                                   # numberConstant
 | v= LABELUPPER                                            # agentOrTokenConstant
;


LABEL : [_a-z][_a-zA-Z0-9]*;
LABELUPPER : [_a-zA-Z][_a-zA-Z0-9]*;

NUMBER : ('-')? DIGIT | ('-')? (DIGIT_NOT_ZERO DIGIT+);
REAL : NUMBER '.' (DIGIT+) | NUMBER '.' (DIGIT+);

TYPE : 'int' | 'float' | 'bool';

WS: [ \r\n\t]+ -> channel (HIDDEN);
fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');

COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);