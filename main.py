# functions
# add book
# view book
# search book
# remove book

# register member
# view member list
# search member

# borrow and return book function 
# view borrowed books

members = []
borrowed_books = []

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

def add_book():
    print("==== Add Book ====")
    
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
    print(f"Book '{title}' added successfully!")
    
def view_books():
    print("==== View Books ====")
    
    if len(books) == 0:
        print("No books available.")
        return
    
    for book in books:
        print("----------------")
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {'Available' if book['available'] else 'Not Available'}")
    print("====================")
    
def search_book():
    print("==== Search Book ====")
    
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
        print("Book not found.")
    print("======================")
        
def remove_book():
    print("==== Remove Book ====")
    
    book_id = int(input("Enter book ID to remove: "))
    
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            print(f"Book '{book['title']}' removed successfully.")
            return
    
    print("Book not found.")
    print("=====================")

    
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
    print("=========================")
    
def view_members():
    print("==== View Members ====")
    
    if len(members) == 0:
        print("No members registered.")
        return
    
    for member in members:
        print("----------------")
        print(f"ID: {member['id']}")
        print(f"Name: {member['name']}")
        
    print("=========================")
        
def search_member():
    print("==== Search Member ====")
    
    search_name = input("Enter member name: ")
    
    found = False
    for member in members:
        if member['name'].lower() == search_name.lower():
            print("----------------")
            print(f"ID: {member['id']}")
            print(f"Name: {member['name']}")
            found = True
        
    if not found:
        print("Member not found.")
        
    print("=========================")

def borrow_book():
    print("==== Borrow Book ====")
    
    if len(members) == 0:
        print("No members registered. Please register a member first.")
        return
    
    member_id = int(input("Enter member ID: "))
    
    # Check if member exists
    member_exists = any(member['id'] == member_id for member in members)
    if not member_exists:
        print("Member not found.")
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
                print("Book is not available.")
                return
    
    print("Book not found.")
    print("=========================")
    
def return_book():
    print("==== Return Book ====")
    
    member_id = int(input("Enter member ID: "))
    
    # Check if member exists
    member_exists = any(member['id'] == member_id for member in members)
    if not member_exists:
        print("Member not found.")
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
    
    print("No record of this book being borrowed by the member.")
    print("=========================")
    
def view_borrowed_books():
    print("==== View Borrowed Books ====")
    
    if len(borrowed_books) == 0:
        print("No books are currently borrowed.")
        return
    
    for borrowed in borrowed_books:
        member_id = borrowed['member_id']
        book_id = borrowed['book_id']
        
        member_name = next((member['name'] for member in members if member['id'] == member_id), "Unknown Member")
        book_title = next((book['title'] for book in books if book['id'] == book_id), "Unknown Book")
        
        print("----------------")
        print(f"Member ID: {member_id}")
        print(f"Member Name: {member_name}")
        print(f"Book ID: {book_id}")
        print(f"Book Title: {book_title}")
        
    print("=========================")

def main():
    while True:
        print("\n==== Library Management System ====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Register Member")
        print("6. View Members")
        print("7. Search Member")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. View Borrowed Books")
        print("11. Exit")
        print("===================================")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
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
            print("Invalid choice. Please try again.")
            
main()