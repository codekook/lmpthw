'''Implementing argv'''

import sys

def main():
    print("This is the name of the program:", sys.argv[0])
    #Check for two arguments
    if len(sys.argv) != 2:
        print("You must have 2 arguments")
        sys.exit()

    print(hello())

#argv command line arument
def hello():
    hello = ("hello, " + sys.argv[1])
    return hello

if __name__ == "__main__":
    main()
