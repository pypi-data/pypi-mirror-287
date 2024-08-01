import pkg_resources

def read_specific_program(program_number):
    # Get the path to prgs.txt in the package
    file_path = pkg_resources.resource_filename(__name__, 'prgs.txt')
    
    with open(file_path, 'r') as file:
        programs = file.read().split('# Program ')
    
    programs = [program.strip() for program in programs if program.strip()]
    
    for program in programs:
        if program.startswith(f"{program_number}\n") or program.startswith(f"{program_number} "):
            return program
    return None

def prg1():
    code = read_specific_program(1)
    print(code)

def prg2():
    code = read_specific_program(2)
    print(code)

def prg3():
    code = read_specific_program(3)
    print(code)

def prg4():
    code = read_specific_program(4)
    print(code)

def prg5():
    code = read_specific_program(5)
    print(code)

def prg6():
    code = read_specific_program(6)
    print(code)

def prg7():
    code = read_specific_program(7)
    print(code)

def prg8():
    code = read_specific_program(8)
    print(code)

def prg9():
    code = read_specific_program(9)
    print(code)

def prg10():
    code = read_specific_program(10)
    print(code)

