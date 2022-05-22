import sys, argparse

def doc_reader():
    #Check for two arguments
    if len(sys.argv) < 2:
        print("You must have at least one document")
        sys.exit()

    #create a newfile
    newfile = open("new_document.txt", "w")

    #open and read each file from the command line
    for doc in sys.argv[1:]:
        with open(doc, encoding="utf-8") as doc:
            read_data = doc.read()
            #write the contents of each argv to the newfile
            newfile.write(read_data)
            newfile.write("\n")
    doc.closed
    newfile.close()

#doc_reader()

'''Refactored with argparse'''
def doc_reader2():
    #Check for two arguments
    if len(sys.argv) < 2:
        print("You must have at least one document")
        sys.exit()

    #Create the parser object
    parser = argparse.ArgumentParser(description="Create cat-style python application")

    #Add the arguments
    parser.add_argument("files", nargs="+", help="Grabs all files")

    #create a newfile
    newfile = open("new_document.txt", "w")

    #Call parse_args function on the parser and assign to args variable
    args = parser.parse_args()

    #open and read each file from the command line
    for arg in args.files:
            with open(arg, encoding="utf-8") as arg:
                read_data = arg.read()
                #write the contents of each argv to the newfile
                newfile.write(read_data)
                newfile.write("\n")
    arg.closed
    newfile.close()

doc_reader2()
