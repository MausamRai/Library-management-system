import coding1
import os
from datetime import date, timedelta, time, datetime

class libraryms:
    def __init__(self, book,lender, name):
        self.book = book
        self.lender = lender
        self.name = name
        self.bookdictionary = {}
        self.lenderdictionary = {}
        self.booklists = []
        self.lenderlists = []


    def display_books(self):
        bookcollection = open(self.book)
        for books in bookcollection:
            line = books.strip()
            word = line.split("\t")
            self.booklists.append(word)
        bookcollection.close()
        for i in range(len(self.booklists)):
            self.bookdictionary.update({self.booklists[i][0]:[self.booklists[i][1], int(self.booklists[i][2]), self.booklists[i][3]]})

        x = open(self.book)
        line1 = x.readlines()
        print("book", "\t\t\t", "author","\t", "quantity", "price") 
        for j in line1:
            print(j)
        x.close()

    def display_lenders(self):
        lendercollection = open(self.lender)
        for lenders in lendercollection:
            line = lenders.strip()
            word = line.split("\t")
            self.lenderlists.append(word)
        lendercollection.close()

        for i in range(len(self.lenderlists)):
            self.lenderdictionary.update({(self.lenderlists[i][0], self.lenderlists[i][1]): self.lenderlists[i][2]})

        x = open(self.lender)
        line1 = x.readlines()
        for j in line1:
            print(j)
        x.close()
        


    def lend_book(self):
        listi = []
        s = "1"
        check = 0
        sum = 0
        while (s == "1"):
            while True:
                try:
                    book = input("Please, Enter the name of the book you want to borrow:")
                    break
                except:
                    print("The book you are looking for is not available in our library!!")
            if check == 0:
                name = input("Please, Enter your name: ")
            bookcollection = open(self.book)
            for books in bookcollection:
                line = books.strip()
                word = line.split("\t")
                self.booklists.append(word)
            bookcollection.close()
            for i in range(len(self.booklists)):
                self.bookdictionary.update({self.booklists[i][0]:[self.booklists[i][1], int(self.booklists[i][2]), self.booklists[i][3]]})
            price = int(self.bookdictionary[book][2])
            if book in self.bookdictionary.keys():
                if self.bookdictionary[book][1]>=1:
                    lend_date = coding1.getDate()
                    lend_time = coding1.time()
                    return_date = lend_date+ timedelta(days = 10)
                    with open(self.lender, "a") as a:
                        a.writelines(book+"\t"+name+"\t"+str(return_date)+"\n")
                    self.lenderdictionary.update({(book, name):return_date})
                    filelender = os.path.abspath("lenderlist/lender("+name+").txt")
                    with open(filelender, "a") as x:
                        if check == 0:
                            x.writelines("lenddate= "+str(lend_date) +str(lend_time)+"\n")
                            x.writelines("name = "+str(name)+"\n")
                        x.writelines("book =" +str(book)+"\n")
                        x.writelines("price =" +str(price)+"\n")
                        sum += price
                    listi = self.bookdictionary.get(book)
                    self.bookdictionary[book][1] = int(self.bookdictionary[book][1])
                    self.bookdictionary[book][1] -= 1
                    self.bookdictionary[book] = listi
                    b = open(self.book, "w")
                    b.close()
                    with open(self.book, "w") as c:
                        for key, value in self.bookdictionary.items():
                            c.write(key+"\t"+value[0]+"\t"+str(value[1])+"\t"+str(value[2])+"\n")
                    print("The book has been issued to your name.", name)
                    print("Please return book within 10 days.Thank You!")
                else:
                    print("Sorry, The book you are looking for is out of stock.")
            else:
                print("Sorry, The book you are looking for is not available in our library. ")
            s = input("Please, press 1 to borrow another book.")
            check = 1
            with open(filelender, "a") as z:
                z.write(" total = "+str(sum)+ "\n")
        while (s != 1):
            print("The book has been lended to you, Thank You!!")
            break



    def return_book(self, book, user):
        listi = []
        filereturner = os.path.abspath("returnerlist/returned_by("+user+").txt")
        lendercollection = open(self.lender)
        for lenders in lendercollection:
            line = lenders.strip()
            word = line.split("\t")
            self.lenderlists.append(word)
        lendercollection.close()
        
        for i in range(len(self.lenderlists)):
            self.lenderdictionary.update({(self.lenderlists[i][0], self.lenderlists[i][1]): self.lenderlists[i][2]})
            
        if (book,user)in self.lenderdictionary.keys():
            return_date = self.lenderdictionary[(book,user)]
            return_date1 = datetime.strptime(return_date,"%Y-%m-%d")
            return_date2 = return_date1.date()
            current_date = coding1.getDate()
            current_time = coding1.time()
            if current_date > return_date2:
                delay_days = (current_date - return_date2).days
                total_fine = delay_days*10
                print("Please pay your fine, you were late in returning the book so you have to pay rupees-", total_fine)
                print("Please wait, while we rediract you to payment page")
                self.payment(book,user)
            else:
                with open(filereturner, "a") as x:
                    x.writelines("return_date =" +str(current_date)+ str(current_time)+"\n")
                    x.writelines("name = "+str(user)+"\n")
                    x.writelines("book = "+book+"\n")
                self.lenderdictionary.pop((book, user))
                x=open(self.lender, "w")
                x.close()
                with open(self.lender, "w") as y:
                   for key, value in self.lenderdictionary.items():
                       y.write(f"{key[0]}\t{key[1]}\t{value}\n")
                bookcollection = open(self.book)
                for books in bookcollection:
                    line = books.strip()
                    word = line.split("\t")
                    self.booklists.append(word)
                bookcollection.close()
                for i in range(len(self.booklists)):
                    self.bookdictionary.update({self.booklists[i][0]:[self.booklists[i][1], int(self.booklists[i][2]), self.booklists[i][3]]})        
                listi = self.bookdictionary.get(book)
                listi[1] += 1
                self.bookdictionary[book] = listi
                x = open(self.book, "w")
                x.close()
                with open (self.book, "w") as y:
                    for key, value in self.bookdictionary.items():
                        y.write(key+"\t"+value[0]+"\t"+str(value[1])+"\t"+str(value[2])+"\n")
                    print("The book has been returned successfully. Thank You for choosing us. ")
        else:
            print("Please, Enter correct username and book name")



    def payment(self, book, user):
        listi = []
        filereturner = os.path.abspath("returnerlist/returned_by("+user+").txt")
        print("for payment process. Enter your choice ")
        choice = input("yes/no")
        if choice == "yes":
            print("your payment is processing")
            print("payment successful")
            return_date = self.lenderdictionary[(book,user)]
            return_date1 = datetime.strptime(return_date,"%Y-%m-%d")
            return_date2 = return_date1.date()
            current_date = coding1.getDate()
            current_time = coding1.time()
            delay_days = (current_date - return_date2).days
            total_fine = delay_days*10
            with open(filereturner, "a") as x:
                x.writelines(f"return_date = {current_date} {current_time}\n")
                x.writelines(f"name = {user}\n")
                x.writelines(f"book = {book}\n")
                x.writelines(f"fine = {total_fine}\n")
            self.lenderdictionary.pop((book, user))
            x = open(self.lender, "w")
            x.close()
            with open (self.lender, "w") as y:
                for key, value in self.lenderdictionary.items():
                    y.write(f"{key[0]}\t{key[1]}\t{value}\n")
            bookcollection = open(self.book)
            for books in bookcollection:
                line = books.strip()
                word = line.split("\t")
                self.booklists.append(word)
            bookcollection.close()
            for i in range(len(self.booklists)):
                self.bookdictionary.update({self.booklists[i][0]:[self.booklists[i][1], int(self.booklists[i][2]), self.booklists[i][3]]})
            listi = self.bookdictionary.get(book)
            listi[1] += 1
            self.bookdictionary[book] = listi
            x = open(self.book, "w")
            x.close()
            with open (self.book, "w") as y:
                for key, value in self.bookdictionary.items():
                    y.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\n")
            print("book has been returned")
        else:
            print("we are redirecting you to homepage")




        
