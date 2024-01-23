import re
from difflib import SequenceMatcher

def split_string(content:str):
    commands=content.lower().split("\n")
    lis_commands = []
    for command in commands:
        if len(command) == 0:
            lis_commands.append(0)
            continue

        inner_string = re.findall(r'"(.*?)"|\'(.*?)\'', command) or [("",""),]
        total_string = inner_string[0][0] + inner_string[0][1]
        text_string = f"'{total_string}'" if total_string else ""

        no_string = re.sub(r'"(.*?)"|\'(.*?)\'', '', command)
        splitted = [i for i in no_string.split(" ")]
        splitted.append(text_string)
        splitted = [i for i in splitted if i != '']
        
        if splitted:
            lis_commands.append(splitted)
    return lis_commands

def command_incorrect_matcher(command:str, valid_commands:list)->bool:
    for valid_command in valid_commands:
        ratio = SequenceMatcher(None, command, valid_command).ratio()
        if ratio > 0.8:
            return valid_command
        
    return False