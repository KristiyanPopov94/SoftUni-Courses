strings_count = int(input())
# is_pure = True

for _ in range(strings_count):
    strings = input()

    # for char in strings:
    #     if char == ',' or \
    #             char == '.' or \
    #             char == '_':
    #         is_pure = False
    #
    # if is_pure:
    #     print(f'{strings} is pure.')
    # else:
    #     print(f'{strings} is not pure!')
    # is_pure = True

    if ',' in strings or \
            '.' in strings or \
            '_' in strings:
        print(f'{strings} is not pure!')
    else:
        print(f'{strings} is pure.')