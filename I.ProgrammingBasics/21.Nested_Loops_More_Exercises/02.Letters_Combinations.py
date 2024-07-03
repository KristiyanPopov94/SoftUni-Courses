start_of_loop = input()
end_of_loop = input()
letter_to_pass = input()
combinations_count = 0

for a in range(ord(start_of_loop), ord(end_of_loop) + 1):
    for b in range(ord(start_of_loop), ord(end_of_loop) + 1):
        for c in range(ord(start_of_loop), ord(end_of_loop) + 1):
            if a == ord(letter_to_pass) or b == ord(letter_to_pass) or c == ord(letter_to_pass):
                continue
            else:
                combinations_count += 1
                print(chr(a) + chr(b) + chr(c), end=' ')

print(combinations_count)