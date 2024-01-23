from functions import split_string, command_incorrect_matcher

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
    instructions = split_string(content)
    line = 1
    for i in instructions:
        if i == 0:
            line += 1
            continue
        
        if i[0] not in VALID_INSTRUCTIONS:
            result['error'] = f'Invalid instruction - {i[0]} - on line {line}.'
            match = command_incorrect_matcher(i[0], VALID_INSTRUCTIONS)
            if match:
                result['error'] += f' Did you mean - {match} - ?'
            return result
       
        if i[0] in ['add','sub','mul','div']:
            
          
            if len(i) != 3:
                result['error'] = f'Invalid instruction {" ".join(i)} on line {line}'
                return result
            
            if i[1] not in VALID_REGISTERS:
                result['error'] = f'Invalid register - {i[1]} - on line {line}'
                match = command_incorrect_matcher(i[1], VALID_REGISTERS)
                if match:
                    result['error'] += f' Did you mean - {match} - ?'
                return result
            
            #verify if its a number
            if i[2].isdigit():
                formated = {'type':'number', 'value':float(i[2])}
                i[2] = formated
            
            elif i[2] in VALID_REGISTERS:
                formated = {'type':'register', 'value':i[2]}
                i[2] = formated

            else:
                raise Exception(f'Invalid value {i[2]}')
 
        if i[0] == MOV:
          
            if len(i) != 3:
                result['error'] = f'Invalid instruction {i}'
                return result


            if i[1] not in VALID_REGISTERS:
                result['error'] = f'Invalid register -> {i[1]} <- on line {line}.'
                match = command_incorrect_matcher(i[1], VALID_REGISTERS)
                if match:
                    result['error'] += f' Did you mean - {match} - ?'
                return result
            
            elif i[2].startswith('"') or i[2].startswith("'"):
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
        line += 1
    
    instructions = [i for i in instructions if i != 0]
    result['instructions'] = instructions
    return result