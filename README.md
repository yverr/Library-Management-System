(last updated: 09/29/26)

# Library-Management-System

NEW FEATURES: 
- Loan period: every borrowed book has a 7 day limit
- Borrow tracking: when a book is borrowed, the program saves the borrow date and the due date.
- Return tracking: when a book is returned the program saves the return date and calculates if the book was returned in time
- Late fines: if the book is returned late or past the due date, the fine is the number of days late times FINE_PER_DAY (currently P30). But returning exactly on the due date is free
- Overdue stat: the view borrowed books now shows the dates for each book plus how many days are left or how many days is overdue and then the current info
- Return history: new function listing every returned book with the member, book, borrow date, due date, return date, and any fine.

FEATURES TO BE FIXED
- The int(input(...)) lines (member ID, book ID) have no error handling.
- (limitation) data is not saved after closing the program 
