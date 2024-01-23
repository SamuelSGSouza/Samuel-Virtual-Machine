
def transform_content_into_readble_data(content:str):
    instructions = content.split('\n')
    instructions = list(map(lambda x: x.strip(),instructions))
    instructions = list(filter(lambda x: x != '', instructions))
    instructions = list(map(lambda x : x.split(' '), instructions))
    print(instructions)