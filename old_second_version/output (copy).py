
from z3 import *
import time

N = 2

f = Function('f', IntSort(), IntSort())
Time = Function('Time', IntSort(), IntSort())
Sender = Function('Sender', IntSort(), IntSort())
m = Int('m')
n = Int('n')
x = Function('x', IntSort(), IntSort())
ag00 = Function('ag00', IntSort(), IntSort())
ag10 = Function('ag10', IntSort(), IntSort())
tk0 = Function('tk0', IntSort(), IntSort())
xn0 = Function('xn0', IntSort(), IntSort())

s = Solver()

s.add(And(x(0) == 0, tk0(0) == 0))

for i in range(N):
    s.add(
  If(And(f(i)==0, Sender(i) == 0),
    And(
      Time(i)>=0, Time(i)<2, 
      And(
          ag00(i)>=xn0(i), 
          And(xn0(i)>0, 
              If(
                (tk0(i)+xn0(i))>=100, 
                And(
                    tk0(i+1)==(tk0(i)+xn0(i))-(tk0(i)+xn0(i)), 
                    ag00(i+1)==(ag00(i)-xn0(i))+(tk0(i)+xn0(i)), 
                    ag10(i+1)==ag10(i)),
                And(
                    ag00(i+1)==(ag00(i)-xn0(i)), 
                    ag10(i+1)==ag10(i),
                    tk0(i+1)==(tk0(i)+xn0(i))))))
    ), 
    If(And(f(i)==0, Sender(i) == 1),
      And(
        Time(i)>=0, Time(i)<2, 
        And(
            ag10(i)>=xn0(i), 
            And(
                xn0(i)>0, 
                If(
                    (tk0(i)+xn0(i))>=100, 
                    And(
                        tk0(i+1)==(tk0(i)+xn0(i))-(tk0(i)+xn0(i)),
                        ag00(i+1)==ag00(i),
                        ag10(i+1)==(ag10(i)-xn0(i))+(tk0(i)+xn0(i))
                    ), 
                    And(
                        ag10(i+1)==(ag10(i)-xn0(i)),
                        ag00(i+1)==ag00(i),
                        tk0(i+1)==(tk0(i)+xn0(i))
                    )
                )
            )
        )
      ),
      And(tk0(i+1)==tk0(i),ag00(i+1)==ag00(i),ag10(i+1)==ag10(i))
      )))

timeStart = time.time()

queries = [
    And(
        ag10(0)==1,
        ag00(0)==99,
        Exists(n,And(n<=2, n>=0, ag10(n)==100))
    )
	# ForAll(n,Implies(ag00(n)>0,ForAll(m,Implies(m>n,ag00(m)>0))))
]

for q in queries:
    print(str(q) + " : ", end = '')
    if s.check(q)==sat:
        print(" sat")
        print(s.model())
    else:
        print(" unsat")

timeTot = time.time() - timeStart
print("Solving time: " + str(timeTot) + "s")
        
