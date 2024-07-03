divisor = int(input())
boundary = int(input())
# largest_number = 0
#
# for number in range(1, boundary + 1):
#     if number % divisor == 0:
#         largest_number = number

# for number in range(boundary, divisor - 1, -1):
#     if number % divisor == 0:
#         print(number)
#         break

largest_n = (boundary // divisor) * divisor
print(largest_n)