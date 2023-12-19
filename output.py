
from z3 import *
import time


def stringOfXA(m, i):
    return "A" + str(m.eval(xa[i]))


def stringOfTx(m, i):
    contract = "C4"
    sender = stringOfXA(m, i)
    method = str(m.eval(f[i]))
    args = str(m.eval(xn[i]))
    return "-- " + sender + ": " + contract + "." + method + "(" + args + ") -->"


def stringOfWal(m, i):
    s = ""
    for j in range(A+1):
        s += "A" + str(j) + "[" + str(m.eval(aw[i][j])) + ":T] | "
    return s


def stringOfContr(m, i):
    contract = "C4"
    return contract + "[" + str(m.eval(w[i])) + ":T] "


def stringOfSuccess(m, i):
    s = "| success:"
    return s + str(m.eval(success[i]))


def printState(m):
    for i in range(N):
        print(stringOfWal(m, i), end='')
        print(stringOfContr(m, i), end='')
        print(stringOfSuccess(m, i), end='')
        print()
        print(stringOfTx(m, i), end='')
        print()
    print(stringOfWal(m, N), end='')
    print(stringOfContr(m, N), end='')
    print()


timeStart = time.time()

# N = upper bound on the length of trace
N = 2

# A = upper bound on the number of actors (A+1)
A = 2

# Maximum functions depth
M = 1

# Contract's balance
w = [Int("w_%s" % (i)) for i in range(N+1)]
w_q = Int("wq")

Proc = Datatype('Proc')
Proc.declare('pay')

Proc = Proc.create()

# Contract's state variables

maxCount = [Int("maxCount_%s" % (i)) for i in range(N+1)]
maxCount_q = Int("maxCountq")
t_maxCount = [[Int("t_maxCount_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
t_maxCount_q = [Int("t_maxCountq_%s" % (m)) for m in range(M)]
count = [Int("count_%s" % (i)) for i in range(N+1)]
count_q = Int("countq")
t_count = [[Int("t_count_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
t_count_q = [Int("t_countq_%s" % (m)) for m in range(M)]
owner = [Int("owner_%s" % (i)) for i in range(N+1)]
owner_q = Int("ownerq")
t_owner = [[Int("t_owner_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
t_owner_q = [Int("t_ownerq_%s" % (m)) for m in range(M)]
myMap = [[Int("myMap_%s_%s" % (i, j)) for j in range(A+1)] for i in range(N+1)]
myMap_q = [Int("myMapq_%s" % j) for j in range(A+1)]
t_myMap = [[[Int("t_myMap_%s_%s_%s" % (i, m, j)) for j in range(A+1)] for m in range(M)] for i in range(N+1)]
t_myMap_q = [[Int("t_myMapq_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]

# Called procedure
f = [Const("f_%s" % (i), Proc) for i in range(N+1)]
f_q = Const("f_q", Proc)

# users' wallets
aw = [[Int("aw_%s_%s" % (i, j)) for j in range(A+1)] for i in range(N+1)]
aw_q = [Int("awq_%s" % j) for j in range(A+1)]

# msg.sender
xa = [Int("xa_%s" % (i)) for i in range(N+1)]
xa_q = Int("xa_q")

# msg.value
xn = [Int("xn_%s" % (i)) for i in range(N+1)]
xn_q = Int("xn_q")

# functions args


# List of ids hard coded
hard_coded_list = [0]

# Temporary contract balance. Used inside functions to model internal states
t_w = [[Int("t_w_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
t_w_q = [Int("t_wq_%s" % (m)) for m in range(M)] 

# Temporary users wallets
t_aw = [[[Int("t_aw_%s_%s_%s" % (i, m, j)) for j in range(A+1)]
         for m in range(M)] for i in range(N+1)]

t_aw_q = [[Int("t_awq_%s_%s" % (m, j)) for j in range(A+1)]
         for m in range(M)]

s = Solver()

# initial state
s.add(w[0] >= 0)
# s.add(w[0] == 1)

def next_state_tx(aw1, aw2, w1, w2, maxCountNow, maxCountNext, countNow, countNext, ownerNow, ownerNext, myMapNow, myMapNext):
    return And(w2 == w1,
               And([aw2[j] == aw1[j] for j in range(A+1)])
               , maxCountNow==maxCountNext, countNow==countNext, ownerNow==ownerNext
               , And([myMapNow[j] == myMapNext[j] for j in range(A+1)]))

def send(sender_id, amount, w_b, w_a, aw_b, aw_a): # '_b' and '_a' mean 'before' and 'after'
    return And(w_a == w_b - amount,
                  And([If(j == sender_id,
                          aw_a[j] == aw_b[j] + amount,
                          aw_a[j] == aw_b[j]) for j in range(A+1)]))


def constructor(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, maxCountNow, maxCountNext, t_maxCount, countNow, countNext, t_count, ownerNow, ownerNext, t_owner, myMapNow, myMapNext, t_myMap):
    return And(t_w[0] == wNow + xn1, 
	And(And(
	t_owner[0] == xa1,
	And(
	t_maxCount[0] == 1,
	And(t_count[0] == 0, next_state_tx(awNow, awNext, t_w[0], wNext, t_maxCount[0], maxCountNext, t_count[0], countNext, t_owner[0], ownerNext, myMapNow, myMapNext))))))


def pay(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, maxCountNow, maxCountNext, t_maxCount, countNow, countNext, t_count, ownerNow, ownerNext, t_owner, myMapNow, myMapNext, t_myMap):
    return If(Not(xn1==0), next_state_tx(awNow, awNext, wNow, wNext, maxCountNow, maxCountNext, countNow, countNext, ownerNow, ownerNext, myMapNow, myMapNext), 
	And(If(
	Not(t_count[0]<t_maxCount[0]), 
		next_state_tx(awNow, awNext, wNow, wNext, maxCountNow, maxCountNext, countNow, countNext, ownerNow, ownerNext, myMapNow, myMapNext), And(
		And(
	And(t_myMap[0][xa1] == 10, And([t_myMap[0][j] == myMapNow[j] for j in range(A+1) if j != xa1])),
	And(
	And(t_myMap[1][xa1] == t_myMap[0][xa1]+2, And([t_myMap[1][j] == t_myMap[0][j] for j in range(A+1) if j != xa1])),
	And(If(And(xa1==t_owner[0]),And(t_count[0] == countNow+1),And(And(
	t_count[0] == countNow,
	send(xa1, wNow, wNow, t_w[0], awNow, t_aw[0])))), next_state_tx(t_aw[0], awNext, t_w[0], wNext, maxCountNow, maxCountNext, t_count[0], countNext, ownerNow, ownerNext, t_myMap[1], myMapNext))))))))



def user_is_legit(xa1):
    return And(xa1 >= 0, xa1 <= A)


def user_has_not_already_played(xa, xa1, f, i):
    return Not(Or([And(xa[k] == xa1, f[k] == Proc.pay) for k in range(i)]))


def user_is_not_hard_coded(xa1):
    return Not(Or([xa1 == hc_i for hc_i in hard_coded_list]))


def user_is_fresh(xa, xa1, f, i):
    return And(user_is_not_hard_coded(xa1), user_has_not_already_played(xa, xa1, f, i))

# transition rules

def step_trans(f1, xa1, xn1,  aw1, aw2, w1, w2, t_aw, t_w, i, maxCountNow, maxCountNext, t_maxCount, countNow, countNext, t_count, ownerNow, ownerNext, t_owner, myMapNow, myMapNext, t_myMap):
    return And(And(xa1 >= 0, xa1 <= A, xn1 >= 0),
               And([aw1[j] >= 0 for j in range(A+1)]),
               	pay(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, maxCountNow, maxCountNext, t_maxCount, countNow, countNext, t_count, ownerNow, ownerNext, t_owner, myMapNow, myMapNext, t_myMap))

new_state = And(And(xa[0] >= 0, xa[0] <= A, xn[0] >= 0),
               And([aw[0][j] >= 0 for j in range(A+1)]),
                  constructor(xa[0], xn[0],  aw[0], aw[1], w[0], w[1], t_aw[0], t_w[0], maxCount[0], maxCount[1], t_maxCount[0], count[0], count[1], t_count[0], owner[0], owner[1], t_owner[0], myMap[0], myMap[1], t_myMap[0]))
s.add(new_state)
for i in range(1, N):
    new_state = step_trans(f[i], xa[i], xn[i],  aw[i],
                           aw[i+1], w[i], w[i+1], t_aw[i], t_w[i], i, maxCount[i], maxCount[i+1], t_maxCount[i], count[i], count[i+1], t_count[i], owner[i], owner[i+1], t_owner[i], myMap[i], myMap[i+1], t_myMap[i])
    s.add(new_state)


# print(s)

def p(i):
    t_awq_list = [t_awq_m_j for t_awq_m in t_aw_q for t_awq_m_j in t_awq_m]
    #print([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ])
    return And(w[i] > 0,
               Exists([xa_q], And(user_is_legit(xa_q), user_is_fresh(xa, xa_q, f,  i),
                      ForAll([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list, maxCount_q, *t_maxCount_q, count_q, *t_count_q, owner_q, *t_owner_q, myMap_q, *t_myMap_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw_q, t_w_q, i, maxCount[i], maxCount_q, t_maxCount_q, count[i], count_q, t_count_q, owner[i], owner_q, t_owner_q, myMap[i], myMap_q, t_myMap_q)), w_q > 0)))))
                      #ForAll([xn_q, f_q, w_q, *aw_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw[i], t_w[i], i)), w_q > 0)))))

queries = [p(i) for i in range(1, N)]

# queries = [ p(0) ]

for i, q in enumerate(queries):
    timeStart = time.time()
    # print("q : ", q)
    print("p " + str(i) + " : ", end='')
    # sq = s
    # sq.add(q)
    # print("\n\nsq:", sq, "\n\n")
    res = s.check(q)
    if res == sat:
        print(" sat (=> not liquid)")
        m = s.model()
        # print(m)
        #printState(m)
        # exit()
    else:
        print(" unsat (=> liquid)")

    timeTot = time.time() - timeStart
    print("Solving time: " + str(timeTot) + "s")
                      

