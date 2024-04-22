import csv

class Book:
    genrename = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }
    
    def _init_(self, isbn, t, a, genrecode, ava):
        self.isbn = isbn
        self.t = t
        self.a = a
        self.genrecode = genrecode
        self.ava = ava
    
    def get_genre_name(self):
        return self.genrename.get(self.genrecode, "Invalid")

    def _str_(self):
        return f"ISBN: {self.isbn}, Title: {self.t}, Author: {self.a}, Genre Code: {self.genrecode}, Available: {self.ava}"

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.t

    def get_author(self):
        return self.a

    def get_genre_code(self):
        return self.genrecode

    def get_availability(self):
        return "Available" if self.ava else "Borrowed"

    def borrow_it(self):
        self.ava = False

    def return_it(self):
        self.ava = True




def load_books(booklist, csvpath):
    while True:
        try:
            with open(csvpath, 'r', newline='') as f:
                csvreader = csv.reader(f)
                next(csvreader)
                loaded_books = 0
                for row in csvreader:
                    if len(row) == 5:
                        isbn, t, a, genrecode, ava = row
                        genrecode = int(genrecode)
                        ava = ava.lower() == 'true'
                        booklist.append(Book(isbn, t, a, genrecode, ava))
                        loaded_books += 1
            print("Successfully loaded book catalog.")
            return loaded_books
        except FileNotFoundError:
            csvpath = input("File not found. Re-enter  file: ")
            continue
        except:
            print("Error .")
            return 0




def print_books(booklist):
    print("Print the catalog")
    print("ISBN".ljust(15), "Title".ljust(25), "Author".ljust(25), "Genre".ljust(20), "Availability".ljust(15))
    print("---------------- -------------------- ----------------------- -------------------------- -------------------- -----------------")
    for book in booklist:
        genrename = Book.genrename.get(book.get_genre_code(), "not known")
        print(book.isbn.ljust(15), book.t.ljust(25), book.a.ljust(25), genrename.ljust(20), book.get_availability().ljust(15))

def print_menu(menuheading, menuoptions):
    print(menuheading)
    print("===================================================================")
    for key, value in menuoptions.items():
        print(f"{key}: {value}")

 
    while True:
        u_input = input("Enter your selection: ")
        if u_input in menuoptions:
            return u_input
        if u_input == '2130':
            return u_input
        else :
            print("invalid option.") 
            if u_input in menuoptions: 
                return u_input