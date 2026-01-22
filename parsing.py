import argparse
parsing = argparse.ArgumentParser()
parsing.add_argument( '-n','--numbers', type=float, help='The greeting message should not be displayed')

args = parsing.parse_args()

print(args.numbers)