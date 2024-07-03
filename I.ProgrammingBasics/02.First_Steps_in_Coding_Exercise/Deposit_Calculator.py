deposit = float(input())
period = int(input())
increase = float(input()) / 100

finalSum = deposit + period * ((deposit * increase) / 12)

print(finalSum)