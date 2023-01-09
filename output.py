
from z3 import *
import time

N = 10

f = Function('f', IntSort(), IntSort())
Time = Function('Time', IntSort(), IntSort())
Sender = Function('Sender', IntSort(), IntSort())
m = Int('m')
n = Int('n')
x = Function('x', IntSort(), IntSort())
ag10 = Function('ag10', IntSort(), IntSort())
ag20 = Function('ag20', IntSort(), IntSort())
ag30 = Function('ag30', IntSort(), IntSort())
tk0 = Function('tk0', IntSort(), IntSort())
xn0 = Function('xn0', IntSort(), IntSort())

s = Solver()

s.add(And(x(0) == 0, tk0(0) == 0))

for i in range(N):
    s.add(If(And(f(i)==0, Sender(i)==1), And(Time(i)>=0, Time(i)<2, ag10(i)>=xn0(i), xn0(i)>0, If((tk0(i)+xn0(i))>=100, And(tk0(i+1)==(tk0(i)+xn0(i))-(tk0(i)+xn0(i)), ag10(i+1)==(ag10(i)-xn0(i))+(tk0(i)+xn0(i))), And(ag10(i+1)==(ag10(i)-xn0(i)), tk0(i+1)==(tk0(i)+xn0(i)))), ag20(i+1)==ag20(i), ag30(i+1)==ag30(i), x(i+1)==x(i)), If(And(f(i)==0, Sender(i)==2), And(Time(i)>=0, Time(i)<2, ag20(i)>=xn0(i), xn0(i)>0, If((tk0(i)+xn0(i))>=100, And(tk0(i+1)==(tk0(i)+xn0(i))-(tk0(i)+xn0(i)), ag20(i+1)==(ag20(i)-xn0(i))+(tk0(i)+xn0(i))), And(ag20(i+1)==(ag20(i)-xn0(i)), tk0(i+1)==(tk0(i)+xn0(i)))), ag10(i+1)==ag10(i), ag30(i+1)==ag30(i), x(i+1)==x(i)), If(And(f(i)==0, Sender(i)==3), And(Time(i)>=0, Time(i)<2, ag30(i)>=xn0(i), xn0(i)>0, If((tk0(i)+xn0(i))>=100, And(tk0(i+1)==(tk0(i)+xn0(i))-(tk0(i)+xn0(i)), ag30(i+1)==(ag30(i)-xn0(i))+(tk0(i)+xn0(i))), And(ag30(i+1)==(ag30(i)-xn0(i)), tk0(i+1)==(tk0(i)+xn0(i)))), ag10(i+1)==ag10(i), ag20(i+1)==ag20(i), x(i+1)==x(i)), And(ag10(i+1)==ag10(i), ag20(i+1)==ag20(i), ag30(i+1)==ag30(i), tk0(i+1)==tk0(i), x(i+1)==x(i))))))

timeStart = time.time()

queries = [
    ForAll(n,Implies(And(And(n>=0,n<=5),tk0(n)>0),Exists(m,And(And(m>n,m<=10),tk0(m)==0)))),
	And(And(And(And(tk0(0)==98,ag10(0)==1),ag20(0)==1),ag30(0)==1),Exists(n,And(And(n>=0,n<=5),ag20(n)==100)))
]

def parse(m):
    out = ''
    for i in range(0, 11):
        out += '|' 
        out += 'T0:' + str(m.eval(tk0(i))) + ' | ' 
        out += 'A1' + '[' + str(m.eval(ag10(i))) + ':T0' + ']' + ' | ' 
        out += 'A2' + '[' + str(m.eval(ag20(i))) + ':T0' + ']' + ' | ' 
        out += 'A3' + '[' + str(m.eval(ag30(i))) + ':T0' + ']' + ' | ' 
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
        
