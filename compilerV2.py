import sys
import os
import time
import argparse
from lexer import lexer
from parser import parser
from CCG import CCG

def tokenize(data, lexer):
    lexer.input(data)
    for tok in lexer:
        print(tok)

if __name__ == "__main__":

    # Parse command line arguments
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('infile', type=str)
    arg_parser.add_argument('outfile', type=str)
    arg_parser.add_argument('--dbg', action='store_true')
    arg_parser.add_argument('--lexemes', action='store_true')
    arg_parser.add_argument('--hide_tree', action='store_true')
    arg_parser.add_argument('--hide_stdout', action='store_true')
    arg_parser.add_argument('--run', action='store_true')

    args = arg_parser.parse_args()
    print(args)

    # Open input file
    try:
        input_file = open(args.infile)
    except FileNotFoundError:
        sys.exit(f"{sys.argv[0]}: FileNotFoundError: input file '{args.infile}' does not exist")
    
    # Read data from input
    data = input_file.read()

    # Debug mode lexemes
    if args.dbg or args.lexemes:
        print("\n ============= Lexemes ============\n")
        lexer.input(data)
        for tok in lexer:
            print(tok)
    
    # Create deriviation tree
    result = parser.parse(data, lexer=lexer, debug=args.dbg)
    input_file.close()
    if result == None:
        sys.exit(f"{sys.argv[0]}: SyntaxError: could not build the abstract syntax tree")
    
    # Debug mode tree
    if args.dbg or not args.hide_tree:
        print("\n ======== Deriviation Tree ========\n")
        print(result.printTree())
        print()
    
    # Generate output code from Deriviation Tree
    ccg = CCG(result)
    c_out_code = ccg.generate_code()
    
    # Debug mode C code output
    if args.dbg or not args.hide_stdout:
        print("\n ========= C Output Code ==========\n")
        print(c_out_code)
    
    # Writes to a file
    if args.outfile:
        output_file = open(args.outfile, "w")
        output_file.write(c_out_code)
        output_file.close()

    if args.run and args.outfile:
        print("\n ===== Compiled Program Output ====\n")
        os.system(f"gcc {args.outfile} -o {args.outfile[:-2]}")
        os.system(f"{args.outfile[:-2]}")
        print()
    

    