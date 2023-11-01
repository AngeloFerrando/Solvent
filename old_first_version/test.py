import time

from pysmt.shortcuts import *
from pysmt.typing import INT, ArrayType
from pysmt.logics import *

N = 30

f = Symbol('f', ArrayType(INT, INT))
Time = Symbol('time', ArrayType(INT, INT))
Sender = Symbol('sender', ArrayType(INT, INT))
m = Symbol('m', INT)
n = Symbol('n', INT)
x = Symbol('x', ArrayType(INT, INT))
ag10 = Symbol('ag10', ArrayType(INT, INT))
ag20 = Symbol('ag20', ArrayType(INT, INT))
tk0 = Symbol('tk0', ArrayType(INT, INT))
xn0 = Symbol('xn0', ArrayType(INT, INT))

values = [ag10, ag20, tk0]

contract = And(Equals(Select(x, Int(0)), Int(0)), Equals(Select(tk0, Int(0)), Int(0)))

for i in range(N):
    contract = And(contract, 
      Implies(
        And(Equals(Select(f, Int(i)), Int(0)), Equals(Select(Sender, Int(i)), Int(1))), 
        And(
          GE(Select(Time, Int(i)), Int(0)), 
          LT(Select(Time, Int(i)), Int(2)),
          GE(Select(ag10, Int(i)), Select(xn0, Int(i))), 
          GT(Select(xn0, Int(i)), Int(0)), 
          Implies(
            GE(Plus(Select(tk0, Int(i)), Select(xn0, Int(i))), Int(100)), 
            And(
              Equals(Select(tk0, Int(i+1)), Minus(Plus(Select(tk0, Int(i)), Select(xn0, Int(i))), Plus(Select(tk0, Int(i)), Select(xn0, Int(i))))), 
              Equals(Select(ag10, Int(i+1)), Plus(Minus(Select(ag10, Int(i)), Select(xn0, Int(i))), Plus(Select(tk0, Int(i)), Select(xn0, Int(i)))))
            )
          ),
          Implies(
            Not(GE(Plus(Select(tk0, Int(i)), Select(xn0, Int(i))), Int(100))),
            And(
              Equals(Select(ag10, Int(i+1)), Minus(Select(ag10, Int(i)), Select(xn0, Int(i)))), 
              Equals(Select(tk0, Int(i+1)), Plus(Select(tk0, Int(i)), Select(xn0, Int(i))))
            )
          ), 
          Equals(Select(ag20, Int(i+1)), Select(ag20, Int(i))), 
          Equals(Select(x, Int(i+1)), Select(x, Int(i)))
        )
      ),
      Implies(
        And(Not(And(Equals(Select(f, Int(i)), Int(0)), Equals(Select(Sender, Int(i)), Int(1)))), Equals(Select(f, Int(i)), Int(0)), Equals(Select(Sender, Int(i)), Int(2))), 
        And(
          GE(Select(Time, Int(i)), Int(0)), 
          LT(Select(Time, Int(i)), Int(2)),
          GE(Select(ag20, Int(i)), Select(xn0, Int(i))), 
          GT(Select(xn0, Int(i)), Int(0)), 
          Implies(
            GE(Plus(Select(tk0, Int(i)), Select(xn0, Int(i))), Int(100)), 
            And(
              Equals(Select(tk0, Int(i+1)), Minus(Plus(Select(tk0, Int(i)), Select(xn0, Int(i))), Plus(Select(tk0, Int(i)), Select(xn0, Int(i))))), 
              Equals(Select(ag20, Int(i+1)), Plus(Minus(Select(ag20, Int(i)), Select(xn0, Int(i))), Plus(Select(tk0, Int(i)), Select(xn0, Int(i)))))
            )
          ),
          Implies(
            Not(GE(Plus(Select(tk0, Int(i)), Select(xn0, Int(i))), Int(100))),
            And(
              Equals(Select(ag20, Int(i+1)), Minus(Select(ag20, Int(i)), Select(xn0, Int(i)))), 
              Equals(Select(tk0, Int(i+1)), Plus(Select(tk0, Int(i)), Select(xn0, Int(i))))
            )
          ),
          Equals(Select(ag10, Int(i+1)), Select(ag10, Int(i))), 
          Equals(Select(x, Int(i+1)), Select(x, Int(i)))
        )
      ),
      Implies(
        Not(And(Not(And(Equals(Select(f, Int(i)), Int(0)), Equals(Select(Sender, Int(i)), Int(1)))), Equals(Select(f, Int(i)), Int(0)), Equals(Select(Sender, Int(i)), Int(2))), ),
        And(
          Equals(Select(ag10, Int(i+1)), Select(ag10, Int(i))), 
          Equals(Select(ag20, Int(i+1)), Select(ag20, Int(i))), 
          Equals(Select(tk0, Int(i+1)), Select(tk0, Int(i))), 
          Equals(Select(x, Int(i+1)), Select(x, Int(i)))
        )
      )
    )
      
queries = [
    # ForAll(
    #   [n],
    #   Implies(
    #     And(GE(n, Int(0)),LE(n, Int(5)),GT(Select(tk0, n), Int(0))),
    #     Exists(
    #       [m],
    #       And(GT(m, n), LE(m, Int(10)), Equals(Select(tk0, m), Int(0)))
    #     )
    #   )
    # )
	  # And(
    #   Equals(Select(tk0, Int(0)), Int(98)), 
    #   Equals(Select(ag10, Int(0)), Int(1)),
    #   Equals(Select(ag20, Int(0)), Int(1)),
    #   Exists([n],And(GE(n, Int(0)), LE(n, Int(5)), Equals(Select(ag20, n), Int(100))))
    # )
    # ForAll(
    #   [n],
    #   Equals(Plus(Select(ag10, Int(0)), Select(ag20, Int(0))), Plus(Select(ag10, n), Select(ag20, n)))
    # )
    And(
      Equals(Select(ag10, Int(0)), Int(1)),
      Equals(Select(ag20, Int(0)), Int(0)),
      Equals(Select(tk0, Int(0)), Int(100)),
      ForAll(
        [n],
        Equals(Select(ag10, n), Int(101))
      )
    )
]

# queries = [Equals(Plus(Select(ag10, Int(0)), Select(ag20, Int(0))), Plus(Select(ag10, Int(n)), Select(ag20, Int(n)))) for n in range(0, N+1)]

# print('Serialization of the formula:')
# print(contract)

timeStart = time.time()
# solvers_set = ["z3", "msat"]

for q in queries:
  print(q)
  with Solver(name='z3') as solver:
    solver.add_assertion(contract)
    solver.add_assertion(q)
    if solver.solve():
      print('SAT')
      # for v in values:
      #   print('%s = %s' %(v, solver.get_value(v)))
    else:
      print('No solution found')
  # res = is_sat(And(contract, q), portfolio=solvers_set)
  # print(res)


timeTot = time.time() - timeStart
print("Solving time: " + str(timeTot) + "s")




# hello = [Symbol(s, INT) for s in 'hello']
# world = [Symbol(s, INT) for s in 'world']
# letters = set(hello+world)
# domains = And([And(GE(l, Int(1)),
#                    LT(l, Int(10))) for l in letters])

# sum_hello = Plus(hello) # n-ary operators can take lists
# sum_world = Plus(world) # as arguments
# problem = And(Equals(sum_hello, sum_world),
#               Equals(sum_hello, Int(25)))
# problem = And(problem, Equals(hello[0], Int(2)))
# formula = And(domains, problem)