'''Implementing find'''

import os, argparse, sys
from pathlib import Path

def main():
    #Check for at least two arguments (file name and directory to search)
    if len(sys.argv) < 2:
        print("You must have at least one directory to search")
        sys.exit()

    #Create the parser object
    parser = argparse.ArgumentParser(description="Implement Unix-style find function in python")

    #First argument is the directory to search
    parser.add_argument("directory", type=str, nargs="+", help="This should be the directory to search. Type '../' followed by the directory name")

    #Optional argument is a filter to apply in the directory for the names of files
    parser.add_argument("--name", type=str, help="This is the name filter to apply.  Use --name followed by the file name to search for")

    #Optional argument is a filter to apply in the directory for the type
    parser.add_argument("--type", type=str, help="This should be the filter to apply.  Use ---type followed by a [d] or a [f] to find the subdirectories or file types")

    #Call parse_args function on the parser and assign to args variable
    args = parser.parse_args()

    #Create a concrete path for the directory provided
    files = Path(args.directory[0])

    #If the optional argument is for name search
    if args.name:
        for file in files.rglob(args.name):
            print(file)
    #If the optonal argument is to search for a type directory or type file
    elif args.type:
        if args.type not in ["d", "f"]:
            print(f"Unknown file: {args.type}")
            sys.exit()
        for file in files.rglob(args.name or "*"):
            if args.type == "d" and file.is_dir():
                print(file)
            elif args.type == "f" and file.is_file():
                print(file)
    else:
        print("You need either --name or --type")
        sys.exit(1)

if __name__ == "__main__":
    main()
