import re

def replace_int_with_real_and_integers(file_path):
    # Open the original Lustre file in read mode
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace all occurrences of 'int' with 'real'
    content = content.replace('int', 'real')

    # Use regular expression to replace integer numbers with float
    # This regex will match integer numbers (positive or negative)
    # and it will be surrounded by non-word characters or start/end of line
    content = re.sub(r'(?<!\w)(\+?\-?\d+)(?!\w)', lambda m: m.group(1) + '.0', content)

    # Write the modified content to a new file or overwrite the original one
    new_file_path = file_path.replace(".lus","_2REALS.lus")
    with open(new_file_path, 'w') as file:
        file.write(content)

    print(f"File has been processed and saved as 'modified_{file_path}'")
    
    
    
# Usage example
file_path = 'out/outputTrace.lus'  # replace with the actual file name
replace_int_with_real_and_integers(file_path)

