import math
from math import floor

processors_count_target = int(input())
workers_count = int(input())
working_days = int(input())

total_time_needed = processors_count_target * 3
total_hours_work_time = working_days * 8 * workers_count

processors_count = math.floor(total_hours_work_time / 3)
total_profit_target = processors_count_target * 110.10
actual_profit = processors_count * 110.10

if total_hours_work_time >= total_time_needed:
    extra_profit = actual_profit - total_profit_target
    print(f'Profit: -> {extra_profit:.2f} BGN')
else:
    profit_lost = total_profit_target - actual_profit
    print(f'Losses: -> {profit_lost:.2f} BGN')
