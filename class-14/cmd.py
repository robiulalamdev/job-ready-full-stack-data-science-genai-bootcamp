# Command line tool
import sys
import argparse



def calculator(args):
    if args.operation == "add":
        print(args.num1 + args.num2)
    elif args.operation == "sub":
        print(args.num1 - args.num2)
    elif args.operation == "mul":
        print(args.num1 * args.num2)
    elif args.operation == "div":
        if args.num2 == 0:
            print("Cannot divide by zero")
        else:
            print(args.num1 / args.num2)
    else:
        print("Invalid operation")




parser = argparse.ArgumentParser(description="Calculator")
parser.add_argument("--operation", type=str, help="Operation to perform")
parser.add_argument("--num1", type=int, help="First number")
parser.add_argument("--num2", type=int, help="Second number")

# calling the function

args = parser.parse_args()
sys.stdout.write(str(calculator(args)))


