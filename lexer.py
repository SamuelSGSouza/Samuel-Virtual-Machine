
MOV = 'mov'
SYSCALL = 'syscall'
VALID_INSTRUCTIONS = [
    MOV,
    'add',
    'sub',
    'mul',
    'div',
    'push',
    'pop',
    'syscall',
    'jump_equal',
    'jump_not_equal'
    ,'jump_greater_than',
    'jump_less_than',
    'jump_greater_than_equal',
    'jump_less_than_equal',
    ]


STATE = 'state'
A = 'a'
B = 'b'
C = 'c'
VALID_REGISTERS = [STATE, A, B, C]
VALID_SYSCALLS = ['print', 'read', 'exit','parse_num']



def transform_content_into_readble_data(content:str)->dict:
    result = {
        'error':None,
        'instructions':None,
    }
    instructions = content.split('\n')
    instructions = list(map(lambda x: x.strip(),instructions))
    instructions = list(filter(lambda x: x != '', instructions))
    instructions = list(map(lambda x : x.split(','), instructions))
    instructions = list(map(
        lambda x: list(map(lambda y: y.strip(), x)), 
        instructions))
    instructions = list(map(lambda x: list(filter(lambda y: y != '', x)), instructions))
   
    for i in instructions:
        
        if i[0] not in VALID_INSTRUCTIONS:
            result['error'] = f'Invalid instruction {i}'
            return result
       
        if i[0] in ['add','sub','mul','div']:
            
          
            if len(i) != 3:
                result['error'] = f'Invalid instruction {i}'
                return result
            
            if i[1] not in VALID_REGISTERS:
                result['error'] = f'Invalid register {i}'
                return result
            
            #verify if its a number
            if not i[2].isdigit():
                result['error'] = f'Invalid number {i[2]}'
                return result
            formated = {'type':'number', 'value':float(i[2])}
            i[2] = formated

        if i[0] == MOV:
          
            if len(i) != 3:
                result['error'] = f'Invalid instruction {i}'
                return result


            if i[1] not in VALID_REGISTERS:
                result['error'] = f'Invalid register {i}'
                return result
            
            elif i[2].startswith('"'):
                formated = {'type':'string', 'value':i[2][1:-1]}
            

            elif i[2] in VALID_SYSCALLS:
                formated = {'type':'string', 'value':i[2]}


            #verify if its a number
            elif i[2].isdigit():
                formated = {'type':'number', 'value':float(i[2])}
            

            elif i[2] in VALID_REGISTERS:
                formated = {'type':'register', 'value':i[2]}
            
            else:
                result['error'] = f'Invalid value {i[2]}'
                return result
            i[2] = formated
    result['instructions'] = instructions
    return result