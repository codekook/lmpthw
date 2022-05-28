import os, argparse, sys
from pathlib import Path

def main():
    #Check for at least two arguments (file name and directory to search)
    if len(sys.argv) < 2:
        print("You must have at least one directory to search")
        sys.exit()

    #Create the parser object
    parser = argparse.ArgumentParser(description="Implement Unix-style find function a python application")

    #First argument is the directory to search
    parser.add_argument("directory", type=str, nargs=1, help="This should be the directory to search")

    #Second argument is a filter to apply in the directory
    parser.add_argument("-filter", type=str, nargs="?", help="This should be the filter to apply.  Type -filter and then type the filter name")

    #Call parse_args function on the parser and assign to args variable
    args = parser.parse_args()
    print(args)

    #Print a list of each file found in the directory that meets the filter argument
    files = sorted(Path(args.directory[0]).rglob("*.py"))
    print(files)

if __name__ == "__main__":
    main()
