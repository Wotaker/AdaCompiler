import sys
import os
import argparse
from lexer import lexer
from parser import parser
from CCG import CCG

DEBUG = False
SHOW_TREE = True

def tokenize(data, lexer):
    lexer.input(data)
    for tok in lexer:
        print(tok)

if __name__ == "__main__":

    # Parse arguments and initiate files

    if len(sys.argv) == 1:
        fileArg = input("Please specify file to compile:")
    else:
        fileArg = f"{sys.argv[1]}"
    
    filePath = os.path.join(os.getcwd(), "AdaFiles", fileArg)
    file = open(filePath)
    data = file.read()

    if len(sys.argv) == 3:
        DEBUG = True
    
    
    # Parse the input file

    if DEBUG:
        lexer.input(data)
        for tok in lexer:
            print(tok)

    result = parser.parse(data, lexer=lexer, debug=DEBUG)

    if result and SHOW_TREE:
        print("\n ======= Deriviation Tree =======\n")
        print(result.printTree())

    file.close()

    # Generate output code from Deriviation Tree
    if result:
        ccg = CCG(result)
        out = ccg.generate_code()
        print()
        print(out)


