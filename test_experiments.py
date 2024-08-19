import os
import subprocess
import time
import sys
import argparse


def run_makefile(folder, dict_res):
    # Change directory to the specified folder
    orig_dir = os.getcwd()

    os.chdir(folder)
    
    # List all files in the current directory
    files = os.listdir('.')

    # Filter '.sol' files
    sol_files = [file for file in files if file.endswith('.sol')]
    sol_files.sort()

    for sol in sol_files:
        clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        clean_output, clean_error = clean_process.communicate()
        #print(f"{sol=}")
        passed = 0
        not_passed = 0
        timeout = 0
        starting_time_sol = time.time()
        liquid_up_to = None
        status = None

        print('\n---------------------')
        print(f'Contract: {sol}\n')
        try:
            
            compilation_time = 0
            running_time = 0
            compile_and_run_time = 0
            for iteration in range(1, N_Transactions+1):
                # Start timing
                start_time = time.time()
                """
                # Compile the code
                #compile_process = subprocess.Popen(['make', 'compile', f'Contract={sol}', f'N_Transactions={N_Transactions}', 'Can_Transactions_Arrive_Any_time=True', f'Fixed_Iteration={iteration}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                #compile_run = compile_process.communicate(compile_process, timeout=Timeout)
                

                compile_process = subprocess.run(['make', 'compile', f'Contract={sol}', f'N_Transactions={N_Transactions}', 'Can_Transactions_Arrive_Any_time=True', f'Fixed_Iteration={iteration}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)
                
                if compile_process.returncode != 0:
                    print(f"Compilation failed for {folder}. Error message:\n{compile_process.stderr.decode()}")
                    return

                end_time = time.time()
                compilation_time += end_time - start_time

                # Start timing
                start_time = time.time()

                # Run the code
                run_process = subprocess.run(['make', 'run', 'SMT=cvc5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)
                """
                # Start timing
                start_time = time.time()

                if iteration == try_statebased_iter:  # Try statebased
                    compile_and_run_process = subprocess.run(f"make compile Contract={sol} N_Transactions={N_Transactions} Can_Transactions_Arrive_Any_time=True Fixed_Iteration={iteration}; echo end_compile_start_run; make run SMT={solver}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)
                else:
                    compile_and_run_process = subprocess.run(f"make compile Contract={sol} N_Transactions={N_Transactions} Can_Transactions_Arrive_Any_time=True Fixed_Iteration={iteration} State_Based=false; echo end_compile_start_run; make run SMT={solver} State_Based=false", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)


                if compile_and_run_process.returncode != 0:
                    print(f"Compilation or Execution failed for {folder}. Error message:\n{compile_and_run_process.stderr.decode()}")
                    return

                end_time = time.time()
                compile_and_run_time += end_time - start_time

                # If timeout passed, don't consider last result
                if compile_and_run_time > Timeout:
                    compile_and_run_time = Timeout     # TODO
                    break


                # Print the output of the make run command
                # print(f"Output for {folder}:\n")
                stop = False
                ok = False
                res = compile_and_run_process.stdout.decode()
                #print(f"{res=}")
                res_compile, res_run = res.split("end_compile_start_run")
                for phi in res_run.split('PROPERTY:'):
                    if 'out/' not in phi: continue
                    phi = phi.split('\n')
                    if iteration == 1: print(f'PROPERTY: {phi[0]}')
                    if '_nonliquid' in phi[0] or '_notliquid' in phi[0]:
                        if 'NOT LIQUID' in phi[-2]:
                            print_passed()
                            print_not_liquid(iteration)
                            print('')
                            passed += 1
                            status = "passed"
                            stop = True
                            ok = True
                        elif 'LIQUID'  in phi[-2]  and not 'UP TO' in phi[-2]:        # Strong unsat
                            print_not_passed()
                            not_passed += 1
                            status = "not passed"
                            stop = True
                            pass
                        elif 'LIQUID'  in phi[-2]  and 'UP TO' in phi[-2]:    # Weak unsat
                            pass
                            # print_not_passed()
                            # not_passed += 1
                        else:
                            pass
                            # print_not_passed()
                            # not_passed += 1
                    else:
                        #print(f"{phi[-2]=}")
                        if 'NOT LIQUID'  in phi[-2]:
                            ok = False
                            stop = True
                            # print_not_passed()
                            # not_passed += 1
                        elif 'LIQUID' in phi[-2] and 'UP TO' not in phi[-2]:  # Strong unsat
                            stop = True
                            ok = True
                            print_passed()
                            print_liquid(-1)
                            print('')
                            status = "passed"
                            passed += 1
                        elif 'LIQUID' in phi[-2]:
                            ok = True
                            liquid_up_to = iteration
                            #print(f"{liquid_up_to=}")
                            # print_not_passed()
                            # not_passed += 1
                        else:
                            ok = True
                            # print_not_passed()
                            # not_passed += 1
                if stop:
                    break
            if not ok:
                print_not_passed()
                print('')
                status = "not passed"
                not_passed += 1
            elif not stop and ok:
                print_passed()
                print_liquid(iteration)
                print('')
                status = "passed"
                passed += 1
            
            print(f"Time: {compile_and_run_time} seconds")
            #print(f"Compilation time: {compilation_time} seconds; Running time: {running_time} seconds")
        except subprocess.TimeoutExpired:
            pass 
            #timeout += 1
            #print(f"Timeout for {sol}")
        if not status:
            #print(f"{liquid_up_to=}")
            if liquid_up_to:
                print_passed()
                print_liquid(liquid_up_to)
                print('')
                print(f"Time: {compile_and_run_time} seconds")
                status = "passed"
                passed += 1
            else:
                status = "timeout"  
                timeout += 1
                print(f"Timeout for {sol}")


        clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        clean_output, clean_error = clean_process.communicate()
        dict_res[sol] = (passed, not_passed, timeout)

    # Change back to the original directory
    os.chdir(orig_dir)
    return dict_res

def print_passed():
    print("\033[92mPassed\033[0m", end='', flush=True)  # ANSI escape code for green text

def print_not_passed():
    print("\033[91mNot Passed\033[0m", end='', flush=True)  # ANSI escape code for red text

def print_not_liquid(i):
    if i == 1:
        print(f"\t - \t\033[94mNOT LIQUID (counterexample found in {i} step)\033[0m\n", end='', flush=True)  # ANSI escape code for blue text
    else:
        print(f"\t - \t\033[94mNOT LIQUID (counterexample found in {i} steps)\033[0m\n", end='', flush=True)  # ANSI escape code for blue text


def print_liquid(i = None):
    if i == -1:         # LIQUID
        print(f"\t - \t\033[93mLIQUID\033[0m\n", end='', flush=True)  # ANSI escape code for blue text
    elif i >= 0:        # LIQUID up to i
        print(f"\t - \t\033[93mLIQUID (up to {i-1})\033[0m\n", end='', flush=True)  # ANSI escape code for blue text
    # else -> unknown, don't print anything


def main(sys_argv):

    parser = argparse.ArgumentParser(prog='')
    parser.add_argument ('--N_Transactions', help='Max number of transactions of the bounded model checking problem.', action='store', required=False, type=int, default=500)
    parser.add_argument ('--Timeout', help='Timeout for each verification task.', action='store', required=False, type=int, default=1000)
    parser.add_argument ('--solver', help='Name of the SMT solver (e.g., z3 or cvc5)', action='store', required=True, type=str)
    parser.add_argument ('--try_statebased_iter', help='Try to use predicate abstraction after *n* successfull steps of bmc.', action='store', required=False, type=int, default=5)
    parser.add_argument ('--no_regression', help="If 'True' (default), does not run regression tests; if 'False', it runs also regression tests.", action='store', required=False, type=bool, default=True)
    parser.add_argument ('--only_regression', help='Run only regression tests', action='store_true')
    parser.set_defaults(only_regression=False)

    args= parser.parse_args()   
    global N_Transactions, Timeout, solver, try_statebased_iter

    N_Transactions = args.N_Transactions
    Timeout = args.Timeout  # seconds
    solver = args.solver
    try_statebased_iter = args.try_statebased_iter  # Try statebased after given number of iterations
    only_regression = args.only_regression
    no_regression = args.no_regression

    # List all directories in the current directory

    if only_regression:
        directories = sorted([f"./experiments/contracts/{d}" for d in os.listdir('./contracts') if "regression" in d])
    else:
        if no_regression:
            directories = sorted([f"./experiments/contracts/{d}" for d in os.listdir('./contracts') if "regression" not in d])
        else:
            directories = sorted([f"./experiments/contracts/{d}" for d in os.listdir('./contracts')])
    #print(f"{directories=}")
    dict_res = {}
    # Run makefile for each directory
    for directory in directories:
        os.chdir('.')
        makefile_path = os.path.join(f"{directory}", 'Makefile')
        #print(f"{makefile_path=}")
        if os.path.exists(makefile_path):
            dict = run_makefile(directory, dict_res)
            dict_res.update(dict)
        else:
            raise Exception(f"makefile_path not found: {makefile_path}")

    # print wrap up
    print('\n\nResults overview:\n')

    exp_succ = True

    for k in dict_res:
        if dict_res[k][0]+dict_res[k][1] == 0:
            perc = 0
        else:
            perc = dict_res[k][0]/(dict_res[k][0]+dict_res[k][1])*100
        print('Contract:', k, dict_res[k][0], "\033[92mPassed\033[0m,", dict_res[k][1], "\033[91mNot Passed\033[0m", dict_res[k][2], "\033[93mTimeout\033[0m", '\t[', str(perc)+'%', ']')
        if dict_res[k][1]>0:
            exp_succ = False

    if exp_succ:
        print("\n\nAll experiments were successful.")
    else:
        print("\n\nSome experiments were not successful.")



if __name__ == '__main__':

    # os.chdir('./contracts')
    main(sys.argv)