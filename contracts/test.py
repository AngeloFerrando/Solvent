import os
import subprocess

N_Transactions = 5

def run_makefile(folder):
    # Change directory to the specified folder
    os.chdir(folder)
    
    # List all files in the current directory
    files = os.listdir('.')

    # Filter '.sol' files
    sol_files = [file for file in files if file.endswith('.sol')]

    for sol in sol_files:
        print('\n---------------------')
        print(f'Contract: {sol}\n')
        # Compile the code
        compile_process = subprocess.Popen(['make', 'compile', f'Contract={sol}', f'N_Transactions={N_Transactions}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        compile_output, compile_error = compile_process.communicate()

        if compile_process.returncode != 0:
            print(f"Compilation failed for {folder}. Error message:\n{compile_error.decode()}")
            return

        # Run the code
        run_process = subprocess.Popen(['make', 'run', 'SMT=cvc5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        run_output, run_error = run_process.communicate()

        if run_process.returncode != 0:
            print(f"Execution failed for {folder}. Error message:\n{run_error.decode()}")
            return

        # Print the output of the make run command
        # print(f"Output for {folder}:\n")
        res = run_output.decode()
        for phi in res.split('PROPERTY:'):
            if 'out/' not in phi: continue
            phi = phi.split('\n')
            print(f'PROPERTY: {phi[0]}')
            if '_nonliq' in phi[0]:
                if 'NOT LIQUID' in phi[-2]:
                    print_passed()
                else:
                    print_not_passed()
            else:
                if 'NOT LIQUID' in phi[-2]:
                    print_not_passed()
                else:
                    print_passed()
            print('')

        clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        clean_output, clean_error = run_process.communicate()

    # Change back to the original directory
    os.chdir('..')

def print_passed():
    print("\033[92mPassed\033[0m", end='', flush=True)  # ANSI escape code for green text

def print_not_passed():
    print("\033[91mNot Passed\033[0m", end='', flush=True)  # ANSI escape code for red text


# List all directories in the current directory
directories = sorted([d for d in os.listdir('.') if os.path.isdir(d)])
directories.remove('regression')
directories.insert(0, 'regression')

# Run makefile for each directory
for directory in directories:
    makefile_path = os.path.join(directory, 'Makefile')
    if os.path.exists(makefile_path):
        run_makefile(directory)
    else:
        print(f"No makefile found in {directory}")
