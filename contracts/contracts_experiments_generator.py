
import sys
import os



def main(args):
    if not os.path.exists('./experiments'):
        os.makedirs('./experiments')
    directories = sorted([d for d in os.listdir('.') if os.path.isdir(d) and 'cache' not in d])
    for directory in directories:
        print('Generate experiments for', directory)
        if not os.path.exists('./experiments/' + directory):
            os.makedirs('./experiments/' + directory)
        os.chdir(directory)
        # List all files in the current directory
        files = os.listdir('.')
        # Filter '.sol' files
        sol_files = [file for file in files if file.endswith('.sol')]
        for sol in sol_files:
            with open(sol, 'r') as f_sol:
                content = f_sol.read()
            content = content.replace('// property', '// ')
            index = content.index('property')
            for property in content.split('property'):
                 with open('../experiments/' + directory + '/' + sol, 'w') as f_sol:
                      f_sol.write(content[:index])
                      f_sol.write(property)
        os.chdir('../')
            

if __name__ == '__main__':
	main(sys.argv)
