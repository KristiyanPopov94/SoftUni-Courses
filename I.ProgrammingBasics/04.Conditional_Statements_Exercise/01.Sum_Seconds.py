first_competitor = int(input())
second_competitor = int(input())
third_competitor = int(input())

sum_of_seconds = first_competitor + second_competitor + third_competitor
minutes = sum_of_seconds // 60
seconds = sum_of_seconds % 60

# 1
# if sum_of_seconds % 60 < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')
# 2

print(f'{minutes}:{seconds:02d}')
