
from z3 import *
import time

N = 10

f = Function('f', IntSort(), IntSort())
Time = Function('Time', IntSort(), IntSort())
Sender = Function('Sender', IntSort(), IntSort())
n = Int('n')
x = Function('x', IntSort(), IntSort())
ag10 = Function('ag10', IntSort(), IntSort())
ag20 = Function('ag20', IntSort(), IntSort())
tk0 = Function('tk0', IntSort(), IntSort())
xn0 = Function('xn0', IntSort(), IntSort())

s = Solver()

s.add(And(x(0) == 0, tk0(0) == 0))

for i in range(N):
    s.add(If(And(f(i)==0, Sender(i)==1), And(Time(i)>=0, Time(i)<2, ag10(i)>=xn0(i), xn0(i)>0, If((tk0(i)+xn0(i))>=100, And(tk0(i+1)==(tk0(i)+xn0(i))-(tk0(i)+xn0(i)), ag10(i+1)==(ag10(i)-xn0(i))+(tk0(i)+xn0(i))), And(ag10(i+1)==(ag10(i)-xn0(i)), tk0(i+1)==(tk0(i)+xn0(i)))), ag20(i+1)==ag20(i), x(i+1)==x(i)), If(And(f(i)==0, Sender(i)==2), And(Time(i)>=0, Time(i)<2, ag20(i)>=xn0(i), xn0(i)>0, If((tk0(i)+xn0(i))>=100, And(tk0(i+1)==(tk0(i)+xn0(i))-(tk0(i)+xn0(i)), ag20(i+1)==(ag20(i)-xn0(i))+(tk0(i)+xn0(i))), And(ag20(i+1)==(ag20(i)-xn0(i)), tk0(i+1)==(tk0(i)+xn0(i)))), ag10(i+1)==ag10(i), x(i+1)==x(i)), And(ag10(i+1)==ag10(i), ag20(i+1)==ag20(i), tk0(i+1)==tk0(i), x(i+1)==x(i)))))

timeStart = time.time()

queries = [
    And(And(ag10(0)==99,ag20(0)==1),Exists(n,And(And(n>=0,n<=10),ag20(n)==100))),
	Exists(n,And(And(n>=0,n<=10),(ag10(n)+ag20(n))+tk0(n)!=(ag10(0)+ag20(0))+tk0(0)))
]

def parse(model):
    tokens = dict()
    for tk in range(0, 1):
        tokens['tk' + str(tk)] = dict()
        eq = model.index('=', model.index('tk' + str(tk)))
        assignments = model[eq+3:model.index(']', eq)]
        for assignment in assignments.split(','):
            key = assignment[0:assignment.index('->')].strip()
            value = assignment[assignment.index('->')+2:].strip()
            tokens['tk' + str(tk)][key] = value
    agents = dict()
    for ag in range(1, 3):
        for tk in range(0, 1):
            agents['ag' + str(ag) + str(tk)] = dict()
            eq = model.index('=', model.index('ag' + str(ag) + str(tk)))
            assignments = model[eq+3:model.index(']', eq)]
            for assignment in assignments.split(','):
                key = assignment[0:assignment.index('->')].strip()
                value = assignment[assignment.index('->')+2:].strip()
                agents['ag' + str(ag) + str(tk)][key] = value
    sender = dict()
    eq = model.index('=', model.index('Sender'))
    assignments = model[eq+3:model.index(']', eq)]
    for assignment in assignments.split(','):
        key = assignment[0:assignment.index('->')].strip()
        value = assignment[assignment.index('->')+2:].strip()
        sender[key] = value
    time = dict()
    eq = model.index('=', model.index('Time'))
    assignments = model[eq+3:model.index(']', eq)]
    for assignment in assignments.split(','):
        key = assignment[0:assignment.index('->')].strip()
        value = assignment[assignment.index('->')+2:].strip()
        time[key] = value
    f = dict()
    eq = model.index('=', model.index('f'))
    assignments = model[eq+3:model.index(']', eq)]
    for assignment in assignments.split(','):
        key = assignment[0:assignment.index('->')].strip()
        value = assignment[assignment.index('->')+2:].strip()
        f[key] = value
    out = ''
    for i in range(0, 10):
        out += 'Coinpusher '
        for tk in range(0, 1):
            if str(i) in tokens['tk' + str(tk)]:
                out += '[' + tokens['tk' + str(tk)][str(i)] + ':' + 'T' + str(tk) + '] |'
            else:
                out += '[' + tokens['tk' + str(tk)]['else'] + ':' + 'T' + str(tk) + '] |'
        for ag in range(1, 3):
            for tk in range(0, 1):
                if str(i) in agents['ag' + str(ag) + str(tk)]:
                    out += 'A' + str(ag) + '[' + agents['ag' + str(ag) + str(tk)][str(i)] + ':' + 'T'+ str(tk) + '] |'
                else:
                    out += 'A' + str(ag) + '[' + agents['ag' + str(ag) + str(tk)]['else'] + ':' + 'T'+ str(tk) + '] |'
        out += '\n'
        if str(i) in f:
            if int(f[str(i)]) >= len(['play']):
                out += '--> skip \n'
            else:
                out += '--> ' + ['play'][int(f[str(i)])] + '('
                if str(i) in sender:
                    out += 'A' + sender[str(i)] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)) + ')' + '@' + str(i) + '\n'
                else:
                    out += 'A' + sender['else'] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)) + ')' + '@' + str(i) + '\n'
        else:
            if int(f['else']) >= len(['play']):
                out += '--> skip \n'
            else:
                out += '--> ' + ['play'][int(f['else'])] + '('
                if str(i) in sender:
                    out += 'A' + sender[str(i)] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)).replace('tk', '') + ')' + '@' + str(i) + '\n'
                else:
                    out += 'A' + sender['else'] + '!' + str(getConsumerDownV(i, agents)) + ':' + 'T' + str(getConsumerUp(i, tokens)).replace('tk', '') + ')' + '@' + str(i) + '\n'
    return out

def getConsumerDown(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) > int(elems[j][str(i+1)]):
            return j
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) > int(elems[j][str(i+1)]):
            return j
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) > int(elems[j]['else']):
           return j
    return None
def getConsumerUp(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) < int(elems[j][str(i+1)]):
            return j
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) < int(elems[j][str(i+1)]):
            return j
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) < int(elems[j]['else']):
           return j
    return None
def getConsumerDownV(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) > int(elems[j][str(i+1)]):
            return int(elems[j][str(i)]) - int(elems[j][str(i+1)])
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) > int(elems[j][str(i+1)]):
            return int(elems[j]['else']) - int(elems[j][str(i+1)])
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) > int(elems[j]['else']):
            return int(elems[j][str(i)]) - int(elems[j]['else'])
    return None
def getConsumerUpV(i, elems):
    for j in elems:
        if str(i) in elems[j] and str(i+1) in elems[j] and int(elems[j][str(i)]) < int(elems[j][str(i+1)]):
            return int(elems[j][str(i+1)]) - int(elems[j][str(i)])
        elif str(i) not in elems[j] and str(i+1) in elems[j] and int(elems[j]['else']) < int(elems[j][str(i+1)]):
            return int(elems[j][str(i+1)]) - int(elems[j]['else'])
        elif str(i) in elems[j] and str(i+1) not in elems[j] and int(elems[j][str(i)]) < int(elems[j]['else']):
           return int(elems[j]['else']) - int(elems[j][str(i)])
    return None

for q in queries:
    print(str(q) + " : ", end = '')
    if s.check(q)==sat:
        print(" sat")
        print(parse(str(s.model())))
    else:
        print(" unsat")

timeTot = time.time() - timeStart
print("Solving time: " + str(timeTot) + "s")
        
