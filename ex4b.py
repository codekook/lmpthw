import argparse

def main():
    hello()

#argparse command line argument
def hello():
    #Create the parser object
    parser = argparse.ArgumentParser(description="Say hello to the user using the Command Line.")

    #Add the arguments
    parser.add_argument("greeting", type=str, nargs="?", help="Type hello", default="hello, ")
    parser.add_argument("name", type=str, nargs="?", help="This should be your name", default="world")
    parser.add_argument("-age", type=int, nargs="?", help="Type -age and then add your age")
    parser.add_argument("-gender", type=str, nargs="?", help="Type -gender and then add male or female", choices=["male", "female"])
    parser.add_argument("-eyecolor", type=str, nargs="?", help="Type -eyecolor and then add blue, brown, or green", choices=["blue", "brown", "green"])
    parser.add_argument("-t", action="store_true", help="Type -t to store True")
    parser.add_argument("-f", action="store_false", help="Type -f to store False")

    #Call parse_args function on the parser and assign to args variable
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
