start_of_first_loop = int(input())
start_of__second_loop = int(input())
difference_for_first_pair = int(input())
difference_for_second_pair = int(input())

for first_pair in range(start_of_first_loop, (start_of_first_loop + difference_for_first_pair + 1)):
    if first_pair > 1:
        for i in range(2, first_pair // 2):
            if first_pair % i == 0:
                break
        else:
            for second_pair in range(start_of__second_loop, (start_of__second_loop + difference_for_second_pair + 1)):
                if second_pair > 1:
                    for i in range(2, second_pair // 2):
                        if second_pair % i == 0:
                            break
                    else:
                        print(f'{first_pair}{second_pair}')