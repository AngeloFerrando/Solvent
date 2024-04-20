import re, time
import pprint
from functools import cmp_to_key
import sys

def was_internal_var(var):
    first2letters = var[:2]
    return first2letters == "t_"
    pattern = re.compile("t_")
    return pattern.match(first2letters) != None

def get_subscripts(var):
    pattern = re.compile("_([0-9]+)")
    subscripts = [x for x in re.findall(pattern, var)]
    return subscripts

def get_var_name(var, i, user):
    var_spl = var.split('_')
    if(user):
        var_name = '_'.join(var_spl[:-2]) + '[' + var_spl[-1] + ']'
    else:
        var_name = '_'.join(var_spl[:-1])
    var_name = var_name.replace("_func", "")
    if var_name == 'xa':
        var_name = 'msg.sender'
    if var_name == 'xn':
        var_name = 'msg.value'
    if var_name == 'block_num':
        var_name = 'block.number'
    if var_name == 'w':
        var_name = 'balance' 
    if var_name[:3] == 'aw[':
        var_name = 'user_balance[' + var_name[3:] 
    return var_name

    var_name = var.replace(f"_{i}","",  )
    if user:
        var_name = var.replace(f"_{user}","",  )
    return var_name

def is_state_variable(var, var_name):
    is_trans_variable = ( "_func" in var) or (var_name == "f") or ( "constructor" in var_name) or ("msg." in var_name) or (var_name == "block.num")
    return not is_trans_variable
    

def construct_trace_obj(text):
    trace_obj = {}
    orig_vars_sort = {}
    pattern_def_fun = re.compile("\(define-fun (.+?) \(\) (.+?) (\(?.+?\)?)\)")
    def_funs= [x for x in re.findall(pattern_def_fun, text)] 
    for def_fun in def_funs:
        var = def_fun[0]
        if was_internal_var(var):
            #print("internal")
            continue
        #print("\n",def_fun)
        sort = def_fun[1]
        value = def_fun[2]
        subscripts = get_subscripts(var)
        assert(len(subscripts)>0)
        assert(len(subscripts)<3)
        i = int(subscripts[0])
        if len(subscripts)==2:
            user = subscripts[1]
        else:
            user = None
        #print(subscripts)
        var_name = get_var_name(var, i, user)
        #print("varn name: ",var_name)
        is_state_var = is_state_variable(var, var_name)
        #print(is_state_var)
        if not i in trace_obj.keys():
            trace_obj[i] = {}

        trace_obj[i][var_name] = {'sort' : sort,
                          'is_state_var' : is_state_var,
                          'value' : value,
                          'user' : user
        }
        #pprint.pprint( trace_obj[i])
        #assignment[]
    return trace_obj

def print_trans_var(trace_i, var):
    if "constructor" in var or "msg." in var or var == "f":
        return True
    if not 'f' in  trace_i.keys() :
        return True
    f_value = trace_i['f']['value'].replace("_func","")
    #print(f"{f_value=}")
    #print(f"{var=}")
    if f_value in var:
        return True
    else:
        return False
    
def trans_var_order(v1, v2):
    if v1 == "f":
        return -1
    elif v2 == "f":
        return 1
    else:
        return v1 < v2

def parse_trace(text):
    trace_obj = construct_trace_obj(text)
    #pprint.pprint( trace_obj)
    trans = list(trace_obj.keys())  
    trans.sort()
    #print(trans)
    for i in trans:
        #print(f"{i=}")
        trace_i = trace_obj[i]
        vars = list(trace_i.keys())
        vars.sort()
        state_vars = [var for var in vars if trace_i[var]['is_state_var']]
        trans_vars = [var for var in vars if not trace_i[var]['is_state_var']]
        trans_vars = sorted(trans_vars, key=cmp_to_key(trans_var_order))
        #print("\n",vars)
        #print(f"{state_vars=}")
        #print(f"{trans_vars=}")
        trace_i_state = {k: v for k, v in trace_i.items() if  v['is_state_var']}
        trace_i_trans = {k: v for k, v in trace_i.items() if not v['is_state_var']}
        #print("trace_i_state:")
        #pprint.pprint(trace_i_state)
        #print("trace_i_trans:")
        #pprint.pprint(trace_i_trans)
        print(f"\n\nSTATE {i}")
        for var in state_vars:
            print(f"\t{var} = {trace_i[var]['value']}")
        if i > transaction: break
        print(f"\n\nTRANSACTION {i} => {int(i)+1}")
        for var in trans_vars:
            if  print_trans_var(trace_i, var):
                value_pr = trace_i[var]['value'].replace("_func", "")
                print(f"\t{var} = {value_pr}")

text = open(sys.argv[1],"r").read()
transaction = int(sys.argv[2])

parse_trace(text)
