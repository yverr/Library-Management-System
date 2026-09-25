# ! ADDITIONAL FEATURES TO BE ADDED
# add status on members and borrowed books
# add time limit on borrowed books fine fees


class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    YELLOW = '\033[33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

green = bcolors.OKGREEN
end = bcolors.ENDC
yellow = bcolors.YELLOW
fail = bcolors.FAIL

members = []
borrowed_books = []

# the books list 
books = [
    {
    "id": 1,
    "title": "Lord of Mysteries",
    "author": "Cuttlefish That Loves Diving",
    "available": True
},
{
    "id": 2,
    "title": "Omniscient Reader's Viewpoint",
    "author": "Sing Shong",
    "available": True
},
{
    "id": 3,
    "title": "Reverend Insanity",
    "author": "Gu Zhen Ren",
    "available": True
}
]

def exit_program():
    print(green + "\nPress any key to return to the main menu." + end)
    input()

def view_rules():
    print(green + "\n----------- RULES -----------" + end)

    exit_program()

# add book function
def add_book():
    print("")
    print(green + "----------- ADD BOOK -----------" + end)
    
    book_id = len(books) + 1
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    
    books.append(new_book)
    print(yellow + f"\nBook '{title}' added successfully!" + end)
    
    exit_program()
    
def view_books():
    print("==== View Books ====")
    
    if len(books) == 0:
        print(fail + "\nNo books available." + end)
        return
    
    for book in books:
        print("----------------")
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {'Available' if book['available'] else 'Not Available'}")
    print("-----------------------------------")
    
    exit_program()
    
def search_book():
    print(green + "\n----------- Search Book -----------" + end)
    
    search_title = input("Enter book title: ")
    
    found = False
    for book in books:
        if book['title'].lower() == search_title.lower():
            print("----------------")
            print(f"ID: {book['id']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Status: {'Available' if book['available'] else 'Not Available'}")
            found = True
        
    if not found:
        print(fail + "Book not found." + end)
    print(green +"-----------------------------------" + end)
    
    exit_program()    
        
def remove_book():
    print("==== Remove Book ====")
    
    book_id = int(input("Enter book ID to remove: "))
    
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            print(f"Book '{book['title']}' removed successfully.")
            return
    
    print(fail + "\nBook not found." + end)
    print("\n-----------------------------------")

    exit_program()
    
def add_member():
    print("==== Register Member ====")
    
    member_id = len(members) + 1
    name = input("Enter member name: ")
    
    new_member = {
        "id": member_id,
        "name": name
    }
    
    members.append(new_member)
    print(f"Member '{name}' registered successfully.")
    print(f"Member ID: {member_id}")

    exit_program()
    
        
    
def view_members():
    print("==== View Members ====")
    
    if len(members) == 0:
        print(fail + "No members registered." + end)
        return
    
    for member in members:
        print("----------------")
        print(f"ID: {member['id']}")
        print(f"Name: {member['name']}")
        
    print("-----------------------------------")
    
    exit_program()
        
def search_member():
    print("----------- Search Member -----------")
    
    search_name = input("Enter member name: ")
    
    found = False
    for member in members:
        if member['name'].lower() == search_name.lower():
            print("----------------")
            print(f"ID: {member['id']}")
            print(f"Name: {member['name']}")
            found = True
        
    if not found:
        print(fail + "Member not found." + end)

    exit_program()

def borrow_book():
    print("==== Borrow Book ====")
    
    if len(members) == 0:
        print(fail + "No members registered. Please register a member first." + end)
        return
    
    member_id = int(input("Enter member ID: "))
    
    # Check if member exists
    member_exists = any(member['id'] == member_id for member in members)
    if not member_exists:
        print(fail + "Member not found." + end)
        return
    
    book_id = int(input("Enter book ID to borrow: "))
    
    # Check if book exists and is available
    for book in books:
        if book['id'] == book_id:
            if book['available']:
                book['available'] = False
                borrowed_books.append({
                    "member_id": member_id,
                    "book_id": book_id
                })
                print(f"Book '{book['title']}' borrowed successfully.")
                return
            else:
                print(fail + "\n Book is not available." + end)
                return
    
    print(fail + "Book not found." + end)
    
    exit_program()
    
def return_book():
    print("----------- Return Book -----------")
    
    member_id = int(input("Enter member ID: "))
    
    # Check if member exists
    member_exists = any(member['id'] == member_id for member in members)
    if not member_exists:
        print(fail + "Member not found." + end)
        return
    
    book_id = int(input("Enter book ID to return: "))
    
    # Check if the book was borrowed by the member
    for borrowed in borrowed_books:
        if borrowed['member_id'] == member_id and borrowed['book_id'] == book_id:
            borrowed_books.remove(borrowed)
            for book in books:
                if book['id'] == book_id:
                    book['available'] = True
                    print(f"Book '{book['title']}' returned successfully.")
                    return
    
    print(fail + "No record of this book being borrowed by the member." + end)
  
    exit_program()
    
def view_borrowed_books():
    print("==== View Borrowed Books ====")
    
    if len(borrowed_books) == 0:
        print(bcolors.WARNING + "\nNo books are currently borrowed." + bcolors.ENDC)
        return
    
    for borrowed in borrowed_books:
        member_id = borrowed['member_id']
        book_id = borrowed['book_id']
        
        member_name = next((member['name'] for member in members if member['id'] == member_id), "Unknown Member")
        book_title = next((book['title'] for book in books if book['id'] == book_id), "Unknown Book")
        
        print(f"Member ID: {member_id}")
        print(f"Member Name: {member_name}")
        print(f"Book ID: {book_id}")
        print(f"Book Title: {book_title}")
        
    exit_program()

def main():
    while True:
        
        print("\n  --------------------------")
        print(" |"+bcolors.OKGREEN+" Library Management System "+bcolors.ENDC +" |     ⠀⠀⠀⢸⣦⡀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀")
        print(" |  0. View Rules             |     ⠀⠀⠀⢸⣏⠻⣶⣤⡶⢾⡿⠁⠀⢠⣄⡀⢀⣴⠀")
        print(" |  1. Add Book               |     ⠀⠀⣀⣼⠷⠀⠀⠁⢀⣿⠃⠀⠀⢀⣿⣿⣿⣇⠀ ˚　　✦　　　.　　. 　 ˚　.　　　　　 . ✦　　　 　˚　　　　 . ★ ⋆ .")
        print(" |  2. View Books             |     ⠴⣾⣯⣅⣀⠀⠀⠀⠈⢻⣦⡀⠒⠻⠿⣿⡿⠿⠓⠂⠀⠀⢀⡇ 　.   　　˚　　 　*　　 　　✦　.　　.　　　✦　˚ 　 ˚　.˚　　　.　　. 　 ˚　.　 ⠀")
        print(" |  3. Search Book            |     ⠀⠀⠀⠉⢻⡇⣤⣾⣿⣷⣿⣿⣤⠀⠀⣿⠁⠀⠀⠀⢀⣴⣿⣿⠀")
        print(" |  4. Remove Book            |     ⠀⠀⠀⠀⠸⣿⡿⠏⠀⢀⠀⠀⠿⣶⣤⣤⣤⣄⣀⣴⣿⡿⢻⣿⡆⠀⠀")
        print(" |  5. Register Member        |     ⠀⠀⠀⠀⠀⠟⠁⠀⢀⣼⠀⠀⠀⠹⣿⣟⠿⠿⠿⡿⠋⠀⠘⣿⣇⠀.   　　˚　　　✦　.　　.　　　✦　˚ 　 ˚　.˚　　　.　　. 　 ˚　.　" )
        print(" |  6. View Members           |     ⠀⠀⠀⠀⠀⢳⣶⣶⣿⣿⣇⣀⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⠛⠿⣿⣦⣤⣀⠀⠀　　　 . ✦　　　 　˚　　　　 . ★ ⋆ .")
        print(" |  7. Search Member          |     ⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⠿⠋⠁⠀⣹⣿⠳⠀⠀⠁⠀⠀⠀⢀⣠⣽⣿⡿⠟⠃")
        print(" |  8. Borrow Book            |     ⠀⠀⠀⠀⠀⢰⠿⠛⠻⢿⡇⠀⠀⠀⣰⣿⠏⠀⠀⢀⠀⠀⠀⣾⣿⠟⠋⠁⠀⠀")
        print(" |  9. Return Book            |     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣰⣿⣿⣾⣿⠿⢿⣷⣀⢀⣿⡇⠁⠀⠀⠀✦　.　　.　　　✦　˚ 　 ˚　.˚　　　.　　. 　⠀")
        print(" |  10. View Borrowed Books   |     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠉⠁⠀⠀⠀⠀⠙⢿⣿⣿⠇⠀⠀")
        print(" |  11. Exit                  |     ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⠀⠀⠀⠀⠀")
        print("  ---------------------------")
        
        choice = input(bcolors.OKGREEN + "Enter choice: " + bcolors.ENDC)
        
        if choice == '0':
            view_rules()
        elif choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            add_member()
        elif choice == '6':
            view_members()
        elif choice == '7':
            search_member()
        elif choice == '8':
            borrow_book()
        elif choice == '9':
            return_book()
        elif choice == '10':
            view_borrowed_books()
        elif choice == '11':
            print("Exiting the program. Thank you for using the Library Management System, bye-bye!!!")
            break
        else:
            print(fail + "\nInvalid choice. Please try again." + end)

main()
