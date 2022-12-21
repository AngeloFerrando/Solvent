from z3 import *
import time

# @pre xn > 0
# f0(xa?xn:T) { if wal(T)>=100 then xa!wal(T):T }

# N = upper bound on the length of trace
N = 6

# A's balance
a0 = IntVector('a0', N+1)
# B's balance
a1 = IntVector('a1', N+1)
# Contract's balance
w = IntVector('w', N+1)
# Called procedure
f = IntVector('f', N+1)
# Actual parameter xn
xn = IntVector('xn', N+1)
# Actual parameter xa
xa = IntVector('xa', N+1)

def stringOfF(m,i):
    n = m.eval(f[i])
    if n==0:
        return "f0"
    else:
        return "fUnk"

def stringOfXA(m,i):
    n = m.eval(xa[i])
    if n==0: return "A"
    elif n==1: return "B"
    else: return "Unk"

def printState(m):
    for i in range(N):
        print("A[" + str(m.eval(a0[i])) + ":T] | ", end='')
        print("B[" + str(m.eval(a1[i])) + ":T] | ", end='')
        print("CoinPusher[" + str(m.eval(w[i])) + ":T] ", end='')
        print()
        print("  --" + stringOfF(m,i) + "(" + stringOfXA(m,i) + "?"+ str(m.eval(xn[i])) + ":T)-->", end='')
        print()

    print("A[" + str(m.eval(a0[N])) + ":T] | ", end='')
    print("B[" + str(m.eval(a1[N])) + ":T] | ", end='')
    print("CoinPusher[" + str(m.eval(w[N])) + ":T] ", end='')
    print()

s = Solver()

s.add(a0[0]==1,a1[0]==100,w[0]==0)

for i in range(N):
    s.add(f[i]==0)
    s.add(xn[i]>=0)
    #s.add(Or(xa[i]==0,xa[i]==1))
    s.add(Implies(xa[i]==0,a0[i]>=xn[i]))
    s.add(Implies(xa[i]==1,a1[i]>=xn[i]))
    s.add(
        If(And(xa[i]==0,a0[i]>=xn[i]),
           If(And(xn[i]+w[i]>=100,xn[i]>0),
              And(a0[i+1]==a0[i]+w[i],w[i+1]==0,a1[i+1]==a1[i]),
              And(a0[i+1]==a0[i]-xn[i],w[i+1]==w[i]+xn[i],a1[i+1]==a1[i])),
           If(And(xa[i]==1,a1[i]>=xn[i]),
              If(And(xn[i]+w[i]>=100,xn[i]>0),
                 And(a1[i+1]==a1[i]+w[i],w[i+1]==0,a0[i+1]==a0[i]),
                 And(a1[i+1]==a1[i]-xn[i],w[i+1]==w[i]+xn[i],a0[i+1]==a0[i])),
          # fallback
          And(a0[i+1]==a0[i],a1[i+1]==a1[i],w[i+1]==w[i])
    )))

# for c in s.assertions():
#     print(c)

timeStart = time.time()

queries = [
    a0[i]+a1[i]+w[i]!=a0[0]+a1[0]+w[0],  # Wealth preservation
#    w[i]==0,               # Depletion
#    a0[4]>100               # Specific wealth
]

for q in queries:
    print(str(q) + " : ", end = '')
    if s.check(q)==sat:
        print(" sat")
        printState(s.model())
    else:
        print(" unsat")

timeTot = time.time() - timeStart
print("Solving time: " + str(timeTot) + "s")

# print(s.statistics())
