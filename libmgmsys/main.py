import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second


class Library:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "a+")

    def list_books(self):
        books_file = open(self.file_name, "r")
        if books_file.readlines() == []:
            print("There is no book in the library system!")
        else:
            books_file = open(self.file_name, "r")
            print("__________________________Books list__________________________\n")
            books_number = 0
            books_list = []
            author_list = []
            for line in books_file:
                books_list.append(line.strip().split(",")[0])
                author_list.append(line.strip().split(",")[1])
                books_number += 1

            books_dataframe = pd.DataFrame(data=books_list, index=np.arange(1, len(books_list) + 1),
                                           columns=["BOOK NAME"])
            books_dataframe["AUTHOR NAME"] = author_list
            print(books_dataframe, "\n")

    def add_book(self):
        print("___Book Adding Section___\n")
        title = input("Type the book title:")
        author = input("Type the book author:")
        release_year = input("Type the release year of the book:")
        page_num = input("Type the number of pages of the book:")
        genre = input("type the genre of the book (novel, science-fiction, fantastic, spor): ")
        new_book = f"{title},{author},{release_year},{page_num},{genre},{month}\n"
        books_file = open("books.txt", "a+")
        books_file.write(new_book)
        books_file.close()
        print(f"The book named {title} was saved to the system! ({hour}:{minute}:{second})\n")

    def remove_book(self):
        to_be_deleted_book_name = input("Type the name of the book you want to delete:")
        books_file = open(self.file_name, "r")
        books_list = []

        for line in books_file:
            books_list.append(line.strip().split(","))

        for i in range(len(books_list)):
            if books_list[i][0] == to_be_deleted_book_name:
                print(
                    f"The book named {books_list[i][0]} has been deleted from the system! ({hour}:{minute}:{second})\n")
                del books_list[i]
                break
        books_file.close()

        with open("books.txt", "w") as books_file:
            for book in books_list:
                book_info = ",".join(book) + "\n"
                books_file.write(book_info)

    def book_page_graph(self):
        books_file = open(self.file_name, "r")
        books_list = []

        for line in books_file:
            books_list.append(line.strip().split(","))

        numbers_of_pages = []
        for i in range(len(books_list)):
            numbers_of_pages.append(int(books_list[i][3]))

        pagenumber_data = pd.Series(numbers_of_pages)
        plt.hist(pagenumber_data, bins=30, range=(0, 1000), color="red", alpha=0.5)
        plt.xlabel("Number of Page")
        plt.ylabel("Amount")
        plt.title("Graph of Distribution of Number of Pages In Our Library's Book")
        plt.show()

    def book_genre_graph(self):
        books_file = open(self.file_name, "r")
        books_list = []

        for line in books_file:
            books_list.append(line.strip().split(","))

        genre_list = []
        for i in range(len(books_list)):
            genre_list.append(books_list[i][4])

        novel_amount = genre_list.count("novel")
        sci_fi_amount = genre_list.count("science-fiction")
        fantastic_amount = genre_list.count("fantastic")
        spor_amount = genre_list.count("spor")

        fixed_genre_amount_list = [novel_amount, sci_fi_amount, fantastic_amount, spor_amount]
        fixed_genre_list = ["Novel", "Science-Fiction", "Fantastic", "Spor"]
        plt.pie(fixed_genre_amount_list, labels=fixed_genre_list, autopct="%1.1f%%")
        plt.title("Book Genre Graph")
        plt.show()

    def saved_book_graph_by_month(self):
        books_file = open(self.file_name, "r")
        books_list = []
        month_list = []
        for line in books_file:
            books_list.append(line.strip().split(","))

        for i in range(len(books_list)):
            month_list.append(books_list[i][5])

        jan_saved_book_amount = month_list.count("1")
        feb_saved_book_amount = month_list.count("2")
        mar_saved_book_amount = month_list.count("3")
        apr_saved_book_amount = month_list.count("4")
        may_saved_book_amount = month_list.count("5")
        jun_saved_book_amount = month_list.count("6")
        jul_saved_book_amount = month_list.count("7")
        aug_saved_book_amount = month_list.count("8")
        sep_saved_book_amount = month_list.count("9")
        oct_saved_book_amount = month_list.count("10")
        nov_saved_book_amount = month_list.count("11")
        dec_saved_book_amount = month_list.count("12")

        saved_book_amount_list = [jan_saved_book_amount, feb_saved_book_amount, mar_saved_book_amount,
                                  apr_saved_book_amount, may_saved_book_amount,
                                  jun_saved_book_amount, jul_saved_book_amount, aug_saved_book_amount,
                                  sep_saved_book_amount, oct_saved_book_amount,
                                  nov_saved_book_amount, dec_saved_book_amount]

        plt.plot(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                 saved_book_amount_list,
                 c="g")
        plt.xlabel("Month")
        plt.ylabel("Book Amount")
        plt.title(f"Number of Books Registered in the Library System  ({day}.{month}.{year})")
        plt.show()

    def total_book_graph(self):
        books_file = open(self.file_name, "r")
        books_list = []
        month_list = []
        for line in books_file:
            books_list.append(line.strip().split(","))

        for i in range(len(books_list)):
            month_list.append(books_list[i][5])

        jan_book_amount = month_list.count("1")
        feb_book_amount = month_list.count("2") + jan_book_amount
        mar_book_amount = month_list.count("3") + feb_book_amount
        apr_book_amount = month_list.count("4") + mar_book_amount
        may_book_amount = month_list.count("5") + apr_book_amount
        jun_book_amount = month_list.count("6") + may_book_amount
        jul_book_amount = month_list.count("7") + jun_book_amount
        aug_book_amount = month_list.count("8") + jul_book_amount
        sep_book_amount = month_list.count("9") + aug_book_amount
        oct_book_amount = month_list.count("10") + sep_book_amount
        nov_book_amount = month_list.count("11") + oct_book_amount
        dec_book_amount = month_list.count("12") + nov_book_amount

        total_book_amount = [jan_book_amount, feb_book_amount, mar_book_amount, apr_book_amount, may_book_amount,
                             jun_book_amount, jul_book_amount, aug_book_amount,
                             sep_book_amount, oct_book_amount, nov_book_amount, dec_book_amount]

        plt.plot(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                 total_book_amount, c="b")
        plt.xlabel("Month")
        plt.ylabel("Book Amount")
        plt.title(f"The graph of total book amount ({year})")
        plt.show()

    def print_main_menu(self):
        print("_____Welcome to Library Management System____")
        print(f"        Date: {day}.{month}.{year}  Time: {hour}:{minute}          \n")
        print("*****MENU*****")
        print("1- List Books")
        print("2- Add Book")
        print("3- Remove Book")
        print("4- Statistics")
        print("Press \"Q\" for quit\n")

    def print_stat_menu(self):
        print("_____Welcome to Library Management System Statistic Section____\n")
        print("*****MENU*****")
        print("1- Graph of distribution of number of pages in our librarys book")
        print("2- Graph of books genre")
        print("3- Graph of Number of Books Registered in the Library System")
        print("4- Graph of total book amount")
        print("Press \"B\" for back to the main menu\n")


lib = Library("books.txt")

while True:
    lib.print_main_menu()
    prompt = input("Type the number of the operation you want to perform:\n")
    if prompt == "1":
        lib.list_books()
    elif prompt == "2":
        lib.add_book()
    elif prompt == "3":
        lib.remove_book()
    elif prompt == "4":
        lib.print_stat_menu()
        prompt2 = input("Type the number of the operation you want to perform:\n")
        if prompt2 == "1":
            lib.book_page_graph()
        elif prompt2 == "2":
            lib.book_genre_graph()
        elif prompt2 == "3":
            lib.saved_book_graph_by_month()
        elif prompt2 == "4":
            lib.total_book_graph()
        elif prompt2 == "B" or prompt2 == "b":
            lib.print_main_menu()

        else:
            print("İnvalid Number")

    elif prompt == "q" or prompt == "Q":
        print("you quit!")
        break
    else:
        print("invalid Number or value")
