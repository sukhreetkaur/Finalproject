#Jawad Latif Part1
import csv

class Book:
    def __init__(self, ISBN, t, a, genrecode, ava):
        self.ISBN = ISBN
        self.t = t
        self.a = a
        self.genrecode = genrecode
        self.ava = ava

    def __str__(self):
        return f"ISBN: {self.ISBN}, title: {self.t}, author: {self.a}, genre code: {self.genrecode}, available: {self.ava}"

    def get_isbn(self):
        return self.ISBN

    def get_title(self):
        return self.t

    def get_author(self):
        return self.a

    def get_genre_code(self):
        return self.genrecode

    def get_availability(self):
        return "It is Available" if self.ava else "It is Borrowed"

    def borrow_it(self):
        self.ava = False

    def return_it(self):
        self.ava = True

def load_books(booklist, csv_path):
    try:
        with open(csv_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  
            for row in csv_reader:
                ISBN, t, a, genrecode, ava = row
                genrecode = int(genrecode)  
                ava = ava.lower() == 'True' 
                booklist.append(Book(ISBN, t, a, genrecode, ava))
        return len(booklist)
    except FileNotFoundError:
        print("Error.")
        return 0

def print_books(booklist):
    
    print("Printing book catalog")
    print("ISBN".ljust(15), "Title".ljust(25), "Author".ljust(25), "Genre".ljust(20), "Availability".ljust(15))
    print("---------------------------------------------------------------------------------------------------------")
    for book in booklist:
        print(book.ISBN.ljust(15), book.t.ljust(25), book.a.ljust(25), str(book.get_genre_code()).ljust(20), book.get_availability().ljust(12))

def print_menu(menu_heading, menu_options):
    print(menu_heading)
    for key, value in menu_options.items():
        print(f"{key}: {value}")

    u_input = input("Enter your choice: ")
    return u_input