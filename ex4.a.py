import sys

#argv command line arument
def hello():
    print("This is the name of the program:", sys.argv[0])
    #Check for two arguments
    if len(sys.argv) != 2:
        print("You must have 2 arguments")
        sys.exit()

    hello = ("hello, " + sys.argv[1])
    print(hello)

hello()
