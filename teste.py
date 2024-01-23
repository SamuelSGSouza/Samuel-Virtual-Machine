import re

string = 'quero pegar o texto "esse texto" '
inner_string = re.findall(r'"(.*?)"|\'(.*?)\'', string)
sem_texto = re.sub(r'"(.*?)"|\'(.*?)\'', '', string)
print(sem_texto)
print(inner_string)