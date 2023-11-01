
from z3 import *
import time

N = 10

f = Function('f', IntSort(), IntSort())
Time = Function('Time', IntSort(), IntSort())
Sender = Function('Sender', IntSort(), IntSort())
balances = Function('balances', IntSort(), RealSort())
ag10 = Function('ag10', IntSort(), IntSort())
ag20 = Function('ag20', IntSort(), IntSort())
tk0 = Function('tk0', IntSort(), IntSort())
balances0 = Function('balances0', IntSort(), IntSort())
value1 = Function('value1', IntSort(), IntSort())
amount2 = Function('amount2', IntSort(), IntSort())

s = Solver()

s.add(And(tk0(0)==0))

for i in range(N):
    s.add(
        If(
            And(
                f(i)==1, Sender(i)==1), 
                And(
                    And(
                        balances0(i)(ag10(i))==balances0(i)(ag10(i))-amount2(i), 
                        And(
                            tk0(i)>=amount2(i), 
                            ag10(i+1)==ag10(i) + amount2(i), 
                            tk0(i+1)==tk0(i) -amount2(i)
                        )
                    ), 
                    ag20(i+1)==ag20(i), 
                    balances(i+1)==balances(i)), 
                    If(And(f(i)==1, Sender(i)==2), And(And(balances0(i)(ag20(i))==balances0(i)(ag20(i))-amount2(i), And(tk0(i)>=amount2(i), ag20(i+1)==ag20(i) + amount2(i), tk0(i+1)==tk0(i) -amount2(i))), ag10(i+1)==ag10(i), balances(i+1)==balances(i)), And(ag10(i+1)==ag10(i), ag20(i+1)==ag20(i), tk0(i+1)==tk0(i), balances(i+1)==balances(i)))))))

timeStart = time.time()

queries = [
    
]

def parse(m):
    out = ''
    for i in range(0, 11):
        out += '|' 
        out += 'T0:' + str(m.eval(tk0(i))) + ' | ' 
        out += 'A1' + '[' + str(m.eval(ag10(i))) + ':T0' + ']' + ' | ' 
        out += 'A2' + '[' + str(m.eval(ag20(i))) + ':T0' + ']' + ' | ' 
        out += '\n' 
    return out

for q in queries:
    print(str(q) + " : ", end = '')
    if s.check(q)==sat:
        print(" sat")
        print(parse(s.model()))
    else:
        print(" unsat")

timeTot = time.time() - timeStart
print("Solving time: " + str(timeTot) + "s")
        
