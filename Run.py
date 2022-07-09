from Coding import libraryms
library = libraryms("bookcollection.txt", "lendercollection.txt", "clover")
while(True):
    try:
        print("Welcome to the", library.name, "library. Please choose the following option.")
        print("1", "display_books")
        print("2", "display_lenders")
        print("3", "lend_book")
        print("4", "return_book")

        user_choice = input()
        if user_choice not in ["1","2","3","4"]:
            print("Please, choose wisely. \n")
            continue
        else:
            user_choice = int(user_choice)
            if user_choice == 1:
                print("Following books are available in our library.")
                library.display_books()
                print("\n")

            elif user_choice == 2:
                print("Following are the list of the lenders.")
                library.display_lenders()
                print("\n")

            elif user_choice == 3:
                library.lend_book()
                print("\n")

            elif user_choice == 4:
                book = input("Please, enter the name of the book you want to return:")
                user = input("Please, enter your name: ")
                library.return_book(book,user)
                print("\n")


            else:
                print("Not a valid option")

            print("Please,press q to quit or c to continue")
            choice = ""
            while(choice!= "c" and choice != "q"):
                choice = input()
                if choice == "c":
                    continue
                elif choice == "q":
                    exit()
    except:
        print("Invalid Input!!")
        continue
