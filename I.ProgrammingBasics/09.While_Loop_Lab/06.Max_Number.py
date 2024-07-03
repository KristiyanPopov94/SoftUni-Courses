import sys

max_number = -sys.maxsize

variable = input()

while variable != 'Stop':

    if max_number < int(variable):
        max_number = int(variable)

    variable = input()

print(max_number)
