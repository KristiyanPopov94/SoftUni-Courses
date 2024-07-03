import sys

min_number = sys.maxsize

variable = input()

while variable != 'Stop':

    if min_number > int(variable):
        min_number = int(variable)

    variable = input()

print(min_number)
