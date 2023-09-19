book_needed = input()

search_count = 0

while True:
    book_found = input()

    if book_found == book_needed:
        print(f"You checked {search_count} books and found it.")
        break
    elif book_found == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {search_count} books.")
        break

    search_count += 1