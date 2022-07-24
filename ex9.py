'''Implmenting sed command'''

import sys, argparse, re

def main():
    #check for a file and cut selections for each line in the command line
    if len(sys.argv) < 2:
        print("You must have at least one file to search")
        sys.exit()

    args = parse_args()
    print("args: ", args)

    #request regex pattern from user
    pattern = input("What's the regex pattern to search? ")
    repl = input("What's the new text? ")

    #read file into memory
    with open(args.file[0], "r+", encoding="utf-8") as file:
        new_text = sed(pattern, repl, file)
        #write the new_text into the file
        file.write(new_text)

    if args.print:
        print(new_text)

#substitute the replacement string for any instance of the regular expression in the pattern
def sed(pattern, repl, file):
    #search the list for a matching regex pattern and if there is a match substitute the repl text
    return re.sub(pattern, repl, file.read())

def parse_args():

    #create an argparser to parse the command line arguments
    parser = argparse.ArgumentParser(description="Implement unix sed command to subtitute text using python")

    #argument for the file
    parser.add_argument("file", nargs="+", help="file(s) used for the sed function")

    #optionally prints text to stdout
    parser.add_argument("-print", action="store_true", help="prints all the contents of a file to the standard output.")

    #return parsed arguments
    return parser.parse_args()

if __name__ == "__main__":
    main()
