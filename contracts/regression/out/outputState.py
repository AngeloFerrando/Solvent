
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
w_q0 = Int("wq0")
w_q1 = Int("wq1")
w_q2 = Int("wq2")
w_q3 = Int("wq3")
w_q4 = Int("wq4")


# Block number
block_num = [Int("block_num_%s" % (i)) for i in range(N+1)]

Proc = Datatype('Proc')
Proc.declare('Constructor1')
Proc.declare('pay')

Proc = Proc.create()

# Contract's state variables


# Called procedure
f = [Const("f_%s" % (i), Proc) for i in range(N+1)]
f_q0 = Const("f_q0", Proc)
f_q1 = Const("f_q1", Proc)
f_q2 = Const("f_q2", Proc)
f_q3 = Const("f_q3", Proc)
f_q4 = Const("f_q4", Proc)


# users' wallets
aw = [[Int("aw_%s_%s" % (i, j)) for j in range(A+1)] for i in range(N+1)]
aw_q0 = [Int("awq0_%s" % j) for j in range(A+1)]
aw_q1 = [Int("awq1_%s" % j) for j in range(A+1)]
aw_q2 = [Int("awq2_%s" % j) for j in range(A+1)]
aw_q3 = [Int("awq3_%s" % j) for j in range(A+1)]
aw_q4 = [Int("awq4_%s" % j) for j in range(A+1)]


# msg.sender
xa = [Int("xa_%s" % (i)) for i in range(N+1)]
xa_q = Int("xa_q")

# msg.value
xn = [Int("xn_%s" % (i)) for i in range(N+1)]
xn_q0 = Int("xn_q0")
xn_q1 = Int("xn_q1")
xn_q2 = Int("xn_q2")
xn_q3 = Int("xn_q3")
xn_q4 = Int("xn_q4")


# functions args
pay_amount = [Int("pay_amount_%s" % (i)) for i in range(N+1)]
pay_amount_q0 = Int("pay_amount0_q")
pay_amount_q1 = Int("pay_amount1_q")
pay_amount_q2 = Int("pay_amount2_q")
pay_amount_q3 = Int("pay_amount3_q")
pay_amount_q4 = Int("pay_amount4_q")

# List of ids hard coded
hard_coded_list = [0]

# Temporary contract balance. Used inside functions to model internal states
t_w = [[Int("t_w_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
t_w_q0 = [Int("t_wq0_%s" % (m)) for m in range(M)]
t_w_q1 = [Int("t_wq1_%s" % (m)) for m in range(M)]
t_w_q2 = [Int("t_wq2_%s" % (m)) for m in range(M)]
t_w_q3 = [Int("t_wq3_%s" % (m)) for m in range(M)]
t_w_q4 = [Int("t_wq4_%s" % (m)) for m in range(M)]
 

# Temporary users wallets
t_aw = [[[Int("t_aw_%s_%s_%s" % (i, m, j)) for j in range(A+1)]
         for m in range(M)] for i in range(N+1)]

t_aw_q0 = [[Int("t_awq0_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]
t_aw_q1 = [[Int("t_awq1_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]
t_aw_q2 = [[Int("t_awq2_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]
t_aw_q3 = [[Int("t_awq3_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]
t_aw_q4 = [[Int("t_awq4_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]


s = Solver()

# initial state
s.add(w[0] == 0)
# s.add(w[0] == 1)

def next_state_tx(aw1, aw2, w1, w2):
    return And(w2 == w1,
               And([aw2[j] == aw1[j] for j in range(A+1)])
               
               )

def send(sender_id, amount, w_b, w_a, aw_b, aw_a): # '_b' and '_a' mean 'before' and 'after'
    return And(w_a == w_b - amount,
                  And([If(j == sender_id,
                          aw_a[j] == aw_b[j] + amount,
                          aw_a[j] == aw_b[j]) for j in range(A+1)]))


def constructor(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num):
    return And(t_w[0] == wNow + xn1, 
	And(xn1==0, True, next_state_tx(awNow, awNext, t_w[0], wNext)))

def pay(xa1, xn1, pay_amount, awNow, awNext, wNow, wNext, t_aw, t_w, block_num):
    return If(Not(xn1==0), next_state_tx(awNow, awNext, wNow, wNext), 
	And(If(
	Not(1 >= 0), 
		next_state_tx(awNow, awNext, wNow, wNext), And(send(xa1, 1, wNow, t_w[0], awNow, t_aw[0]), True, next_state_tx(t_aw[0], awNext, t_w[0], wNext)))))


def user_is_legit(xa1):
    return And(xa1 >= 0, xa1 <= A)


def user_has_not_already_played(xa, xa1, f, i):
    return Not(Or([And(xa[k] == xa1, f[k] == Proc.pay) for k in range(i)]))


def user_is_not_hard_coded(xa1):
    return Not(Or([xa1 == hc_i for hc_i in hard_coded_list]))


def user_is_fresh(xa, xa1, f, i):
    return And(user_is_not_hard_coded(xa1), user_has_not_already_played(xa, xa1, f, i))

# transition rules

def step_trans(f1, xa1, xn1, pay_amount, aw1, aw2, w1, w2, t_aw, t_w, block_num1, block_num2, i):
    return And(And(xa1 >= 0, xa1 <= A, xn1 >= 0),
               And([aw1[j] >= 0 for j in range(A+1)]),
               block_num2 >= block_num1,
               	pay(xa1, xn1, pay_amount, aw1, aw2, w1, w2, t_aw, t_w, block_num1))

new_state = And(And(xa[0] >= 0, xa[0] <= A, xn[0] >= 0),
               And([aw[0][j] >= 0 for j in range(A+1)]),
                  constructor(xa[0], xn[0],  aw[0], aw[1], w[0], w[1], t_aw[0], t_w[0], block_num[0]))
s.add(new_state)
for i in range(1, N):
    new_state = step_trans(f[i], xa[i], xn[i], pay_amount[i], aw[i],
                           aw[i+1], w[i], w[i+1], t_aw[i], t_w[i], block_num[i], block_num[i+1], i)
    s.add(new_state)


# print(s)

# def p(i):
#     t_awq_list = [t_awq_m_j for t_awq_m in t_aw_q for t_awq_m_j in t_awq_m]
#     #print([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ])
#     return And(w[i] > 0,
#                Exists([xa_q], And(user_is_legit(xa_q), user_is_fresh(xa, xa_q, f,  i),
#                       ForAll([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list, pay_amount_q ], Or(Not(step_trans(f_q, xa_q, xn_q, pay_amount_q, aw[i], aw_q, w[i], w_q, t_aw_q, t_w_q, i)), w_q > 0)))))
#                       #ForAll([xn_q, f_q, w_q, *aw_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw[i], t_w[i], i)), w_q > 0)))))



def p_liquidity1_liq_1(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), True,
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, pay_amount_q0],  
                Or(
Not(step_trans(f_q0, xa_q, xn_q0, pay_amount_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num[i], i+0)),

And([Or(j != xa_q, Not(aw_q0[j] > aw[i][j])) for j in range(A+1)])
        )))))
def p_liquidity1_liq_2(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), True,
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, pay_amount_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, pay_amount_q1],  
                Or(
Not(step_trans(f_q0, xa_q, xn_q0, pay_amount_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num[i], i+0)),
Not(step_trans(f_q1, xa_q, xn_q1, pay_amount_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num[i], block_num[i], i+1)),

And([Or(j != xa_q, Not(aw_q1[j] > aw[i][j])) for j in range(A+1)])
        )))))
def p_liquidity1_liq_3(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), True,
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, pay_amount_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, pay_amount_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, pay_amount_q2],  
                Or(
Not(step_trans(f_q0, xa_q, xn_q0, pay_amount_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num[i], i+0)),
Not(step_trans(f_q1, xa_q, xn_q1, pay_amount_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num[i], block_num[i], i+1)),
Not(step_trans(f_q2, xa_q, xn_q2, pay_amount_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num[i], block_num[i], i+2)),

And([Or(j != xa_q, Not(aw_q2[j] > aw[i][j])) for j in range(A+1)])
        )))))
def p_liquidity1_liq_4(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; t_awq_list3 = [t_awq_m_j for t_awq_m in t_aw_q3 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), True,
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, pay_amount_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, pay_amount_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, pay_amount_q2, xn_q3, f_q3, w_q3, *aw_q3, *t_w_q3, *t_awq_list3, pay_amount_q3],  
                Or(
Not(step_trans(f_q0, xa_q, xn_q0, pay_amount_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num[i], i+0)),
Not(step_trans(f_q1, xa_q, xn_q1, pay_amount_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num[i], block_num[i], i+1)),
Not(step_trans(f_q2, xa_q, xn_q2, pay_amount_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num[i], block_num[i], i+2)),
Not(step_trans(f_q3, xa_q, xn_q3, pay_amount_q3, aw_q2, aw_q3, w_q2, w_q3, t_aw_q3, t_w_q3, block_num[i], block_num[i], i+3)),

And([Or(j != xa_q, Not(aw_q3[j] > aw[i][j])) for j in range(A+1)])
        )))))
def p_liquidity1_liq_5(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; t_awq_list3 = [t_awq_m_j for t_awq_m in t_aw_q3 for t_awq_m_j in t_awq_m]; t_awq_list4 = [t_awq_m_j for t_awq_m in t_aw_q4 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), True,
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, pay_amount_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, pay_amount_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, pay_amount_q2, xn_q3, f_q3, w_q3, *aw_q3, *t_w_q3, *t_awq_list3, pay_amount_q3, xn_q4, f_q4, w_q4, *aw_q4, *t_w_q4, *t_awq_list4, pay_amount_q4],  
                Or(
Not(step_trans(f_q0, xa_q, xn_q0, pay_amount_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num[i], i+0)),
Not(step_trans(f_q1, xa_q, xn_q1, pay_amount_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num[i], block_num[i], i+1)),
Not(step_trans(f_q2, xa_q, xn_q2, pay_amount_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num[i], block_num[i], i+2)),
Not(step_trans(f_q3, xa_q, xn_q3, pay_amount_q3, aw_q2, aw_q3, w_q2, w_q3, t_aw_q3, t_w_q3, block_num[i], block_num[i], i+3)),
Not(step_trans(f_q4, xa_q, xn_q4, pay_amount_q4, aw_q3, aw_q4, w_q3, w_q4, t_aw_q4, t_w_q4, block_num[i], block_num[i], i+4)),

And([Or(j != xa_q, Not(aw_q4[j] > aw[i][j])) for j in range(A+1)])
        )))))

queries = {}
queries['liquidity1_liq'] = [[p_liquidity1_liq_1(i),p_liquidity1_liq_2(i),p_liquidity1_liq_3(i),p_liquidity1_liq_4(i),p_liquidity1_liq_5(i)] for i in range(1, N+1)]


for prop in {'liquidity1_liq'}:
    for i, q in enumerate(queries[prop]):
        for j in range(0, len(q)):
            qj = q[j]
            s2 = Solver()
            s2.add(s.assertions())
            s2.add(qj)
            text= s2.to_smt2()
            filename = 'out/smt2/%s/statebased/%s/output_%s.smt2'%(prop, i, j)
            if not os.path.exists('out/smt2/'):
                os.makedirs('out/smt2/')
            if not os.path.exists('out/smt2/%s/'%(prop)):
                os.makedirs('out/smt2/%s/'%(prop))
            if not os.path.exists('out/smt2/%s/statebased/'%(prop)):
                os.makedirs('out/smt2/%s/statebased/'%(prop))
            if not os.path.exists('out/smt2/%s/statebased/%s/'%(prop, i)):
                os.makedirs('out/smt2/%s/statebased/%s/'%(prop, i))
            with open(filename, 'w') as my_file:
                print(my_file.write(text))

# timeStart = time.time()
# for prop in {'liquidity1_liq'}:
#     print('Property [' + prop + ']')
#     for i, q in enumerate(queries[prop]):
#         liquid = False
#         for j in range(0, len(q)):
#             qj = q[j] 
#             resj = s.check(qj)
#             if resj == unsat:
#                 liquid = True
#                 break
#         if not liquid:
#             break
#     if not liquid: print("not liquid [in 5 steps]")
#     else: print("liquid [in 5 steps]")
#     timeTot = time.time() - timeStart
#     print("Solving time: " + str(timeTot) + "s")
               
