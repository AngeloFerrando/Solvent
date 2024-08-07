import os
import subprocess
import time
import argparse

try_statebased_iter = 5 # Try statebased after given number of iterations

def remove_files_and_folder(folder_path):
    # Remove all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error while deleting file {file_path}: {e}")

    # Remove the folder itself
    try:
        os.rmdir(folder_path)
    except Exception as e:
        print(f"Error while deleting folder {folder_path}: {e}")

def split_properties(Contract):
    if not os.path.exists('./split'):
        os.makedirs('./split')
    with open(Contract, 'r') as f_sol:
        content = f_sol.read()
    content = content.replace('// property', '// ')
    index = content.index('property')
    for property in content[index:].split('property'):
            if '{' not in property: continue
            property = 'property '+ property
            with open('./split/' + Contract.replace('.sol', '').replace('/', '_') + '_' + property[9:property.index('{')].replace(' ', '') + '.sol', 'w') as f_sol:
                f_sol.write(content[:index])
                f_sol.write(property)

def run_makefile(Contract, N_Transactions, Solver, Timeout):
    clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    clean_output, clean_error = clean_process.communicate()
    
    liquid_up_to = None
    status = None

    print('\n---------------------')
    print(f'Contract: {Contract}\n')

    split_properties(Contract)

    # List all files in the current directory
    files = os.listdir('./split/')

    # Filter '.sol' files
    sol_files = [file for file in files if file.endswith('.sol')]

    for sol in sol_files:
        try:
            compile_and_run_time = 0
            for iteration in range(1, N_Transactions+1):
                # Start timing
                start_time = time.time()

                if iteration == try_statebased_iter:  # Try statebased
                    compile_and_run_process = subprocess.run(f"make compile Contract=./split/{sol} N_Transactions={N_Transactions} Can_Transactions_Arrive_Any_time=True Fixed_Iteration={iteration}; echo end_compile_start_run; make run SMT={Solver}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)
                else:
                    compile_and_run_process = subprocess.run(f"make compile Contract=./split/{sol} N_Transactions={N_Transactions} Can_Transactions_Arrive_Any_time=True Fixed_Iteration={iteration} State_Based=false; echo end_compile_start_run; make run SMT={Solver} State_Based=false", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)


                if compile_and_run_process.returncode != 0:
                    print(f"Compilation or Execution failed for {sol}. Error message:\n{compile_and_run_process.stderr.decode()}")
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
                print(res_run)
                for phi in res_run.split('PROPERTY:'):
                    if 'out/' not in phi: continue
                    phi = phi.split('\n')
                    if iteration == 1: print(f'PROPERTY: {phi[0]}')
                    if '_nonliquid' in phi[0] or '_notliquid' in phi[0]:
                        if 'NOT LIQUID' in phi[-2]:
                            print_not_liquid(iteration)
                            print('')
                            status = "passed"
                            stop = True
                            ok = True
                        elif 'LIQUID'  in phi[-2]  and not 'UP TO' in phi[-2]:        # Strong unsat
                            print_liquid(-1)
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
                            print_liquid(-1)
                            print('')
                            status = "passed"
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
                print_not_liquid(iteration)
                print('')
                status = "not passed"
            elif not stop and ok:
                print_liquid(iteration)
                print('')
                status = "passed"
                
            print(f"Time: {compile_and_run_time} seconds")
            #print(f"Compilation time: {compilation_time} seconds; Running time: {running_time} seconds")
        except subprocess.TimeoutExpired:
            pass 
            #timeout += 1
            #print(f"Timeout for {sol}")
        if not status:
            #print(f"{liquid_up_to=}")
            if liquid_up_to:
                print_liquid(liquid_up_to)
                print('')
                print(f"Time: {compile_and_run_time} seconds")
                status = "passed"
            else:
                status = "timeout"  
                print(f"Timeout for {sol}")

    remove_files_and_folder('./split')

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solvent: a formal verification tool to verify Smart Contracts.")
    parser.add_argument("contract", type=str, help="Path to the smart contract file (.sol)")
    parser.add_argument("num_transactions", type=int, help="Number of transactions")
    parser.add_argument("solver", type=str, help="Name of the SMT solver (e.g., z3 or cvc5)")
    parser.add_argument("-t", "--timeout", type=int, help="Timeout for the verification process (optional)")

    args = parser.parse_args()

    contract_path = args.contract
    num_transactions = args.num_transactions
    solver = args.solver
    timeout = args.timeout if args.timeout else 1500
    
    run_makefile(contract_path, num_transactions, solver, timeout)
    