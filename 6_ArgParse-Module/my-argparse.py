import argparse
import sys  # for the custom exit codes

# Build the parser
parser = argparse.ArgumentParser(
    description='for learning the argparse module')  # we can add a description for this script
parser.add_argument('filename',
                    help='this arg for the filename to read')  # If -- is not specified then its a positional argument
parser.add_argument('--limit', '-l', type=int,
                    help='the number of lines to read')  # If -- is specified then its an optional argument
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

# Parse the arguments
args = parser.parse_args()

# Carry out the scripts (Read the file, reverse the contents and print)

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)  # here it returns the exit code as 1 - since the exception occured
else:
    with f:  # getting the filename from filename argument and open the file
        lines = f.readlines()  # reading all lines in the file
        lines.reverse()  # reversing the order of the line contents such as last line becoming first line
        if args.limit:  # If --limit argument is given then we are only reversing those lines
            lines = lines[:args.limit]
        for line in lines:
            print(line.strip()[::-1])  # reversing the characters in each line and printing
