def main():
    print('System starting')
    csvpath = input("Enter the file: ")
    booklist = []
    books_loaded = load_books(booklist, csvpath)
    if books_loaded > 0:
        menuoptions = {
            '1': 'Search for books',
            '2': 'Borrow a book',
            '3': 'Return a book',
            '0': 'Exit the system',
    
        }

        choice = ''
        while choice != '0':
            choice = print_menu("\nReader's Guild Library - Main Menu", menuoptions)

            if choice == '1':
                print("\nsearch for book")
                search_string = input("Enter value: ")
                search_result = search_books(booklist, search_string)
                if search_result:
                    print_books(search_result)
                else:
                    print("No book found.")
            elif choice == '2':
                print("\nBorrow a book")
                borrow_book(booklist)
            elif choice == '3':
                print("\nReturn a book")
                return_book(booklist)
            elif choice == '2130':
                extentedmenu = {
                    '1': 'Search for books',
                    '2': 'Borrow a book',
                    '3': 'Return a book',
                    '4': 'Add book',
                    '5': 'Remove book',
                    '6': 'Print all books',
                    '0': 'Exit the system',
                }
                while choice != '0':
                    choice = print_menu("\nReader's Guild Library - Librarian Menu", extentedmenu)

                    if choice == '1':
                        print("\nsearch for book")
                        search_string = input("Enter search query: ")
                        search_result = search_books(booklist, search_string)
                        if search_result:
                            print_books(search_result)
                        else:
                            print("No book found.")
                    elif choice == '2':
                        print("\nBorrow a book")
                        borrow_book(booklist)
                    elif choice == '3':
                        print("\nReturn a book")
                        return_book(booklist)
                    elif choice == '4':
                        print("\nAdd a book")
                        add_book(booklist)
                    elif choice == '5':
                        print("\nRemove a book")
                        remove_book(booklist)
                    elif choice == '6':
                        print("\nPrint books")
                        print_books(booklist)
                    elif choice== '0':
                        print("\nExit the system")
                        print("Book catalog saved.")
                        print("Good Bye")
                        exit()

                
                choice = ''

        
        with open(csvpath, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["ISBN", "Title", "Author", "Genre Code", "Available"])
            for book in booklist:
                csv_writer.writerow([book.isbn, book.t, book.a, book.genrecode, book.ava])
        
        print("\nExit the system")
        print(" saved.")
        print("Good Bye!")

if __name__ == "__main__":
    main()