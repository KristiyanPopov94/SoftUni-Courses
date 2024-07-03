budget = float(input())
GPUs = int(input())
CPUs = int(input())
RAMs = int(input())

GPU_price = GPUs * 250
CPU_price = CPUs * (GPU_price * 0.35)
RAM_price = RAMs * (GPU_price * 0.10)

total_price = GPU_price + CPU_price + RAM_price

if GPUs > CPUs:
    total_price = total_price * 0.85

if budget >= total_price:
    print(f'You have {(budget - total_price):.2f} leva left!')
else:
    print(f'Not enough money! You need {(total_price - budget):.2f} leva more!')
