
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
A = 3

# Maximum functions depth
M = 2

# Contract's balance
w = [Int("w_%s" % (i)) for i in range(N+1)]
w_q0 = Int("wq0")
w_q1 = Int("wq1")
w_q2 = Int("wq2")
w_q3 = Int("wq3")
w_q4 = Int("wq4")


# Block number
block_num = [Int("block_num_%s" % (i)) for i in range(N+1)]
block_num_q0 = Int("block_num_q0")
block_num_q1 = Int("block_num_q1")
block_num_q2 = Int("block_num_q2")
block_num_q3 = Int("block_num_q3")
block_num_q4 = Int("block_num_q4")


Proc = Datatype('Proc')
Proc.declare('timeout')
Proc.declare('join')
Proc.declare('win')

Proc = Proc.create()

# Contract's state variables

oracle = [Int("oracle_%s" % (i)) for i in range(N+1)]
t_oracle = [[Int("t_oracle_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
oracle_q0 = Int("oracleq0")
t_oracle_q0 = [Int("t_oracleq0_%s" % (m)) for m in range(M)]
oracle_q1 = Int("oracleq1")
t_oracle_q1 = [Int("t_oracleq1_%s" % (m)) for m in range(M)]
oracle_q2 = Int("oracleq2")
t_oracle_q2 = [Int("t_oracleq2_%s" % (m)) for m in range(M)]
oracle_q3 = Int("oracleq3")
t_oracle_q3 = [Int("t_oracleq3_%s" % (m)) for m in range(M)]
oracle_q4 = Int("oracleq4")
t_oracle_q4 = [Int("t_oracleq4_%s" % (m)) for m in range(M)]
deadline = [Int("deadline_%s" % (i)) for i in range(N+1)]
t_deadline = [[Int("t_deadline_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
deadline_q0 = Int("deadlineq0")
t_deadline_q0 = [Int("t_deadlineq0_%s" % (m)) for m in range(M)]
deadline_q1 = Int("deadlineq1")
t_deadline_q1 = [Int("t_deadlineq1_%s" % (m)) for m in range(M)]
deadline_q2 = Int("deadlineq2")
t_deadline_q2 = [Int("t_deadlineq2_%s" % (m)) for m in range(M)]
deadline_q3 = Int("deadlineq3")
t_deadline_q3 = [Int("t_deadlineq3_%s" % (m)) for m in range(M)]
deadline_q4 = Int("deadlineq4")
t_deadline_q4 = [Int("t_deadlineq4_%s" % (m)) for m in range(M)]
par1 = [Int("par1_%s" % (i)) for i in range(N+1)]
t_par1 = [[Int("t_par1_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
par1_q0 = Int("par1q0")
t_par1_q0 = [Int("t_par1q0_%s" % (m)) for m in range(M)]
par1_q1 = Int("par1q1")
t_par1_q1 = [Int("t_par1q1_%s" % (m)) for m in range(M)]
par1_q2 = Int("par1q2")
t_par1_q2 = [Int("t_par1q2_%s" % (m)) for m in range(M)]
par1_q3 = Int("par1q3")
t_par1_q3 = [Int("t_par1q3_%s" % (m)) for m in range(M)]
par1_q4 = Int("par1q4")
t_par1_q4 = [Int("t_par1q4_%s" % (m)) for m in range(M)]
par2 = [Int("par2_%s" % (i)) for i in range(N+1)]
t_par2 = [[Int("t_par2_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
par2_q0 = Int("par2q0")
t_par2_q0 = [Int("t_par2q0_%s" % (m)) for m in range(M)]
par2_q1 = Int("par2q1")
t_par2_q1 = [Int("t_par2q1_%s" % (m)) for m in range(M)]
par2_q2 = Int("par2q2")
t_par2_q2 = [Int("t_par2q2_%s" % (m)) for m in range(M)]
par2_q3 = Int("par2q3")
t_par2_q3 = [Int("t_par2q3_%s" % (m)) for m in range(M)]
par2_q4 = Int("par2q4")
t_par2_q4 = [Int("t_par2q4_%s" % (m)) for m in range(M)]

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
constructor_o = [Int("constructor_o_%s" % (i)) for i in range(N+1)]
constructor_d = [Int("constructor_d_%s" % (i)) for i in range(N+1)]
win_winner = [Int("win_winner_%s" % (i)) for i in range(N+1)]
constructor_o_q0 = Int("constructor_o0_q")
constructor_d_q0 = Int("constructor_d0_q")
win_winner_q0 = Int("win_winner0_q")
constructor_o_q1 = Int("constructor_o1_q")
constructor_d_q1 = Int("constructor_d1_q")
win_winner_q1 = Int("win_winner1_q")
constructor_o_q2 = Int("constructor_o2_q")
constructor_d_q2 = Int("constructor_d2_q")
win_winner_q2 = Int("win_winner2_q")
constructor_o_q3 = Int("constructor_o3_q")
constructor_d_q3 = Int("constructor_d3_q")
win_winner_q3 = Int("win_winner3_q")
constructor_o_q4 = Int("constructor_o4_q")
constructor_d_q4 = Int("constructor_d4_q")
win_winner_q4 = Int("win_winner4_q")

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
s.add(w[0] >= 0)
# s.add(w[0] == 1)

def next_state_tx(aw1, aw2, w1, w2, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next):
    return And(w2 == w1,
               And([aw2[j] == aw1[j] for j in range(A+1)])
               , oracleNow==oracleNext, deadlineNow==deadlineNext, par1Now==par1Next, par2Now==par2Next
               , )

def send(sender_id, amount, w_b, w_a, aw_b, aw_a): # '_b' and '_a' mean 'before' and 'after'
    return And(w_a == w_b - amount,
                  And([If(j == sender_id,
                          aw_a[j] == aw_b[j] + amount,
                          aw_a[j] == aw_b[j]) for j in range(A+1)]))


def constructor(xa1, xn1, constructor_d,constructor_o, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2):
    return And(t_w[0] == wNow + xn1, 
	And(If(
	Not(xn1==1), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(And(
	t_par1[0] == xa1,
	And(
	t_oracle[0] == constructor_o,
	t_deadline[0] == constructor_d)),next_state_tx(awNow, awNext, t_w[0], wNext, t_oracle[0], oracleNext, t_deadline[0], deadlineNext, t_par1[0], par1Next, par2Now, par2Next))))))

def join(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2):
    return And(t_w[0] == wNow + xn1, 
	And(If(
	Not(t_w[0]==1), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(xn1==1), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(xa1!=par1Now), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(t_par2[0] == xa1,next_state_tx(awNow, awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, t_par2[0], par2Next)))),next_state_tx(awNow, awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, t_par2[0], par2Next)))),next_state_tx(awNow, awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, t_par2[0], par2Next))))))

def win(xa1, xn1, win_winner, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2):
    return If(Not(xn1==0), next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), 
	And(If(
	Not(wNow==2), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(xa1==oracleNow), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(block_num<deadlineNow), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(Or(win_winner==par1Now,win_winner==par2Now)), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(wNow >= 0), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(send(win_winner, wNow, wNow, t_w[0], awNow, t_aw[0]), next_state_tx(t_aw[0], awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next))),next_state_tx(t_aw[0], awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next)))),next_state_tx(t_aw[0], awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next)))),next_state_tx(t_aw[0], awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next)))),next_state_tx(t_aw[0], awNext, t_w[0], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next))))))

def timeout(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2):
    return If(Not(xn1==0), next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), 
	And(If(
	Not(wNow==2), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(block_num>=deadlineNow), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(
		And(If(
	Not(1 >= 0), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(send(par1Now, 1, wNow, t_w[0], awNow, t_aw[0]), And(If(
	Not(1 >= 0), 
		next_state_tx(awNow, awNext, wNow, wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next), And(send(par2Now, 1, t_w[0], t_w[1], t_aw[0], t_aw[1]), next_state_tx(t_aw[1], awNext, t_w[1], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next))),next_state_tx(t_aw[1], awNext, t_w[1], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next)))),next_state_tx(t_aw[1], awNext, t_w[1], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next)))),next_state_tx(t_aw[1], awNext, t_w[1], wNext, oracleNow, oracleNext, deadlineNow, deadlineNext, par1Now, par1Next, par2Now, par2Next))))))


def user_is_legit(xa1):
    return And(xa1 >= 0, xa1 <= A)


def user_has_not_already_played(xa, xa1, f, i):
    return Not(Or([And(xa[k] == xa1, f[k] == Proc.pay) for k in range(i)]))


def user_is_not_hard_coded(xa1):
    return Not(Or([xa1 == hc_i for hc_i in hard_coded_list]))


def user_is_fresh(xa, xa1, f, i):
    return And(user_is_not_hard_coded(xa1), user_has_not_already_played(xa, xa1, f, i))

# transition rules

def step_trans(f1, xa1, xn1, win_winner, aw1, aw2, w1, w2, t_aw, t_w, block_num1, block_num2, i, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2):
    return And(And(xa1 >= 0, xa1 <= A, xn1 >= 0),
               And([aw1[j] >= 0 for j in range(A+1)]),
               block_num2 >= block_num1,
               If(f1 == Proc.join,
	join(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, block_num1, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2),
	If(f1 == Proc.win,
		win(xa1, xn1, win_winner, aw1, aw2, w1, w2, t_aw, t_w, block_num1, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2),
			timeout(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, block_num1, oracleNow, oracleNext, t_oracle, deadlineNow, deadlineNext, t_deadline, par1Now, par1Next, t_par1, par2Now, par2Next, t_par2))))

new_state = And(And(xa[0] >= 0, xa[0] <= A, xn[0] >= 0),
               And([aw[0][j] >= 0 for j in range(A+1)]),
                  constructor(xa[0], xn[0], constructor_d[0],constructor_o[0],  aw[0], aw[1], w[0], w[1], t_aw[0], t_w[0], block_num[0], oracle[0], oracle[1], t_oracle[0], deadline[0], deadline[1], t_deadline[0], par1[0], par1[1], t_par1[0], par2[0], par2[1], t_par2[0]))
s.add(new_state)
for i in range(1, N):
    new_state = step_trans(f[i], xa[i], xn[i], win_winner[i], aw[i],
                           aw[i+1], w[i], w[i+1], t_aw[i], t_w[i], block_num[i], block_num[i+1], i, oracle[i], oracle[i+1], t_oracle[i], deadline[i], deadline[i+1], t_deadline[i], par1[i], par1[i+1], t_par1[i], par2[i], par2[i+1], t_par2[i])
    s.add(new_state)


# print(s)

# def p(i):
#     t_awq_list = [t_awq_m_j for t_awq_m in t_aw_q for t_awq_m_j in t_awq_m]
#     #print([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ])
#     return And(w[i] > 0,
#                Exists([xa_q], And(user_is_legit(xa_q), user_is_fresh(xa, xa_q, f,  i),
#                       ForAll([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list, win_winner_q, oracle_q, *t_oracle_q, deadline_q, *t_deadline_q, par1_q, *t_par1_q, par2_q, *t_par2_q ], Or(Not(step_trans(f_q, xa_q, xn_q, win_winner_q, aw[i], aw_q, w[i], w_q, t_aw_q, t_w_q, i, oracle[i], oracle_q, t_oracle_q, deadline[i], deadline_q, t_deadline_q, par1[i], par1_q, t_par1_q, par2[i], par2_q, t_par2_q)), w_q > 0)))))
#                       #ForAll([xn_q, f_q, w_q, *aw_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw[i], t_w[i], i)), w_q > 0)))))


def p_liq1_1(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),

Or(And([Or(j != par1[i], Not(aw_q0[j]-aw[i][j] >= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q0[j]-aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq1_2(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),

Or(And([Or(j != par1[i], Not(aw_q1[j]-aw[i][j] >= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q1[j]-aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq1_3(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, block_num_q2, win_winner_q2, oracle_q2, *t_oracle_q2, deadline_q2, *t_deadline_q2, par1_q2, *t_par1_q2, par2_q2, *t_par2_q2],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),
Not(step_trans(f_q2, oracle[i], xn_q2, win_winner_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num_q1, block_num_q2, i+2, oracle_q1, oracle_q2, t_oracle_q2, deadline_q1, deadline_q2, t_deadline_q2, par1_q1, par1_q2, t_par1_q2, par2_q1, par2_q2, t_par2_q2)),

Or(And([Or(j != par1[i], Not(aw_q2[j]-aw[i][j] >= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q2[j]-aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq1_4(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; t_awq_list3 = [t_awq_m_j for t_awq_m in t_aw_q3 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, block_num_q2, win_winner_q2, oracle_q2, *t_oracle_q2, deadline_q2, *t_deadline_q2, par1_q2, *t_par1_q2, par2_q2, *t_par2_q2, xn_q3, f_q3, w_q3, *aw_q3, *t_w_q3, *t_awq_list3, block_num_q3, win_winner_q3, oracle_q3, *t_oracle_q3, deadline_q3, *t_deadline_q3, par1_q3, *t_par1_q3, par2_q3, *t_par2_q3],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),
Not(step_trans(f_q2, oracle[i], xn_q2, win_winner_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num_q1, block_num_q2, i+2, oracle_q1, oracle_q2, t_oracle_q2, deadline_q1, deadline_q2, t_deadline_q2, par1_q1, par1_q2, t_par1_q2, par2_q1, par2_q2, t_par2_q2)),
Not(step_trans(f_q3, oracle[i], xn_q3, win_winner_q3, aw_q2, aw_q3, w_q2, w_q3, t_aw_q3, t_w_q3, block_num_q2, block_num_q3, i+3, oracle_q2, oracle_q3, t_oracle_q3, deadline_q2, deadline_q3, t_deadline_q3, par1_q2, par1_q3, t_par1_q3, par2_q2, par2_q3, t_par2_q3)),

Or(And([Or(j != par1[i], Not(aw_q3[j]-aw[i][j] >= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q3[j]-aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq1_5(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; t_awq_list3 = [t_awq_m_j for t_awq_m in t_aw_q3 for t_awq_m_j in t_awq_m]; t_awq_list4 = [t_awq_m_j for t_awq_m in t_aw_q4 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, block_num_q2, win_winner_q2, oracle_q2, *t_oracle_q2, deadline_q2, *t_deadline_q2, par1_q2, *t_par1_q2, par2_q2, *t_par2_q2, xn_q3, f_q3, w_q3, *aw_q3, *t_w_q3, *t_awq_list3, block_num_q3, win_winner_q3, oracle_q3, *t_oracle_q3, deadline_q3, *t_deadline_q3, par1_q3, *t_par1_q3, par2_q3, *t_par2_q3, xn_q4, f_q4, w_q4, *aw_q4, *t_w_q4, *t_awq_list4, block_num_q4, win_winner_q4, oracle_q4, *t_oracle_q4, deadline_q4, *t_deadline_q4, par1_q4, *t_par1_q4, par2_q4, *t_par2_q4],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),
Not(step_trans(f_q2, oracle[i], xn_q2, win_winner_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num_q1, block_num_q2, i+2, oracle_q1, oracle_q2, t_oracle_q2, deadline_q1, deadline_q2, t_deadline_q2, par1_q1, par1_q2, t_par1_q2, par2_q1, par2_q2, t_par2_q2)),
Not(step_trans(f_q3, oracle[i], xn_q3, win_winner_q3, aw_q2, aw_q3, w_q2, w_q3, t_aw_q3, t_w_q3, block_num_q2, block_num_q3, i+3, oracle_q2, oracle_q3, t_oracle_q3, deadline_q2, deadline_q3, t_deadline_q3, par1_q2, par1_q3, t_par1_q3, par2_q2, par2_q3, t_par2_q3)),
Not(step_trans(f_q4, oracle[i], xn_q4, win_winner_q4, aw_q3, aw_q4, w_q3, w_q4, t_aw_q4, t_w_q4, block_num_q3, block_num_q4, i+4, oracle_q3, oracle_q4, t_oracle_q4, deadline_q3, deadline_q4, t_deadline_q4, par1_q3, par1_q4, t_par1_q4, par2_q3, par2_q4, t_par2_q4)),

Or(And([Or(j != par1[i], Not(aw_q4[j]-aw[i][j] >= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q4[j]-aw[i][j] >= 2)) for j in range(A+1)]))
        )))))

def p_liq2_1(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),

Or(And([Or(j != par1[i], Not(aw_q0[j]-aw[i][j] <= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q0[j]+aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq2_2(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),

Or(And([Or(j != par1[i], Not(aw_q1[j]-aw[i][j] <= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q1[j]+aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq2_3(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, block_num_q2, win_winner_q2, oracle_q2, *t_oracle_q2, deadline_q2, *t_deadline_q2, par1_q2, *t_par1_q2, par2_q2, *t_par2_q2],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),
Not(step_trans(f_q2, oracle[i], xn_q2, win_winner_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num_q1, block_num_q2, i+2, oracle_q1, oracle_q2, t_oracle_q2, deadline_q1, deadline_q2, t_deadline_q2, par1_q1, par1_q2, t_par1_q2, par2_q1, par2_q2, t_par2_q2)),

Or(And([Or(j != par1[i], Not(aw_q2[j]-aw[i][j] <= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q2[j]+aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq2_4(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; t_awq_list3 = [t_awq_m_j for t_awq_m in t_aw_q3 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, block_num_q2, win_winner_q2, oracle_q2, *t_oracle_q2, deadline_q2, *t_deadline_q2, par1_q2, *t_par1_q2, par2_q2, *t_par2_q2, xn_q3, f_q3, w_q3, *aw_q3, *t_w_q3, *t_awq_list3, block_num_q3, win_winner_q3, oracle_q3, *t_oracle_q3, deadline_q3, *t_deadline_q3, par1_q3, *t_par1_q3, par2_q3, *t_par2_q3],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),
Not(step_trans(f_q2, oracle[i], xn_q2, win_winner_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num_q1, block_num_q2, i+2, oracle_q1, oracle_q2, t_oracle_q2, deadline_q1, deadline_q2, t_deadline_q2, par1_q1, par1_q2, t_par1_q2, par2_q1, par2_q2, t_par2_q2)),
Not(step_trans(f_q3, oracle[i], xn_q3, win_winner_q3, aw_q2, aw_q3, w_q2, w_q3, t_aw_q3, t_w_q3, block_num_q2, block_num_q3, i+3, oracle_q2, oracle_q3, t_oracle_q3, deadline_q2, deadline_q3, t_deadline_q3, par1_q2, par1_q3, t_par1_q3, par2_q2, par2_q3, t_par2_q3)),

Or(And([Or(j != par1[i], Not(aw_q3[j]-aw[i][j] <= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q3[j]+aw[i][j] >= 2)) for j in range(A+1)]))
        )))))
def p_liq2_5(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; t_awq_list1 = [t_awq_m_j for t_awq_m in t_aw_q1 for t_awq_m_j in t_awq_m]; t_awq_list2 = [t_awq_m_j for t_awq_m in t_aw_q2 for t_awq_m_j in t_awq_m]; t_awq_list3 = [t_awq_m_j for t_awq_m in t_aw_q3 for t_awq_m_j in t_awq_m]; t_awq_list4 = [t_awq_m_j for t_awq_m in t_aw_q4 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(block_num[i]<deadline[i],w[i]==2),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, block_num_q0, win_winner_q0, oracle_q0, *t_oracle_q0, deadline_q0, *t_deadline_q0, par1_q0, *t_par1_q0, par2_q0, *t_par2_q0, xn_q1, f_q1, w_q1, *aw_q1, *t_w_q1, *t_awq_list1, block_num_q1, win_winner_q1, oracle_q1, *t_oracle_q1, deadline_q1, *t_deadline_q1, par1_q1, *t_par1_q1, par2_q1, *t_par2_q1, xn_q2, f_q2, w_q2, *aw_q2, *t_w_q2, *t_awq_list2, block_num_q2, win_winner_q2, oracle_q2, *t_oracle_q2, deadline_q2, *t_deadline_q2, par1_q2, *t_par1_q2, par2_q2, *t_par2_q2, xn_q3, f_q3, w_q3, *aw_q3, *t_w_q3, *t_awq_list3, block_num_q3, win_winner_q3, oracle_q3, *t_oracle_q3, deadline_q3, *t_deadline_q3, par1_q3, *t_par1_q3, par2_q3, *t_par2_q3, xn_q4, f_q4, w_q4, *aw_q4, *t_w_q4, *t_awq_list4, block_num_q4, win_winner_q4, oracle_q4, *t_oracle_q4, deadline_q4, *t_deadline_q4, par1_q4, *t_par1_q4, par2_q4, *t_par2_q4],  
                Or(
Not(step_trans(f_q0, oracle[i], xn_q0, win_winner_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num_q0, i+0, oracle[i], oracle_q0, t_oracle_q0, deadline[i], deadline_q0, t_deadline_q0, par1[i], par1_q0, t_par1_q0, par2[i], par2_q0, t_par2_q0)),
Not(step_trans(f_q1, oracle[i], xn_q1, win_winner_q1, aw_q0, aw_q1, w_q0, w_q1, t_aw_q1, t_w_q1, block_num_q0, block_num_q1, i+1, oracle_q0, oracle_q1, t_oracle_q1, deadline_q0, deadline_q1, t_deadline_q1, par1_q0, par1_q1, t_par1_q1, par2_q0, par2_q1, t_par2_q1)),
Not(step_trans(f_q2, oracle[i], xn_q2, win_winner_q2, aw_q1, aw_q2, w_q1, w_q2, t_aw_q2, t_w_q2, block_num_q1, block_num_q2, i+2, oracle_q1, oracle_q2, t_oracle_q2, deadline_q1, deadline_q2, t_deadline_q2, par1_q1, par1_q2, t_par1_q2, par2_q1, par2_q2, t_par2_q2)),
Not(step_trans(f_q3, oracle[i], xn_q3, win_winner_q3, aw_q2, aw_q3, w_q2, w_q3, t_aw_q3, t_w_q3, block_num_q2, block_num_q3, i+3, oracle_q2, oracle_q3, t_oracle_q3, deadline_q2, deadline_q3, t_deadline_q3, par1_q2, par1_q3, t_par1_q3, par2_q2, par2_q3, t_par2_q3)),
Not(step_trans(f_q4, oracle[i], xn_q4, win_winner_q4, aw_q3, aw_q4, w_q3, w_q4, t_aw_q4, t_w_q4, block_num_q3, block_num_q4, i+4, oracle_q3, oracle_q4, t_oracle_q4, deadline_q3, deadline_q4, t_deadline_q4, par1_q3, par1_q4, t_par1_q4, par2_q3, par2_q4, t_par2_q4)),

Or(And([Or(j != par1[i], Not(aw_q4[j]-aw[i][j] <= 2)) for j in range(A+1)]),And([Or(j != par2[i], Not(aw_q4[j]+aw[i][j] >= 2)) for j in range(A+1)]))
        )))))

queries = {}
queries['liq1'] = [[p_liq1_1(i),p_liq1_2(i),p_liq1_3(i),p_liq1_4(i),p_liq1_5(i)] for i in range(1, N)]
queries['liq2'] = [[p_liq2_1(i),p_liq2_2(i),p_liq2_3(i),p_liq2_4(i),p_liq2_5(i)] for i in range(1, N)]


timeStart = time.time()
for prop in {'liq1','liq2'}:
    print('Property [' + prop + ']')
    for i, q in enumerate(queries[prop]):
        liquid = False
        for j in range(0, len(q)):
            qj = q[j] 
            resj = s.check(qj)
            if resj == unsat:
                liquid = True
                break
        if not liquid:
            break
    if not liquid: print("not liquid [in 5 steps]")
    else: print("liquid [in 5 steps]")
    timeTot = time.time() - timeStart
    print("Solving time: " + str(timeTot) + "s")

# for i, q in enumerate(queries):
#     timeStart = time.time()
#     # print("q : ", q)
#     print("p " + str(i) + " : ", end='')
#     # sq = s
#     # sq.add(q)
#     # print("\n\nsq:", sq, "\n\n")
#     res = s.check(q)
#     if res == sat:
#         print(" sat (=> not liquid)")
#         m = s.model()
#         # print(m)
#         #printState(m)
#         # exit()
#     else:
#         print(" unsat (=> liquid)")

#     timeTot = time.time() - timeStart
#     print("Solving time: " + str(timeTot) + "s")
                      

