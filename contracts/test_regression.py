import os
import subprocess
import time

N_Transactions = 5
Timeout = 20 # seconds

def run_makefile(folder):
    # Change directory to the specified folder
    os.chdir(folder)
    
    # List all files in the current directory
    files = os.listdir('.')

    # Filter '.sol' files
    sol_files = [file for file in files if file.endswith('.sol')]

    for sol in sol_files:
        passed = 0
        not_passed = 0
        timeout = 0

        print('\n---------------------')
        print(f'Contract: {sol}\n')
        try:
            # Start timing
            start_time = time.time()

            # Compile the code
            compile_process = subprocess.run(['make', 'compile', f'Contract={sol}', f'N_Transactions={N_Transactions}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)
            
            if compile_process.returncode != 0:
                print(f"Compilation failed for {folder}. Error message:\n{compile_process.stderr.decode()}")
                return

            end_time = time.time()
            compilation_time = end_time - start_time

            # Start timing
            start_time = time.time()

            # Run the code
            run_process = subprocess.run(['make', 'run', 'SMT=cvc5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)
            
            if run_process.returncode != 0:
                print(f"Execution failed for {folder}. Error message:\n{run_process.stderr.decode()}")
                return

            end_time = time.time()
            running_time = end_time - start_time

            # Print the output of the make run command
            # print(f"Output for {folder}:\n")
            res = run_process.stdout.decode()
            for phi in res.split('PROPERTY:'):
                if 'out/' not in phi: continue
                phi = phi.split('\n')
                print(f'PROPERTY: {phi[0]}')
                if '_nonliquid' in phi[0] or '_notliquid' in phi[0]:
                    if 'NOT LIQUID' in phi[-2]:
                        print_passed()
                        passed += 1
                    elif 'LIQUID'  in phi[-2]:
                        print_not_passed()
                        not_passed += 1
                    else:
                        print_not_passed()
                        not_passed += 1
                else:
                    if 'NOT LIQUID'  in phi[-2]:
                        print_not_passed()
                        not_passed += 1
                    elif 'LIQUID' in phi[-2]:
                        print_passed()
                        passed += 1
                    else:
                        print_not_passed()
                        not_passed += 1
                print('')

            print(f"Compilation time: {compilation_time} seconds; Running time: {running_time} seconds")
        except subprocess.TimeoutExpired:
            timeout += 1
            print(f"Timeout for {sol}")
        clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        clean_output, clean_error = clean_process.communicate()
        dict_res[sol] = (passed, not_passed, timeout)

    # Change back to the original directory
    os.chdir('..')
    return dict_res

def print_passed():
    print("\033[92mPassed\033[0m", end='', flush=True)  # ANSI escape code for green text

def print_not_passed():
    print("\033[91mNot Passed\033[0m", end='', flush=True)  # ANSI escape code for red text


# List all directories in the current directory
directories = ['regression'] #sorted([d for d in os.listdir('.') if os.path.isdir(d)])

dict_res = {}
# Run makefile for each directory
for directory in directories:
    makefile_path = os.path.join(directory, 'Makefile')
    if os.path.exists(makefile_path):
        dict = run_makefile(directory)
        dict_res.update(dict)

# print wrap up
print('\n\nResults overview:\n')
for k in dict_res:
    if dict_res[k][0]+dict_res[k][1] == 0:
        perc = 0
    else:
        perc = dict_res[k][0]/(dict_res[k][0]+dict_res[k][1])*100
    print('Contract:', k, dict_res[k][0], "\033[92mPassed\033[0m,", dict_res[k][1], "\033[91mNot Passed\033[0m", dict_res[k][2], "\033[93mTimeout\033[0m", '\t[', str(perc)+'%', ']')