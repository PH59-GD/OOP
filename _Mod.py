import pickle

LBooks = []
LUser = []
LAuthor = []


class Book:
    def __init__(self):
        self.Book_ID = ""
        self.Book_title = ""
        self.Author_ID = ""
        self.Publisher = ""
        self.Year_of_publication = ""
        self.Checked_out = 0

    def Create_new_book(self):
        self.Book_ID = input("Book ID: ")
        self.Book_title = input("Book Title: ")
        self.Publisher = input("Book Publisher: ")
        self.Year_of_publication = input("Year of publication: ")

    def Assign_author(self):
        UC = input("Enter Author ID: ")
        for i in range(len(LAuthor)):
            if UC == LAuthor[i].AuthorID:
                self.Author_ID = LAuthor[i].AuthorID

    def Display_book(self):
        print("Book Title:", self.Book_title)
        print("Book ID:", self.Book_ID)
        print("Book Author ID:", self.Author_ID)
        print("Book Publisher:", self.Publisher)
        print("Book year of publication:", self.Year_of_publication)
class Author:
    def __init__(self):
        self.Author_ID = ""
        self.Author_Name = ""
        self.Affiliation = ""
        self.Country = ""
        self.Phone = ""
        self.Email_ID = ""
        self.AuthoredB = []

    def Create_new_author(self):
        self.Author_ID = input("Author ID: ")
        self.Author_Name = input("Author name: ")
        self.Affiliation = input("Author Affiliation: ")
        self.Country = input("Country: ")
        self.Phone = input("Phone: ")
        self.Email_ID = input("Email ID: ")

    def Display_author(self):
        print("Author ID", self.Author_ID)
        print("Author Name", self.Author_Name)
        print("Author Affiliation", self.Affiliation)
        print("Country:", self.Country)
        print("Phone:", self.Phone)
        print("Email ID:", self.Email_ID)

    def Display_num_book_CO(self):
        print("Authored Books:", str(len(self.AuthoredB)))
        if len(self.AuthoredB) > 0:
            for i in range(len(self.AuthoredB)):
                for b in range(len(LBooks)):
                    if self.AuthoredB[i] == LBooks[i].Book_ID:
                        print("Title: " + LBooks[i].Book_title + " ID:" + LBooks[
                            i].Book_ID + " Number Checked out: " + str(LBooks[i].Checked_out))
class User:
    def __init__(self):
        self.User_ID = ""
        self.Name = ""
        self.Password = ""
        self.Address = ""
        self.Phone = ""
        self.Email_ID = ""
        self.Books_borrowed = []

    def Create_new_user(self):
        self.User_ID = input("User ID: ")
        self.Name = input("User's name: ")
        self.Password = input("Password: ")
        self.Phone = input("Phone: ")
        self.Email_ID = input("Email ID: ")

    def Display_user(self):
        print("User ID:", self.User_ID)
        print("User's Name:", self.Name)
        print("User's Password:", self.Password)
        print("Phone:", self.Phone)
        print("Email ID:", self.Email_ID)
        print("Books borrowed:", self.Books_borrowed)

    def Borrow_a_book(self):
        UC = input("Enter book ID: ")
        for i in range(len(LBooks)):
            if UC == LBooks[i].Book_ID:
                self.Books_borrowed.append(LBooks[i].Book_ID)
while True:
    print("")
    print("[1] Book")
    print("[2] User")
    print("[3] Author")
    print("[4] Exit")
    print("")
    UC = input("Input: ")
    if UC == "1":
        print("")
        print("[1] Add book")
        print("[2] Assign Author")
        print("[3] Display book")
        print("")
        UC = input("Input: ")
        if UC == "1":
            BookO = Book()
            BookO.Create_new_book()
            file1 = open("mybooks.dat", "ab")
            pickle.dump(BookO, file1)
            file1.close()
        if UC == "2":
            UC = input("Book ID: ")
            OC = input("Enter Author's ID: ")
            for i in range(len(LBooks)):
                if (UC == LBooks[i].Book_ID):
                    LBooks[i].Author_ID = OC
                    LAuthor[b].AuthoredB.append(LBooks[i].Book_ID)
        if UC == "3":
            file1 = open("mybooks.dat", "rb")
            while True:
                try:
                    data = pickle.load(file1)
                    print("")
                    print(data.Book_ID)
                    print(data.Book_title)
                    print(data.Author_ID)
                    print(data.Publisher)
                    print(data.Year_of_publication)
                    print(data.Checked_out)
                except(EOFError):
                    break
            file1.close()
    if UC == "2":
        print("")
        print("[1] Add User")
        print("[2] Display User")
        print("[3] Borrow a book")
        print("")
        UC = input("Input: ")
        if UC == "1":
            UserO = User()
            UserO.Create_new_user()
            file2 = open("myUsers.dat", "ab")
            pickle.dump(UserO, file2)
            file2.close()
        if UC == "2":
            file2 = open("myUsers.dat", "rb")
            while True:
                try:
                    data = pickle.load(file2)
                    print("")
                    print(data.User_ID)
                    print(data.Name)
                    print(data.Password)
                    print(data.Address)
                    print(data.Phone)
                    print(data.Email_ID)
                    print(data.Books_borrowed)
                except(EOFError):
                    break
            file2.close()
        if UC == "3":
            CB = input("Enter book ID: ")
            CU = input("Enter User ID: ")
            for i in range(len(LBooks)):
                if CB == LBooks[i].Book_ID:
                    pass
            for a in range(len(LUser)):
                if CU == LUser[a].User_ID:
                    LUser[a].Books_borrowed.append(LBooks[i].Book_ID)
                    LBooks[i].Checked_out += 1
    if UC == "3":
        print("")
        print("[1] Add Author")
        print("[2] Display Author")
        print("[3] Display Checked out books")
        print("")
        UC = input("Input: ")
        if UC == "1":
            AuthorO = Author()
            AuthorO.Create_new_author()
            file3 = open("myAuthors.dat", "ab")
            pickle.dump(AuthorO, file3)
            file3.close()
        if UC == "2":
            file3 = open("myAuthors.dat", "rb")
            while True:
                try:
                    data = pickle.load(file3)
                    print("")
                    print(data.Author_ID)
                    print(data.Author_Name)
                    print(data.Affiliation)
                    print(data.Country)
                    print(data.Phone)
                    print(data.Email_ID)
                    print(data.AuthoredB)
                except(EOFError):
                    break
            file3.close()
        if UC == "3":
            CA = input("Enter Author ID: ")
            for i in range(len(LAuthor)):
                if CA == LAuthor[i].Author_ID:
                    LAuthor[i].Display_num_book_CO()
    if UC == "4":
        break