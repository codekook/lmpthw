'''Implement Unix Command Cut'''

import sys, argparse

def main():
    #check for a file and cut selections for each line in the command line
    if len(sys.argv) < 3:
        print("You must have at least one [cut] option, [list], and file")
        sys.exit()

    #create an argparser to parse the command line arguments
    parser = argparse.ArgumentParser(description="Implement unix cut command to splice text using python")

    #accept delimiter in command line
    parser.add_argument("-delimeter", type=str, nargs=1, help="cut the text using a delimeter to separate the data. Type -delimeter followed by the method for delimiting")

    #accept fields in command line
    parser.add_argument("-field", type=str, nargs=1, help="cut the text using fields and must accompany the delimeter")

    #accept optionnal characters in command line
    parser.add_argument("-char", type=str, nargs=1, help="cut the text using characters")

    #identify the list to be cut
    parser.add_argument("-list", type=int, nargs=1, help="identifies for the cut function where to cut. Type -list followed by the position to cut.  Accompanies -field or -char arguments")

    #argument for the file
    parser.add_argument("file", nargs="+", help="file used for the cut function")

    #call parse_args function on the parser and assign to args variable
    args = parser.parse_args()
    print(args)

    #read file into memory
    with open(args.file[0]) as file:
        #iterate on the file object
        for line in file:
            #if args has a delimeter provided, cut on the delimiter using the list provided
            #if hasattr(args, "delimeter") == True:
            if args.delimeter[0]:
                #cut for as long as the list
                cut = line.rstrip().split(args.delimeter[0])[args.list[0]]
                print(cut)

            #if -f provided, cut on the field provided
            elif args.field[0]:
                #cut for as long as the field
                cut = line.rstrip().split(args.delimeter[0])
                print(cut)

            #if -c provided, cut at the character provided
            elif args.char[0] in args:
                #cut on the character provided and maxsplit for as long as the list provided 
                cut = line.rstrip().rsplit(args.char[0], args.list[0])
                print(cut)

if __name__ == "__main__":
    main()
