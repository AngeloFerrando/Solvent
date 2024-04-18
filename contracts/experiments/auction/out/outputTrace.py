
from z3 import *
import time
import sys


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
N = 11

# A = upper bound on the number of actors (A+1)
A = 2

# Maximum functions depth
M = 50

# Contract's balance
w = [Int("w_%s" % (i)) for i in range(N+1)]
w_q0 = Int("wq0")


# Block number
block_num = [Int("block_num_%s" % (i)) for i in range(N+1)]

Proc = Datatype('Proc')
Proc.declare('bid_func')
Proc.declare('close_func')
Proc.declare('coinbase')

Proc = Proc.create()

# Contract's state variables

deadline = [Int("deadline_%s" % (i)) for i in range(N+1)]
t_deadline = [[Int("t_deadline_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
deadline_q0 = Int("deadlineq0")
t_deadline_q0 = [Int("t_deadlineq0_%s" % (m)) for m in range(M)]
min_bid = [Int("min_bid_%s" % (i)) for i in range(N+1)]
t_min_bid = [[Int("t_min_bid_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
min_bid_q0 = Int("min_bidq0")
t_min_bid_q0 = [Int("t_min_bidq0_%s" % (m)) for m in range(M)]
seller = [Int("seller_%s" % (i)) for i in range(N+1)]
t_seller = [[Int("t_seller_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
seller_q0 = Int("sellerq0")
t_seller_q0 = [Int("t_sellerq0_%s" % (m)) for m in range(M)]
winner = [Int("winner_%s" % (i)) for i in range(N+1)]
t_winner = [[Int("t_winner_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
winner_q0 = Int("winnerq0")
t_winner_q0 = [Int("t_winnerq0_%s" % (m)) for m in range(M)]
current_bid = [Int("current_bid_%s" % (i)) for i in range(N+1)]
t_current_bid = [[Int("t_current_bid_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
current_bid_q0 = Int("current_bidq0")
t_current_bid_q0 = [Int("t_current_bidq0_%s" % (m)) for m in range(M)]
closed = [Bool("closed_%s" % (i)) for i in range(N+1)]
t_closed = [[Bool("t_closed_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
closed_q0 = Bool("closedq0")
t_closed_q0 = [Bool("t_closedq0_%s" % (m)) for m in range(M)]

# Called procedure
f = [Const("f_%s" % (i), Proc) for i in range(N+1)]
f_q0 = Const("f_q0", Proc)


# users' wallets
aw = [[Int("aw_%s_%s" % (i, j)) for j in range(A+1)] for i in range(N+1)]
aw_q0 = [Int("awq0_%s" % j) for j in range(A+1)]


# msg.sender
xa = [Int("xa_%s" % (i)) for i in range(N+1)]
xa_q = Int("xa_q")

# msg.value
xn = [Int("xn_%s" % (i)) for i in range(N+1)]
xn_q0 = Int("xn_q0")


# functions args
constructor_b = [Int("constructor_b_%s" % (i)) for i in range(N+1)]
constructor_d = [Int("constructor_d_%s" % (i)) for i in range(N+1)]
constructor_m = [Int("constructor_m_%s" % (i)) for i in range(N+1)]
constructor_b_q0 = Int("constructor_b0_q")
constructor_d_q0 = Int("constructor_d0_q")
constructor_m_q0 = Int("constructor_m0_q")

# List of ids hard coded
hard_coded_list = [0]

# Temporary contract balance. Used inside functions to model internal states
t_w = [[Int("t_w_%s_%s" % (i, m)) for m in range(M)] for i in range(N+1)]
t_w_q0 = [Int("t_wq0_%s" % (m)) for m in range(M)]
 

# Temporary users wallets
t_aw = [[[Int("t_aw_%s_%s_%s" % (i, m, j)) for j in range(A+1)]
         for m in range(M)] for i in range(N+1)]

t_aw_q0 = [[Int("t_awq0_%s_%s" % (m, j)) for j in range(A+1)] for m in range(M)]


s = Solver()

def next_state_tx(aw1, aw2, w1, w2, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext):
    return And(w2 == w1,
               And([aw2[j] == aw1[j] for j in range(A+1)])
               , deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, winnerNow==winnerNext, current_bidNow==current_bidNext, closedNow==closedNext
               )

def send(sender_id, amount, w_b, w_a, aw_b, aw_a): # '_b' and '_a' mean 'before' and 'after'
    return And(w_a == w_b - amount,
                  And([If(j == sender_id,
                          aw_a[j] == aw_b[j] + amount,
                          aw_a[j] == aw_b[j]) for j in range(A+1)]))


def constructor(xa1, xn1, constructor_m,constructor_d,constructor_b, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed):
    return And(xn1 == 0, 
	And(And(
	t_seller[0] == constructor_b,
	And(
	t_deadline[0] == constructor_d,
	And(
	t_min_bid[0] == constructor_m,
	t_closed[0] == False))), True, t_seller[0]>=1, t_seller[0]<=A, t_winner[0]==0, t_current_bid[0]==0, next_state_tx(awNow, awNext, wNow, wNext, t_deadline[0], deadlineNext, t_min_bid[0], min_bidNext, t_seller[0], sellerNext, t_winner[0], winnerNext, t_current_bid[0], current_bidNext, t_closed[0], closedNext)))

def bid_func(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed):
    return And(t_w[0] == wNow + xn1, 
	And(If(
	Not(Not(closedNow)), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(
		And(If(
	Not(xn1>=min_bidNow), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(
		And(If(
	Not(xn1>current_bidNow), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(
		And(If(
	Not(current_bidNow>= 0), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(send(winnerNow, current_bidNow, t_w[0], t_w[1], awNow, t_aw[0]), And(And(
	t_winner[0] == xa1,
	t_current_bid[0] == xn1),True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[1], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, t_winner[0], winnerNext, t_current_bid[0], current_bidNext, closedNow, closedNext)))),True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[1], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, t_winner[0], winnerNext, t_current_bid[0], current_bidNext, closedNow, closedNext)))),True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[1], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, t_winner[0], winnerNext, t_current_bid[0], current_bidNext, closedNow, closedNext)))),True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[1], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, t_winner[0], winnerNext, t_current_bid[0], current_bidNext, closedNow, closedNext))))))

def close_func(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed):
    return If(Not(xn1==0), next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), 
	And(If(
	Not(Not(closedNow)), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(
		And(If(
	Not(xa1 == sellerNow), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(
		And(If(
	Not(block_num>deadlineNow), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(
		And(And(
	t_closed[0] == True,
	If(
	Not(wNow>= 0), 
		next_state_tx(awNow, awNext, wNow, wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext), And(send(sellerNow, wNow, wNow, t_w[0], awNow, t_aw[0]), True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[0], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, t_closed[0], closedNext)))),True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[0], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, t_closed[0], closedNext)))),True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[0], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, t_closed[0], closedNext)))),True, deadlineNow==deadlineNext, min_bidNow==min_bidNext, sellerNow==sellerNext, next_state_tx(t_aw[0], awNext, t_w[0], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, t_closed[0], closedNext))))))

def coinbase(xa1, xn1, awNow, awNext, wNow, wNext, t_aw, t_w, block_num, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed):
	return And(t_w[0] == wNow + xn1, next_state_tx(awNow, awNext, t_w[0], wNext, deadlineNow, deadlineNext, min_bidNow, min_bidNext, sellerNow, sellerNext, winnerNow, winnerNext, current_bidNow, current_bidNext, closedNow, closedNext))


def user_is_legit(xa1):
    return And(xa1 >= 1, xa1 <= A)


def user_has_not_already_played(xa, xa1, f, i):
    return Not(Or([And(xa[k] == xa1, f[k] == Proc.pay) for k in range(i)]))


def user_is_not_hard_coded(xa1):
    return Not(Or([xa1 == hc_i for hc_i in hard_coded_list]))


def user_is_fresh(xa, xa1, f, i):
    return And(user_is_not_hard_coded(xa1), user_has_not_already_played(xa, xa1, f, i))

# transition rules

def step_trans(f1, xa1, xn1,  aw1, aw2, w1, w2, t_aw, t_w, block_num1, block_num2, i, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed):
    return And(And(xn1 >= 0, w2 >= 0),
               And([aw1[j] >= 0 for j in range(A+1)]),
               block_num2 >= block_num1,
               sellerNext >= 0, sellerNext <= A, winnerNext >= 0, winnerNext <= A, 
               	If(f1 == Proc.coinbase, And(xa1 == 0, 
	coinbase(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, block_num1, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed)),
And(xa1 >= 1, xa1 <= A, 	If(f1 == Proc.bid_func,
		bid_func(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, block_num1, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed),
			close_func(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, block_num1, deadlineNow, deadlineNext, t_deadline, min_bidNow, min_bidNext, t_min_bid, sellerNow, sellerNext, t_seller, winnerNow, winnerNext, t_winner, current_bidNow, current_bidNext, t_current_bid, closedNow, closedNext, t_closed)))))

# initial state
s.add(w[0] >= 0)
               
new_state = And(And(xa[0] >= 0, xa[0] <= A, xn[0] >= 0),
               And([aw[0][j] >= 0 for j in range(A+1)]),
                  constructor(xa[0], xn[0], constructor_m[0],constructor_d[0],constructor_b[0],  aw[0], aw[1], w[0], w[1], t_aw[0], t_w[0], block_num[0], deadline[0], deadline[1], t_deadline[0], min_bid[0], min_bid[1], t_min_bid[0], seller[0], seller[1], t_seller[0], winner[0], winner[1], t_winner[0], current_bid[0], current_bid[1], t_current_bid[0], closed[0], closed[1], t_closed[0]))
s.add(new_state)
for i in range(1, N):
    new_state = step_trans(f[i], xa[i], xn[i],  aw[i],
                           aw[i+1], w[i], w[i+1], t_aw[i], t_w[i], block_num[i], block_num[i+1], i, deadline[i], deadline[i+1], t_deadline[i], min_bid[i], min_bid[i+1], t_min_bid[i], seller[i], seller[i+1], t_seller[i], winner[i], winner[i+1], t_winner[i], current_bid[i], current_bid[i+1], t_current_bid[i], closed[i], closed[i+1], t_closed[i])
    s.add(new_state)


# print(s)

# def p(i):
#     t_awq_list = [t_awq_m_j for t_awq_m in t_aw_q for t_awq_m_j in t_awq_m]
#     #print([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ])
#     return And(w[i] > 0,
#                Exists([xa_q], And(user_is_legit(xa_q), user_is_fresh(xa, xa_q, f,  i),
#                       ForAll([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list, deadline_q, *t_deadline_q, min_bid_q, *t_min_bid_q, seller_q, *t_seller_q, winner_q, *t_winner_q, current_bid_q, *t_current_bid_q, closed_q, *t_closed_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw_q, t_w_q, i, deadline[i], deadline_q, t_deadline_q, min_bid[i], min_bid_q, t_min_bid_q, seller[i], seller_q, t_seller_q, winner[i], winner_q, t_winner_q, current_bid[i], current_bid_q, t_current_bid_q, closed[i], closed_q, t_closed_q)), w_q > 0)))))
#                       #ForAll([xn_q, f_q, w_q, *aw_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw[i], t_w[i], i)), w_q > 0)))))



def p_seller_wd2_live_1(i):
    t_awq_list0 = [t_awq_m_j for t_awq_m in t_aw_q0 for t_awq_m_j in t_awq_m]; 
    return And(
        Exists([xa_q], And(user_is_legit(xa_q), And(And(And(winner[i]!=0,w[i]>0),block_num[i]>deadline[i]),Not(closed[i])),
            ForAll([xn_q0, f_q0, w_q0, *aw_q0, *t_w_q0, *t_awq_list0, deadline_q0, *t_deadline_q0, min_bid_q0, *t_min_bid_q0, seller_q0, *t_seller_q0, winner_q0, *t_winner_q0, current_bid_q0, *t_current_bid_q0, closed_q0, *t_closed_q0],  
                Or(
Not(step_trans(f_q0, seller[i], xn_q0, aw[i], aw_q0, w[i], w_q0, t_aw_q0, t_w_q0, block_num[i], block_num[i], i+0, deadline[i], deadline_q0, t_deadline_q0, min_bid[i], min_bid_q0, t_min_bid_q0, seller[i], seller_q0, t_seller_q0, winner[i], winner_q0, t_winner_q0, current_bid[i], current_bid_q0, t_current_bid_q0, closed[i], closed_q0, t_closed_q0)),

Not(And(And([Or(j != seller[i], aw_q0[j] >= (aw[i][j]+current_bid[i])) for j in range(A+1)]),current_bid[i]>=min_bid[i]))
        )))))

iteration = 11

queries = {}
queries['seller_wd2_live'] = [[p_seller_wd2_live_1(i)] for i in range(iteration, iteration+1)]


for prop in {'seller_wd2_live'}:
    for i, q in enumerate(queries[prop]):
        for j in range(0, len(q)):
            i = iteration - 1
            qj = q[j]
            s2 = Solver()
            s2.add(s.assertions())
            s2.add(qj)
            text = s2.to_smt2()
            # text = '(set-logic ALL)\n' + text
            text = '(set-logic ALL)\n' + text + '\n(get-model)' 
            filename = 'out/smt2/%s/tracebased/%s/output_%s.smt2'%(prop, str(i).zfill(len(str(len(queries[prop])))), str(j).zfill(len(str(len(q)))))
            if not os.path.exists('out/smt2/'):
                os.makedirs('out/smt2/')
            if not os.path.exists('out/smt2/%s/'%(prop)):
                os.makedirs('out/smt2/%s/'%(prop))
            if not os.path.exists('out/smt2/%s/tracebased/'%(prop)):
                os.makedirs('out/smt2/%s/tracebased/'%(prop))
            if not os.path.exists('out/smt2/%s/tracebased/%s/'%(prop, str(i).zfill(len(str(len(queries[prop])))))):
                os.makedirs('out/smt2/%s/tracebased/%s/'%(prop, str(i).zfill(len(str(len(queries[prop]))))))
            with open(filename, 'w') as my_file:
                my_file.write(text)

# timeStart = time.time()
# for prop in {'seller_wd2_live'}:
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
#     if not liquid: print("not liquid [in 1 steps]")
#     else: print("liquid [in 1 steps]")
#     timeTot = time.time() - timeStart
#     print("Solving time: " + str(timeTot) + "s")
               
