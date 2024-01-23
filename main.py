
from sys import argv 
from sys import exit
from os.path import isfile
from lexer import transform_content_into_readble_data
from execution import execute_virtual_machine
def main():
    if len(argv) < 2:
        raise Exception("File not passed")
    
    filename = argv[1]
    if(not isfile(filename)):
        raise Exception("File not found")
    with open(filename, 'r') as file:   
        content = file.read()
    
    parsed = transform_content_into_readble_data(content)
    if parsed['error']:
        raise Exception(parsed['error'])

    instructions = parsed['instructions']
    execute_virtual_machine(instructions)
    



    

main()