
from sys import argv 
from sys import exit
from os.path import isfile
from lexer import transform_content_into_readble_data
from execution import execute_virtual_machine
def main():
    if len(argv) < 2:
        print("File not passed")
        exit(1)
    
    filename = argv[1]
    if(not isfile(filename)):
        print("File not found")
        exit(1)
    with open(filename, 'r') as file:   
        content = file.read()
    
    parsed = transform_content_into_readble_data(content)
    if parsed['error']:
        print(parsed['error'])
        exit(1)
    instructions = parsed['instructions']
    #virtual machine data
    execute_virtual_machine(instructions)
    



    

main()