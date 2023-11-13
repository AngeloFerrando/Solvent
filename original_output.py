"""
Esempio 18: stati interni (liquid)

contract C18 {

  function deposit(?n:T) { 
	// anyone can deposit
  }

  function pay(amount) {
    require (amount<=balance); // se è falso, lo stato nuovo della blockchain è uguale a quello vecchio
    sender!1;
    require (amount-1<=balance)
    sender!amount-1;
    // se sono arrivato qui, allora lo stato nuovo della blockchain è uguale all'ultimo stato della computazione interna
  }
}

P = in ogni stato, ogni partecipante può sparare una seq atomica di tx (lunga 1) che svuota il contratto

P vera in ogni stato (equivalente all’esempio 2).

"""


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
N = 3

# A = upper bound on the number of actors (A+1)
A = 3

# Contract's balance
w = [Int("w_%s" % (i)) for i in range(N+1)]
w_q = Int("wq")

# Two kinds of procedures: either withdraw from contract balance or a dummy transaction to contract balance (same param 'amount' used for both)
Proc = Datatype('Proc')
Proc.declare('deposit')
Proc.declare('pay')
Proc = Proc.create()

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

# List of ids hard coded
hard_coded_list = [0]

# This param should be computed automatically
# Maximum functions depth
M = 2

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



def valid_tx(xa1, xn1, w1, w2):
    return And(xa1 >= 0, xa1 <= A, xn1 > 0)


"""
  function pay(amount) {
    require (amount<=balance); // se è falso, lo stato nuovo della blockchain è uguale a quello vecchio
    sender!1;
    require (amount-1<=balance)
    sender!amount-1;
    // se sono arrivato qui, allora lo stato nuovo della blockchain è uguale all'ultimo stato della computazione interna
  }

Le require vengono tradotte come if-then-else.
  
Pseudo-traduzione:

  function pay(amount) {
    if not (amount<=balance):   # the require fails 
        next_state = current_state
    else:                       # the require does not fail
        sender!1;
        if not (amount-1<=balance)  # the second require fails:
            next_state = current_state
        else:                       # the second require does not fail:
            sender!amount-1;
            next_state = last state of the internal computation           // se sono arrivato qui, allora lo stato nuovo della blockchain è uguale all'ultimo stato della computazione interna
  }

  xa1: sender id
  xn1: amount
  w1: balance in the current state
  w2: balance in the next state
  aw1: users wallets in the current state
  aw2: users wallets in the next state
  t_w (t_w[0], ..., t_w[M-1]): internal variables that model w during the computation 
  t_aw (t_aw[0], ..., t_aw[M-1]) internal variables that model aw during the computation 

"""

def next_state_tx(aw1, aw2, w1, w2):
    return And(w2 == w1,
               And([aw2[j] == aw1[j] for j in range(A+1)]))

def send(sender_id, amount, w_b, w_a, aw_b, aw_a): # '_b' and '_a' mean 'before' and 'after'
    return And(w_a == w_b - amount,
                  And([If(j == sender_id,
                          aw_a[j] == aw_b[j] + amount,
                          aw_a[j] == aw_b[j]) for j in range(A+1)]))

def pay(xa1, xn1, aw1, aw2, w1, w2,   t_aw, t_w):
            # require (amount<=balance); // se è falso, lo stato nuovo della blockchain è uguale a quello vecchio
    return  If(Not(xn1 <= w1),
              next_state_tx(aw1, aw2, w1, w2),
              # sender!1;
              And(send(xa1, 1, w1, t_w[0], aw1, t_aw[0]),
                  # require (amount-1<=balance)
                  If(Not(xn1-1 <= t_w[0]),
                     next_state_tx(aw1, aw2, w1, w2),
                     # sender!amount-1;
                     And(send(xa1, xn1-1, t_w[0], t_w[1], t_aw[0], t_aw[1]),
                         next_state_tx(t_aw[1], aw2, t_w[1], w2)
                         # this is the last implicit command 
                         # that says that if none of the requires failed
                         # then the next state 
                         # is determined by the last values of the temporary variables
                        )
                     )
                  )
              )


def deposit(xn1, w1, w2, aw1, aw2):
    return And(w2 == w1 + xn1,
               And([aw2[j] == aw1[j] for j in range(A+1)]))


def user_is_legit(xa1):
    return And(xa1 >= 0, xa1 <= A)


def user_has_not_already_played(xa, xa1, f, i):
    return Not(Or([And(xa[k] == xa1, f[k] == Proc.pay) for k in range(i)]))


def user_is_not_hard_coded(xa1):
    return Not(Or([xa1 == hc_i for hc_i in hard_coded_list]))


def user_is_fresh(xa, xa1, f, i):
    return And(user_is_not_hard_coded(xa1), user_has_not_already_played(xa, xa1, f, i))

# transition rules


def step_trans(f1, xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w, i):
    return And(valid_tx(xa1, xn1, w1, w2),
               And([aw1[j] >= 0 for j in range(A+1)]),
               If(f1 == Proc.pay,
                  pay(xa1, xn1, aw1, aw2, w1, w2, t_aw, t_w),
                  #   The only other possible transition is f[i] == Proc.deposit
                  deposit(xn1, w1, w2, aw1, aw2)
                  #new_state_tx(aw1, aw2, w1, w2)
                  ))


for i in range(N):
    new_state = step_trans(f[i], xa[i], xn[i], aw[i],
                           aw[i+1], w[i], w[i+1], t_aw[i], t_w[i], i)

    s.add(new_state)


# print(s)

def p(i):
    t_awq_list = [t_awq_m_j for t_awq_m in t_aw_q for t_awq_m_j in t_awq_m]
    #print([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ])
    return And(w[i] > 0,
               Exists([xa_q], And(user_is_legit(xa_q), user_is_fresh(xa, xa_q, f,  i),
                      ForAll([xn_q, f_q, w_q, *aw_q, *t_w_q, *t_awq_list ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw_q, t_w_q, i)), w_q > 0)))))
                      #ForAll([xn_q, f_q, w_q, *aw_q ], Or(Not(step_trans(f_q, xa_q, xn_q, aw[i], aw_q, w[i], w_q, t_aw[i], t_w[i], i)), w_q > 0)))))


queries = [p(i) for i in range(N)]

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
