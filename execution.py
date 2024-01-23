from lexer import *

def execute_virtual_machine(instructions):

    stack  = []
    regirsters = {
        STATE:None,
        A:None,
        B:None,
        C:None,
    }
    for i in instructions:
        instruction = i[0]
        
        if instruction == MOV:
            register = i[1]
            value = i[2]
            if value['type'] in ['number','string']:
                regirsters[register] = value['value']
        
        if instruction == SYSCALL:
        
        
            if regirsters[STATE] == 'print':
                print(regirsters[A])
           

            if regirsters[STATE] == 'exit':
                exit(regirsters[A])


            if regirsters[STATE]== 'read':
                regirsters[A] = input()