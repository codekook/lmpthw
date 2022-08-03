'''Review'''

import sys, collections, re, argparse, random, os
from pathlib import Path

def main():
    #check for minimum arguments
    if len(sys.argv) < 2:
        print("You must have at least one document")
        sys.exit()

    args = parse_args()
    print("args: ", args)

    #check for a file input or command line input
    if args.file:
        #do stuff
    else:
        #do stuff

#uniq function
def uniq(list):
    #use list comprehension to convert the list to a set and create a new list
    return [i for i in set(list)]

#count function
def count(list):
    return collections.Counter(list)

#combine function
def combine(keys, values):
    #use dict comprehension to combine the count with the list
    return {keys[i] : values[i] for i in range(len(keys))}

#Sort function
def sort(text):
    #split the text on spaces and sort the list
    new_text = sorted(text.lower().split())
    #join the text with spaces
    final_text = " ".join(new_text)
    return final_text

#Reverse sort function
def rsort(text):
    #split the text on spaces and sort the reverse list
    new_text = sorted(text.lower().split(), reverse=True)
    #join the text on spaces
    final_text = " ".join(new_text)
    return final_text

#random sort function
def randsort(text):
    #split the text on spaces
    new_text = text.lower().split()
    #randomize the list of text
    random.shuffle(new_text)
    #join the text on spaces
    final_text = " ".join(new_text)
    return final_text

#substitute the replacement string for any instance of the regular expression in the pattern
def sed(pattern, repl, file):
    #search the list for a matching regex pattern and if there is a match substitute the repl text
    return re.sub(pattern, repl, file.read())

#cut function
def cut():
    #iterate on the file object
    for line in file:
        try:
            #cut on the delimiter based on the list provided
            cut = line.rstrip().split(args.delimeter[0])[args.list[0]]
            print(cut)
        except TypeError:
            "Delim error"

#grep function
def grep():
    #read the file into memory
    with open(args.files[0]) as file:
        #iterate on the file object
        for line in file:
            #apply the regex pattern provided from command line look for a match
            s = re.search(args.pattern[0], line)
        print(s)

#find function
def find():
    #Create a concrete path for the directory provided
    files = Path(args.directory[0])

    #If the optional argument is for name search
    if args.name:
        for file in files.rglob(args.name):
            print(file)
    #If the optional argument is to search for a type directory or type file
    elif args.type:
        if args.type not in ["d", "f"]:
            print(f"Unknown file: {args.type}")
            sys.exit()
        for file in files.rglob(args.name or "*"):
            if args.type == "d" and file.is_dir():
                print(file)
            elif args.type == "f" and file.is_file():
                print(file)

#cat function
def cat():
    #create a newfile
    newfile = open("new_document.txt", "w")
    #open and read each file from the command line
    for arg in args.cat:
        with open(arg, encoding="utf-8") as arg:
            read_data = arg.read()
            #write the contents of each argv to the newfile
            newfile.write(read_data)
            newfile.write("\n")
    arg.closed
    newfile.close()

def parse_args():
    #create an argparser to parse the command line arguments
    parser = argparse.ArgumentParser(description="Implement unix commands using python")

    #file argument
    parser.add_argument("-file", nargs="+", help="Type -file followed by the file to use")

    #count argument
    parser.add_argument("-count", action="store_true", help="count the number of times the item occured in the input")

    #sort argument
    parser.add_argument("-sort", action="store_true", help="Sort file alphabetically.")

    #rsort argument
    parser.add_argument("-rsort", action="store_true", help="Reverse sort the words.")

    #random sort argument
    parser.add_argument("-rand", action="store_true", help="Randomize the words.")

    #prints text to stdout
    parser.add_argument("-print", action="store_true", help="prints all the contents of a file to the standard output.")

    #cut argument
    parser.add_argument("-delimeter", type=str, nargs=1, help="cut the text using a delimeter to separate the data. Type -delimeter followed by the method for delimiting")

    #identify the list to be cut
    parser.add_argument("-list", type=int, nargs=1, help="identifies for the cut function where to cut. Type -list followed by the position to cut.")

    #search argument
    parser.add_argument("-search", nargs="+", help="Type -search followed by the file to search")

    #argument for the regex pattern to grep
    parser.add_argument("-regex", nargs=1, help="Type -regex followed by the regex pattern")

    #find argument
    parser.add_argument("-find", type=str, nargs="+", help="This should be the directory to search. Type -find, then '../' followed by the directory name")

    #filter to apply in the directory for the names of files
    parser.add_argument("-name", type=str, help="This is the name filter to apply.  Use -name followed by the file name to search for")

    #filter to apply in the directory for the type
    parser.add_argument("-type", type=str, help="This should be the filter to apply.  Use -type followed by a [d] or a [f] to find the subdirectories or file types")

    #cat argument
    parser.add_argument("-cat", nargs="+", help="Grabs all files.  Type -cat followed by the list of files to concatenate")

    #argument is the directory to search
    parser.add_argument("-directory", type=str, nargs="+", help="This should be the directory to search. Type '../' followed by the directory name")

    #Return parsed arguments
    return parser.parse_args()

if __name__ == "__main__":
    main()
