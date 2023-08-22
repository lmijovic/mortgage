import mortgage
import argparse
import os

default_amount = 300000.
default_rate = 0.05
default_years = 30
default_term = 0
# booking fee
default_arr = -1.

parser = argparse.ArgumentParser(description="",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--amount", default=default_amount, help="amount ", type = float, dest="amount")
parser.add_argument("--rate", default=default_rate, help="rate ", type = float, dest="rate")
parser.add_argument("--years", default=default_years, help="years ", type = int, dest="years")
parser.add_argument("--term", default=default_term, help="term ", type = int, dest="term")
parser.add_argument("--arr", default=default_arr, help="arr ", type = float, dest="arr")

args = parser.parse_args()

## here arg name is identical to destination 
print("\nExample command:\n")
command = "python " + os.path.basename(__file__)
for var in vars(args):
    command += " --"+var
    command += "="+str(vars(args)[var])
print(command)
print("\n")

amount = vars(args)["amount"]
rate = vars(args)["rate"]
years = vars(args)["years"]
term = vars(args)["term"]
arr = vars(args)["arr"]


m=mortgage.Mortgage(interest=rate, amount=amount, months=years*12, term_years = term, arrangement=arr)

mortgage.print_summary(m)
