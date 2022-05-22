import sys

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

doc_reader()
