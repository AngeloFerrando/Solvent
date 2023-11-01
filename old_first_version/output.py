
from z3 import *
import time

N = 10

f = Function('f', IntSort(), IntSort())
Time = Function('Time', IntSort(), IntSort())
Sender = Function('Sender', IntSort(), IntSort())
n = Int('n')
ag10 = Function('ag10', IntSort(), IntSort())
ag20 = Function('ag20', IntSort(), IntSort())
tk0 = Function('tk0', IntSort(), IntSort())
xn0 = Function('xn0', IntSort(), IntSort())
amount1 = Function('amount1', IntSort(), IntSort())

s = Solver()

s.add(And(tk0(0) == 0))

for i in range(N):
    s.add(If(And(f(i)==1, Sender(i)==1), And(Time(i)>=6, Time(i)<10, ag10(i)>=xn0(i), xn0(i)==0, amount1(i)<=(tk0(i)+xn0(i)), amount1(i)>=0, And(tk0(i+1)==(tk0(i)+xn0(i))-amount1(i), ag10(i+1)==(ag10(i)-xn0(i))+amount1(i)), ag20(i+1)==ag20(i)), If(And(f(i)==1, Sender(i)==2), And(Time(i)>=6, Time(i)<10, ag20(i)>=xn0(i), xn0(i)==0, amount1(i)<=(tk0(i)+xn0(i)), amount1(i)>=0, And(tk0(i+1)==(tk0(i)+xn0(i))-amount1(i), ag20(i+1)==(ag20(i)-xn0(i))+amount1(i)), ag10(i+1)==ag10(i)), And(ag10(i+1)==ag10(i), ag20(i+1)==ag20(i), tk0(i+1)==tk0(i)))))

timeStart = time.time()

queries = [
    ForAll(n,Implies(And(n>=0,n<=10),(ag10(n)+ag20(n))-(ag10(0)+ag20(0))<=tk0(0)))
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
        
