'''Implementing regex grep'''

import re, argparse, sys

def main():
    #check for a file and at least one pattern to search for in the command line
    if len(sys.argv) < 2:
        print("You must have at least one file and a regex pattern")
        sys.exit()

    #create an argparser to parse the command line arguments
    parser = argparse.ArgumentParser(description="Implement regex functions to match patterns using python")

    #argument for the file
    parser.add_argument("files", nargs="+", help="provide file to search")

    #argument for the regex pattern
    parser.add_argument("pattern", nargs=1, help="type regex pattern")

    #Call parse_args function on the parser and assign to args variable
    args = parser.parse_args()
    #print(args.files[0])
    #print(args.pattern[0])

    #read the file into memory
    with open(args.files[0]) as file:
        #iterate on the file object
        for line in file:
            #apply the regex pattern provided from command line look for a match
            s = re.search(args.pattern[0], line)
        print(s)

if __name__ == "__main__":
    main()
