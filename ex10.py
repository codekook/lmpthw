'''Implementing sort command'''

import sys, argparse, re, random

def main():
    #Check for minimum arguments
    if len(sys.argv) < 2:
        print("You must have at least one sort command")
        sys.exit()

    #Call parse_args
    args = parse_args()
    #print("args: ", args)

    if args.file == None:
        #if no file provided request string to sort
        text = input("What text do you want to sort? ")
        #if sort parsed, call the sort function
        if args.sort:
            #print("arg.sort: ", args.sort)
            sorted_text = sort(text)
            print("sorted_text: ", sorted_text)
        #if rsort parsed, call the reverse sort function
        if args.rsort:
            reverse_text = rsort(text)
            print("reverse_text: ", reverse_text)
        #if randsort parsed, call the randomize sort function
        if args.rand:
            random_text = randsort(text)
            print("random_text: ", random_text)
    #else if file is parsed, read it into memory
    else:
        #read file into memory
        with open(args.file[0], "r+", encoding="utf-8") as file:
            #if sort parsed, call the sort function
            if args.sort:
                sorted_text = sort(file.read())
                file.write(sorted_text)
            #if rsort parsed, call the reverse sort function
            if args.rsort:
                reverse_text = rsort(file.read())
                file.write(reverse_text)
            #if randsort parsed, call the randomize sort function
            if args.rand:
                random_text = randsort(file.read())
                file.write(random_text)

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

#Randomize sort function
def randsort(text):
    #split the text on spaces
    new_text = text.lower().split()
    #randomize the list of text
    random.shuffle(new_text)
    #join the text on spaces
    final_text = " ".join(new_text)
    return final_text

#Parse command line arguments
def parse_args():
    #Create the parser
    parser = argparse.ArgumentParser(description="Implement unix sort command to sort text alphabetically")
    #Add optional file argument
    parser.add_argument("-file", nargs="+", help="File to sort by line.  Type -file followed by the name of the file to sort")
    #Add optional sort argument
    parser.add_argument("-sort", action="store_true", help="Sort file alphabetically. Type -s followed by sort")
    #Add optional rsort argument
    parser.add_argument("-rsort", action="store_true", help="Reverse sort the words.  Type -r followed by rsort")
    #Add optional randsort argument
    parser.add_argument("-rand", action="store_true", help="Randomize the words.  Type -rand followed by randomize")
    #Return parsed arguments
    return parser.parse_args()

if __name__ == "__main__":
    main()
