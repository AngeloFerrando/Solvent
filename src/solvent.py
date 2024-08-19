import os
import subprocess
import time
import argparse
import shutil

try_statebased_iter = 5 # Try statebased after given number of iterations

def remove_folder(folder_path):
    shutil.rmtree(folder_path)

def remove_files_and_folder(folder_path):
    # Remove all files in the folder
    #print(f"{ os.listdir(folder_path)=}")
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

    if os.path.exists('./split'):
        shutil.rmtree('./split')
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
    # Get current directory
    orig_dir = os.getcwd()
    
    clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    clean_output, clean_error = clean_process.communicate()
    
    liquid_up_to = None
    status = None

    print('\n---------------------')
    print(f'Contract: {Contract}\n')

    split_properties(Contract)

    # List all files in the current directory
    files = os.listdir('./split/')

    if not os.path.exists('./counterexamples'):
        os.makedirs('./counterexamples')

    with open('./src/Makefile', 'r') as file_old:
        with open(f'./split/Makefile', 'w+') as file_new:
            #file_new.write(file_old.read().replace("Contract := './auction.sol'", f"Contract := './../../../{directory}/crowdfund-bug.sol'"))
            file_new.write(file_old.read()
                           .replace('./main.py', '../src/main.py')
                           .replace('./trace/parseTrace.py', '../src/parseTrace.py')
                           .replace('./$$Prop.counterexample', '../counterexamples/$${Prop#"out/smt2/"}.counterexample')
                           )

    # Filter '.sol' files
    sol_files = [file for file in files if file.endswith('.sol')]
    #print(f"{sol_files=}")

    os.chdir('./split/')

    for sol in sol_files:
        #print(f"{sol=}")
        try:
            compile_and_run_time = 0
            for iteration in range(1, N_Transactions+1):
                stop = False
                # Start timing
                start_time = time.time()

                if iteration == try_statebased_iter:  # Try statebased
                    compile_and_run_process = subprocess.run(f"make compile Contract={sol} N_Transactions={N_Transactions} Can_Transactions_Arrive_Any_time=True Fixed_Iteration={iteration}; echo end_compile_start_run; make run SMT={Solver} Timeout={Timeout}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)
                else:
                    compile_and_run_process = subprocess.run(f"make compile Contract={sol} N_Transactions={N_Transactions} Can_Transactions_Arrive_Any_time=True Fixed_Iteration={iteration} State_Based=false; echo end_compile_start_run; make run SMT={Solver} State_Based=false  Timeout={Timeout}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)


                if compile_and_run_process.returncode != 0:
                    print(f"Compilation or Execution failed for {sol}. Error message:\n{compile_and_run_process.stderr.decode()}")
                    remove_folder('./split')
                    return

                end_time = time.time()
                compile_and_run_time += end_time - start_time

                # If timeout passed, don't consider last result
                if compile_and_run_time > Timeout:
                    compile_and_run_time = Timeout     # TODO
                    break


                # Print the output of the make run command
                # print(f"Output for {folder}:\n")
                res = compile_and_run_process.stdout.decode()
                #print(f"{res=}")
                res_compile, res_run = res.split("end_compile_start_run")
                #print(f"{res_compile=}")
                #print(f"{res_run=}")
                #time.sleep(2)

                #print(res_run)
                for phi in res_run.split('PROPERTY:'):
                    if 'out/' not in phi: continue
                    phi = phi.split('\n')
                    if iteration == 1: print(f'\nPROPERTY: {phi[0]}')
                    if 'NOT LIQUID' in phi[-2] and iteration != try_statebased_iter:    # Strong sat
                        print_not_liquid(iteration)
                        print('')
                        stop = True
                    elif 'LIQUID'  in phi[-2]  and not 'UP TO' in phi[-2]:        # Strong unsat
                        print_liquid(-1)
                        stop = True
                        pass
                    elif 'LIQUID'  in phi[-2]  and 'UP TO' in phi[-2]:    # Weak unsat
                        liquid_up_to = iteration
                        pass
                    else:
                        pass
                if stop:
                    print(f"Time: {compile_and_run_time} seconds")
                    break                
            #print(f"Compilation time: {compilation_time} seconds; Running time: {running_time} seconds")
        except subprocess.TimeoutExpired:
            pass 
            #timeout += 1
        if not stop:
            if liquid_up_to:
                print_liquid(liquid_up_to)
                print('')
                print(f"Time: {Timeout} seconds")
                #print(f"Time: {compile_and_run_time} seconds")
            else:
                print(f'\nPROPERTY: {phi[0]}')
                print_timeout()
                #print(f"Timeout for {sol}")
        clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    remove_folder('../split')


def print_timeout():
        print(f"\t\033[95mTIMEOUT\033[0m\n", end='', flush=True) 

def print_not_liquid(i):
    if i == 1:
        print(f"\t\033[94mNOT LIQUID (counterexample found in {i} step)\033[0m", end='', flush=True)  # ANSI escape code for blue text
    else:
        print(f"\t\033[94mNOT LIQUID (counterexample found in {i} steps)\033[0m", end='', flush=True)  # ANSI escape code for blue text

def print_liquid(i = None):
    if i == -1:         # LIQUID
        print(f"\t\033[93mLIQUID\033[0m", end='', flush=True)  # ANSI escape code for blue text
    elif i >= 0:        # LIQUID up to i
        print(f"\t\033[93mLIQUID (up to {i-1})\033[0m", end='', flush=True)  # ANSI escape code for blue text
    # else -> unknown, don't print anything

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solvent: a formal verification tool to verify Smart Contracts.")
    parser.add_argument("contract", type=str, help="Path to the smart contract file (.sol)")
    parser.add_argument("num_transactions", type=int, help='Max number of transactions of the bounded model checking problem.')
    parser.add_argument("solver", type=str, help="Name of the SMT solver (e.g., z3 or cvc5)")
    parser.add_argument("-t", "--timeout", type=int, help="Timeout for the verification process (optional)")

    args = parser.parse_args()

    contract_path = args.contract
    num_transactions = args.num_transactions
    solver = args.solver
    timeout = args.timeout if args.timeout else 1500
    
    run_makefile(contract_path, num_transactions, solver, timeout)
    