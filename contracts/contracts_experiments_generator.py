
import sys
import os



def main(args):
    if not os.path.exists('./experiments'):
        os.makedirs('./experiments')
    directories = sorted([d for d in os.listdir('.') if os.path.isdir(d) and 'cache' not in d and 'experiments' not in d and 'regression' not in d])
    for directory in directories:
        print('Generate experiments for', directory)
        if not os.path.exists('./experiments/' + directory):
            os.makedirs('./experiments/' + directory)
        os.chdir(directory)
        # List all files in the current directory
        files = os.listdir('.')
        with open('Makefile', 'r') as file_old:
            with open(f'../experiments/{directory}/Makefile', 'w') as file_new:
                file_new.write(file_old.read().replace('../../main.py', '../../../main.py'))
        # Filter '.sol' files
        sol_files = [file for file in files if file.endswith('.sol')]
        for sol in sol_files:
            with open(sol, 'r') as f_sol:
                content = f_sol.read()
            content = content.replace('// property', '// ')
            index = content.index('property')
            for property in content[index:].split('property'):
                 if '{' not in property: continue
                 property = 'property '+ property
                 with open('../experiments/' + directory + '/' + sol.replace('.sol', '') + '_' + property[9:property.index('{')].replace(' ', '') + '.sol', 'w') as f_sol:
                      f_sol.write(content[:index])
                      f_sol.write(property)
        os.chdir('../')
            

if __name__ == '__main__':
    # os.chdir('./contracts')
    main(sys.argv)
