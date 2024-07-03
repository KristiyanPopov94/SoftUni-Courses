preferred_book = input()
checked_books = 0
book_found = False

while True:
    new_book = input()

    if new_book == preferred_book:
        book_found = True
        break
    elif new_book == 'No More Books':
        break

    checked_books += 1

if book_found:
    print(f'You checked {checked_books} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {checked_books} books.')
