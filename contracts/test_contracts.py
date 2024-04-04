import os
import subprocess
import pytest

N_Transactions = 5
Timeout = 10

def run_makefile(folder):
    os.chdir(folder)
    files = os.listdir('.')
    sol_files = [file for file in files if file.endswith('.sol')]
    try:
        for sol in sol_files:
            try:
                # Compile the code
                compile_process = subprocess.run(['make', 'compile', f'Contract={sol}', f'N_Transactions={N_Transactions}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)

                if compile_process.returncode != 0:
                    raise RuntimeError(f"Compilation failed for {folder}. Error message:\n{compile_process.stderr.decode()}")

                # Run the code
                run_process = subprocess.run(['make', 'run', 'SMT=cvc5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=Timeout)

                if run_process.returncode != 0:
                    raise RuntimeError(f"Execution failed for {folder}. Error message:\n{run_process.stderr.decode()}")

                res = run_process.stdout.decode()
                for phi in res.split('PROPERTY:'):
                    if 'out/' not in phi: continue
                    phi = phi.split('\n')

                    if '_nonliq' in phi[0]:
                        if 'NOT LIQUID' not in phi[-2]:
                            os.chdir('..')
                            clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            clean_output, clean_error = clean_process.communicate()
                            pytest.fail(f'PROPERTY: {phi[0]}')
                    else:
                        if 'NOT LIQUID' in phi[-2]:
                            os.chdir('..')
                            clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            clean_output, clean_error = clean_process.communicate()
                            pytest.fail(f'PROPERTY: {phi[0]}')
            except subprocess.TimeoutExpired:
                pass
            finally:
                clean_process = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                clean_output, clean_error = clean_process.communicate()
    finally:
        os.chdir('..')

@pytest.mark.parametrize("directory", sorted([d for d in os.listdir('.') if os.path.isdir(d) and 'cache' not in d]))
def test_run_makefile(directory):
    makefile_path = os.path.join(directory, 'Makefile')
    if os.path.exists(makefile_path):
        run_makefile(directory)
    else:
        pytest.fail(f"No makefile found in {directory}, {makefile_path}")
