# Library Management System (terminal version)
# everything is stored in lists of dictionaries, not in a database or file
# so all the data resets whenever the program closes...

# ! ADDITIONAL FEATURES TO BE ADDED
# add status on members and borrowed books
# DONE: time limit on borrowed books + fine fees
# DONE: RULES

# date = today's date, timedelta = a chunk of time (like "7 days").
# we use em together to work out due dates and how late a book is
from datetime import date, timedelta

# settings for the borrowing rules. The rest of the code reads these two,
# so if we want to change the rules we only edit them here
LOAN_DAYS = 7          # how long they can keep the book
FINE_PER_DAY = 30      # pesos per day late

# for testing: set this to a number of days to skip ahead in time
DAY_OFFSET = 0

# gives us today's date plus DAY_OFFSET. We use this instead of date.today()
# so we can fake time passing. Example: DAY_OFFSET = 10 acts like it's 10 days
# from now, which lets us test late fines without waiting
def today():
    return date.today() + timedelta(days=DAY_OFFSET)

returned_books = []    # history of returned books

# text color in the terminal
class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    YELLOW = '\033[33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# shortcuts so we can write green + "text" + end instead of typing
# bcolors.OKGREEN every time. 'end' resets the color back to normal
green = bcolors.OKGREEN
end = bcolors.ENDC
yellow = bcolors.YELLOW
fail = bcolors.FAIL

# members = everyone registered
# borrowed_books = loans that are still going on (the book hasn't been returned yet)
# none of this is saved to a file, so it all resets when the program closes
members = []
borrowed_books = []

# the books list 
# each book is a dictionary: id, title, author, and available
# available = True means it's on the shelf, False means someone borrowed it
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

# called in the end of every function to prevent the user from immediately going back to the main menu
def exit_program():
    print(green + "\nPress any key to return to the main menu." + end)
    # input() just waits for the user to press Enter, so the menu
    # doesn't instantly pop up and cover whatever was printed
    input()

# prints the rules. It uses LOAN_DAYS and FINE_PER_DAY so the rules shown
# always match what the program actually does
def view_rules():
    print("\n╔═══════════════════════════"+ green +" RULES "+ end +"═════════════════════════════╗" )
    print(f"║   1. Books can be borrowed for 7 days.                        ║")
    print(f"║   2. Late returns are fined P30 per day after the due date.   ║")
    print("║   3. Returning on the due date is still free.                 ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

    exit_program()

# add book function
def add_book():
    print("")
    print(green + "----------- ADD BOOK -----------" + end)
    
    # new id = number of books + 1 (3 books now, so the new one gets id 4)
    book_id = len(books) + 1
    # ask the user for the new book's details
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    
    # build the book as a dictionary. available starts as True since nobody has borrowed it yet
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    
    # append = add it to the end of the books list
    books.append(new_book)
    print(yellow + f"\nBook '{title}' added successfully!" + end)
    
    exit_program()
    
# prints every book in the list, with its status
def view_books():
    print("==== View Books ====")
    
    # if the list is empty there's nothing to show, so we stop early
    if len(books) == 0:
        print(fail + "\nNo books available." + end)
        return
    
    # go through the books one by one and print each one's details
    for book in books:
        print("----------------")
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        # 'available' is True/False, so this turns it into words people can read
        print(f"Status: {'Available' if book['available'] else 'Not Available'}")
    print("----------------")
    
    exit_program()
    
# looks for a book by title. Needs the full title, but capital letters don't matter
def search_book():
    print(green + "\n----------- Search Book -----------" + end)
    
    search_title = input("Enter book title: ")
    
    # starts as False and becomes True if we find a match.
    # we check it after the loop to know if we should print "not found"
    found = False
    for book in books:
        # .lower() makes both lowercase, so "reverend insanity" still matches "Reverend Insanity"
        if book['title'].lower() == search_title.lower():
            print("----------------")
            print(f"ID: {book['id']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Status: {'Available' if book['available'] else 'Not Available'}")
            found = True
        
    # nothing matched, so tell the user
    if not found:
        print(fail + "Book not found." + end)
    print(green +"-----------------------------------" + end)
    
    exit_program()    
        
# deletes a book using its ID
def remove_book():
    print("----------- Remove Book -----------")
    
    # input() gives text, so int() turns it into a number we can compare with the ids
    book_id = int(input("Enter book ID to remove: "))
    
    for book in books:
        # found the book the user wants to remove
        if book['id'] == book_id:
            # take it out of the books list
            books.remove(book)
            print(f"Book '{book['title']}' removed successfully.")
            return
    
    # if we get here, the loop finished and no book had that id
    print(fail + "\nBook not found." + end)
    print("\n-----------------------------------")

    exit_program()
    
# registers a new member
def add_member():
    print("==== Register Member ====")
    
    # same idea as the book id: number of members + 1
    member_id = len(members) + 1
    name = input("Enter member name: ")
    
    # for now a member only has an id and a name
    new_member = {
        "id": member_id,
        "name": name
    }
    
    members.append(new_member)
    print(f"Member '{name}' registered successfully.")
    print(f"Member ID: {member_id}")

    exit_program()
    
        
    
# prints every registered member
def view_members():
    print("----------- View Members -----------")
    
    # nobody registered yet, so there's non to show
    if len(members) == 0:
        print(fail + "No members registered." + end)
        return
    
    for member in members:
        print("----------------")
        print(f"ID: {member['id']}")
        print(f"Name: {member['name']}")
        
    print("-----------------------------------")
    
    exit_program()
        
# finds a member by name (full name, capital letters don't matter)
def search_member():
    print("----------- Search Member -----------")
    
    search_name = input("Enter member name: ")
    
    found = False
    for member in members:
        # lowercase both sides so the capitalization doesn't affect the match
        if member['name'].lower() == search_name.lower():
            print("----------------")
            print(f"ID: {member['id']}")
            print(f"Name: {member['name']}")
            found = True
        
    if not found:
        print(fail + "Member not found." + end)

    exit_program()

# lets a member borrow a book. Checks in order:
# are there any members, does this member exist,
# does the book exist, and is it available ?
# if everything passes, the book becomes unavailable and we save a loan record with a due date
def borrow_book():
    print("----------- Borrow Book -----------")
    
    # can't borrow anything if nobody is registered yet
    if len(members) == 0:
        print(fail + "No members registered. Please register a member first." + end)
        return
    
    # ask who is borrowing
    member_id = int(input("Enter member ID: "))
    
    # Check if member exists
    # any() gives True if at least one member has this id.
    # just a shorter way of writing a for loop with an if inside
    member_exists = any(member['id'] == member_id for member in members)
    if not member_exists:
        print(fail + "Member not found." + end)
        return
    
    book_id = int(input("Enter book ID to borrow: "))
    
    # Check if book exists and is available
    for book in books:
        if book['id'] == book_id:
            # only allow it if the book is still on the shelf
            if book['available']:
                # mark it as taken so nobody else can borrow it
                book['available'] = False
                
                # due date = borrow date + LOAN_DAYS (timedelta is what lets us add days to a date)
                borrowed_on = today()
                due_date = borrowed_on + timedelta(days=LOAN_DAYS)
                
                # save the loan, We only store the member id and book id here
                # and then look up the names later when we need to display them
                borrowed_books.append({
                    "member_id": member_id,
                    "book_id": book_id,
                    "borrowed_on": borrowed_on,
                    "due_date": due_date
                })
                print(f"Book '{book['title']}' borrowed successfully.")
                print(f"Borrowed on: {borrowed_on}")
                print(yellow + f"Due date: {due_date}" + end)
                exit_program()
                return
            else:
                print(fail + "\n Book is not available." + end)
                return
    
    # the loop ended without finding a book with that id
    print(fail + "Book not found." + end)
    
    exit_program()
    
# returns a book. Finds the loan, checks if it's late, calculates the fine,
# moves the loan to the history list, and puts the book back on the shelf
def return_book():
    print("----------- Return Book -----------")
    
    member_id = int(input("Enter member ID: "))
    
    # Check if member exists
    # same member check as in borrow_book
    member_exists = any(member['id'] == member_id for member in members)
    if not member_exists:
        print(fail + "Member not found." + end)
        return
    
    book_id = int(input("Enter book ID to return: "))
    
    # Check if the book was borrowed by the member
    # look through the current loans for one that matches BOTH the member and the book..
    for borrowed in borrowed_books:
        if borrowed['member_id'] == member_id and borrowed['book_id'] == book_id:
            # days_late = return date minus due date.
            # max(0, ...) keeps it from going negative when the book is returned early
            returned_on = today()
            days_late = max(0, (returned_on - borrowed['due_date']).days)
            # total fine = number of days late x pesos per day
            fine = days_late * FINE_PER_DAY
            
            # the loan is done, so remove it from the list of current loans
            borrowed_books.remove(borrowed)
            # and save it in the history (with the fine) so View Return History can show it later
            returned_books.append({
                "member_id": member_id,
                "book_id": book_id,
                "borrowed_on": borrowed['borrowed_on'],
                "due_date": borrowed['due_date'],
                "returned_on": returned_on,
                "days_late": days_late,
                "fine": fine
            })
            
            for book in books:
                if book['id'] == book_id:
                    # put the book back on the shelf so it can be borrowed again
                    book['available'] = True
                    print(f"Book '{book['title']}' returned successfully.")
                    print(f"Borrowed on: {borrowed['borrowed_on']}")
                    print(f"Due date: {borrowed['due_date']}")
                    print(f"Returned on: {returned_on}")
                    # red message if they were late, green if they were on time
                    if fine > 0:
                        print(fail + f"Late by {days_late} day(s). Fine: P{fine}" + end)
                    else:
                        print(green + "Returned on time. No fine." + end)
                    exit_program()
                    return
    
    # we only get here if no loan matched (wrong member or wrong book)
    print(fail + "No record of this book being borrowed by the member." + end)
  
    exit_program()
    
# shows every book that's currently borrowed: who has it, due date, and if it's overdue
def view_borrowed_books():
    print("==== View Borrowed Books ====")
    
    # no loans rn, so just say so and go back to the menu..
    if len(borrowed_books) == 0:
        print(bcolors.WARNING + "\nNo books are currently borrowed." + bcolors.ENDC)
        exit_program()
        return
    
    for borrowed in borrowed_books:
        member_id = borrowed['member_id']
        book_id = borrowed['book_id']
        
        # look up the member's name using their ID
        # fallback text in case we can't find the member. If the loop finds them, it gets replaced
        member_name = "Unknown Member"
        for member in members:
            if member['id'] == member_id:
                # found them, so save the name the break below stops the loop 
                member_name = member['name']
                break
        
        # look up the book's title using its ID
        book_title = "Unknown Book"
        for book in books:
            if book['id'] == book_id:
                book_title = book['title']
                break
        
        print("----------------")
        print(f"Member ID: {member_id}")
        print(f"Member Name: {member_name}")
        print(f"Book ID: {book_id}")
        print(f"Book Title: {book_title}")
        print(f"Borrowed on: {borrowed['borrowed_on']}")
        print(f"Due date: {borrowed['due_date']}")
        
        # subtracting two dates gives a timedelta, and .days is the number of days.
        # positive = overdue, zero or negative = still has time left
        days_late = (today() - borrowed['due_date']).days
        # overdue: show the fine so far (red). Otherwise show how many days are left (green)
        if days_late > 0:
            print(fail + f"Status: OVERDUE by {days_late} day(s). Current fine: P{days_late * FINE_PER_DAY}" + end)
        else:
            print(green + f"Status: On time ({-days_late} day(s) left)" + end)
    print("----------------")
        
    exit_program()

# shows every book that was already returned, including any fines
def view_history():
    print(green + "\n----------- Return History -----------" + end)
    
    # nothings been returned yet
    if len(returned_books) == 0:
        print(fail + "No returned books yet." + end)
        exit_program()
        return
    
    # r is one return record (a dictionary from the returned_books list)
    for r in returned_books:
        # look up the member's name using their ID
        # same lookup as view borrowed book where were turning ids into names
        member_name = "Unknown Member"
        for member in members:
            if member['id'] == r['member_id']:
                member_name = member['name']
                break
        
        # look up the book's title using its ID
        book_title = "Unknown Book"
        for book in books:
            if book['id'] == r['book_id']:
                book_title = book['title']
                break
        
        print("----------------")
        print(f"Member: {member_name} (ID: {r['member_id']})")
        print(f"Book: {book_title} (ID: {r['book_id']})")
        print(f"Borrowed on: {r['borrowed_on']}")
        print(f"Due date: {r['due_date']}")
        print(f"Returned on: {r['returned_on']}")
        if r['fine'] > 0:
            print(fail + f"Late by {r['days_late']} day(s). Fine: P{r['fine']}" + end)
        else:
            print(green + "On time. No fine." + end)
    print("----------------")
    
    exit_program()

# the main menu | keeps running until the user picks 12 (Exit)
def main():
    # loops forever so the menu shows again after each action.
    # the only way out is the 'break' in the exit option
    while True:
     
        print("\n ╔════════════════════════════════╗")
        print(" ║"+bcolors.OKGREEN+"  Library Management System "+bcolors.ENDC +"    ║     ⠀⠀⠀⢸⣦⡀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀")
        print(" ║  [0] View Rules                ║     ⠀⠀⠀⢸⣏⠻⣶⣤⡶⢾⡿⠁⠀⢠⣄⡀⢀⣴⠀")
        print(" ║  [1] Add Book                  ║     ⠀⠀⣀⣼⠷⠀⠀⠁⢀⣿⠃⠀⠀⢀⣿⣿⣿⣇⠀ ˚　　✦　　　.　　. 　 ˚　.　　　　　 . ✦　　　 　˚　　　　 . ★ ⋆ .")
        print(" ║  [2] View Books                ║     ⠴⣾⣯⣅⣀⠀⠀⠀⠈⢻⣦⡀⠒⠻⠿⣿⡿⠿⠓⠂⠀⠀⢀⡇ 　.   　　˚　　 　*　　 　　✦　.　　.　　　✦　˚ 　 ˚　.˚　　　.　　. 　 ˚　.　 ⠀")
        print(" ║  [3] Search Book               ║     ⠀⠀⠀⠉⢻⡇⣤⣾⣿⣷⣿⣿⣤⠀⠀⣿⠁⠀⠀⠀⢀⣴⣿⣿⠀")
        print(" ║  [4] Remove Book               ║     ⠀⠀⠀⠀⠸⣿⡿⠏⠀⢀⠀⠀⠿⣶⣤⣤⣤⣄⣀⣴⣿⡿⢻⣿⡆⠀⠀")
        print(" ║  [5] Register Member           ║     ⠀⠀⠀⠀⠀⠟⠁⠀⢀⣼⠀⠀⠀⠹⣿⣟⠿⠿⠿⡿⠋⠀⠘⣿⣇⠀.   　　˚　　　✦　.　　.　　　✦　˚ 　 ˚　.˚　　　.　　. 　 ˚　.　" )
        print(" ║  [6] View Members              ║     ⠀⠀⠀⠀⠀⢳⣶⣶⣿⣿⣇⣀⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⠛⠿⣿⣦⣤⣀⠀⠀　　　 . ✦　　　 　˚　　　　 . ★ ⋆ .")
        print(" ║  [7] Search Member             ║     ⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⠿⠋⠁⠀⣹⣿⠳⠀⠀⠁⠀⠀⠀⢀⣠⣽⣿⡿⠟⠃")
        print(" ║  [8] Borrow Book               ║     ⠀⠀⠀⠀⠀⢰⠿⠛⠻⢿⡇⠀⠀⠀⣰⣿⠏⠀⠀⢀⠀⠀⠀⣾⣿⠟⠋⠁⠀⠀")
        print(" ║  [9] Return Book               ║     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣰⣿⣿⣾⣿⠿⢿⣷⣀⢀⣿⡇⠁⠀⠀⠀✦　.　　.　　　✦　˚ 　 ˚　.˚　　　.　　. 　⠀")
        print(" ║  [10] View Borrowed Books      ║     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠉⠁⠀⠀⠀⠀⠙⢿⣿⣿⠇⠀⠀")
        print(" ║  [11] View Return History      ║     ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⠀⠀⠀⠀⠀")
        print(" ║  [12] Exit                     ║")
        print(" ╚════════════════════════════════╝")
        
        choice = input(bcolors.OKGREEN + " ➤  Enter choice: " + bcolors.ENDC)
        
        # each choice calls the function that handles that feature
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
            view_history()
        elif choice == '12':
            print("Exiting the program. Thank you for using the Library Management System, bye-bye!!!")
            break
        else:
            print(fail + "\nInvalid choice. Please try again." + end)

# start the program
main()