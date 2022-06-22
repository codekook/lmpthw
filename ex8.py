'''Implement Unix Command Cut'''

import sys, argparse

def main():
    #check for a file and cut selections for each line in the command line
    if len(sys.argv) < 3:
        print("You must have at least one [delimeter] option, [list], and file")
        sys.exit()

    args = parse_args()
    print(args)
    #read file into memory
    with open(args.file[0]) as file:
        #iterate on the file object
        for line in file:
            #cut on the delimiter based on the list provided
            try:
                #cut for as long as the list
                cut = line.rstrip().split(args.delimeter[0])[args.list[0]]
                print(cut)
            except TypeError:
                "Delim error"

def parse_args():
    #create an argparser to parse the command line arguments
    parser = argparse.ArgumentParser(description="Implement unix cut command to splice text using python")

    #accept delimiter in command line
    parser.add_argument("-delimeter", type=str, nargs=1, help="cut the text using a delimeter to separate the data. Type -delimeter followed by the method for delimiting")

    #identify the list to be cut
    parser.add_argument("-list", type=int, nargs=1, help="identifies for the cut function where to cut. Type -list followed by the position to cut.")

    #argument for the file
    parser.add_argument("file", nargs="+", help="file used for the cut function")

    #call parse_args function on the parser and assign to args variable
    return parser.parse_args()

if __name__ == "__main__":
    main()
