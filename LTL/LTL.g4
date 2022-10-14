grammar LTL;

ltlExpr :
    ('!' | 'not') child=ltlExpr                                  # Negation
     // temporal operators
     | ('next' | 'X') child=ltlExpr                                    # Next
     | ('eventually' | 'F') child=ltlExpr                              # Eventually
     | ('always' | 'G') child=ltlExpr                                  # Always
     | left=ltlExpr ('until' | 'U') right=ltlExpr                      # Until
     | left=ltlExpr ('release' | 'R') right=ltlExpr                    # Release
     // data operators
     | left=ltlExpr op=('*' | '/') right=ltlExpr                       # MultDivEq
     | left=ltlExpr op=('+' | '-') right=ltlExpr                       # SumSubEq
     | left=ltlExpr ('==') right=ltlExpr                               # Eq
     | left=ltlExpr ('!=') right=ltlExpr                               # NEq
     | left=ltlExpr ('<') right=ltlExpr                                # Less
     | left=ltlExpr ('>') right=ltlExpr                                # Greater
     | left=ltlExpr ('<=') right=ltlExpr                               # LessEq
     | left=ltlExpr ('>=') right=ltlExpr                               # GreaterEq
     // boolean operators
     | left=ltlExpr ('&&' | 'and') right=ltlExpr                       # Conjunction
     | left=ltlExpr ('||' | 'or') right=ltlExpr                        # Disjunction
     | left=ltlExpr ('->' | 'implies') right=ltlExpr                   # Implies
     | '(' ltlExpr ')'                                                 # Grouping
     | child=atomExpr                                                  # Evaluation
     ;

atomExpr : ATOM;

ATOM : [_a-z][_a-z0-9]*;

WS        : [ \t\r\n\u000C]+ -> skip;
