import sys 
import argparse

def claculator(args):
    ''' command line ulitily function it is run in command
    '''
    if args.num1 == 45 and args.num2 == 3 and args.num3 == "*":
        return "777"
    elif args.num1 == 56 and args.num2 == 9 and args.num3 == "+":
        return "77"
    elif args.num1 == 56 and args.num2 == 6 and args.num3 == "/":
        return "4"
    elif args.num3 == "+":
        add = args.num1 + args.num2
        return add
    elif args.num3 == "-":
        subs = args.num1 - args.num2
        return subs
    elif args.num3 == "*":
        multiply = args.num1 * args.num2
        return multiply

    elif args.num3 == "/":
        divide = args.num1 / args.num2
        print(divide)
    elif args.num3 == "%":
        percent = args.num1 % args.num2
        print(percent)

    else:
        print("plaese try again ")



if __name__ == '__main__': #main function
    parser = argparse.ArgumentParser() #create a ojject of argument parser
    parser.add_argument("--num1", type=int, default=5, help="enter firist number")# add  firist number  
    parser.add_argument("--num2", type=int, default=10, help="enter firist number") # add second number into parser         
    parser.add_argument("--num3", type=str, default='+', help="enter firist number")# add third number in  pasers
    args = parser.parse_args()
    sys.stdout.write(str(claculator(args)))
