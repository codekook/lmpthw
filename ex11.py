'''Implementing uniq command'''

import argparse, collections

def main():
    #call parseargs
    args = parse_args()
    print("args: ", args)

    #check if a document was provided
    if args.file:
        #read the file into memory
        with open(args.file[0], "r+", encoding="utf-8") as file:
            start = file.readlines()
            #call the unique function
            unique_line = sorted(uniq(start))
            #print(unique_line)
            #check if the count function was provided
            if args.count:
                #call the count function
                count_line = count(start)
                for i in  unique_line:
                    print(i)
                for j in count_line.values():
                    print(j)
    else:
        #request a list input
        list = input("What is the list to sort? ")
        #call sort function
        sorted_list = sort(list)
        #print(sorted_list)
        #check if the count function was provided
        if args.count:
            count_list = count(sorted_list)
            #print(count_list)
            unique_list = uniq(sorted_list)
            for i in unique_list:
                print(i)
            for j in count_list.values():
                print(j)
        else:
            #call the unique function
            unique_list = uniq(sorted_list)
            print(unique_list)

#sort function
def sort(list):
    new_list = sorted(list.split())
    return new_list

#uniq function
def uniq(list):
    #use list comprehension to convert the list to a set and create a new list
    unique_list = [i for i in set(list)]
    return unique_list

#count function
def count(list):
    return collections.Counter(list)

#argument parser
def parse_args():
    #create the parser
    parser = argparse.ArgumentParser(description="Implement unix uniq command to identify unique items in a list/array")

    #add optional file containing text
    parser.add_argument("-file", nargs="+", help="File to read line into a list and identify the unique lines.  Type -file followed by the name of the file to sort")

    #add optional count feature
    parser.add_argument("-count", action="store_true", help="count the number of times the item occured in the input")

    #return parsed arguments
    return parser.parse_args()


if __name__ == "__main__":
    main()
