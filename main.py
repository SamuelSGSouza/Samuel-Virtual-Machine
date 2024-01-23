
from sys import argv 
from sys import exit
from os.path import isfile

def main():
    if len(argv) != 2:
        print("File not passed")
        exit(1)
    
    filename = argv[1]
    if(not isfile(filename)):
        print("File not found")
        exit(1)
        
    


main()