# utility function to read data from a file
def append_to_file(filename,data):
    with open(filename,'a') as f:
        f.write(data + '\n')

# utility function to read data from a file
def read_file(filename):
    try:
        with open(filename,'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return[]
#1. Function to add a new book
def add_book():
    # Taking book information to add as input from user 
    book_id = input("Enter Book ID : ")
    title = input("Enter the book Title : ")
    author = input("Enter the Author name : ")
    category = input("Enter category : ")
    status = "available" # book is initially available

    #write book details to books.txt
    book_record = f"{book_id},{title},{author},{category},{status}"
    append_to_file('books.txt',book_record)
    print("Book added successfully!!!")

#2. Function to View all books
def view_books():
    books = read_file('books.txt') # Reads all book in books.txt file 
    # If there is no book information in books.txt file,
    if not books: 
        print("No books available") 
        return
    print("Books Records")
    for book in books:
        book_id,title,author,category,status=book.strip().split(',')
        # The output will be given with the following template or format
        print(f"ID:{book_id},Title:{title},Author:{author},Category:{category},Status:{status}")

#3. Function to search books by title or author
def search_books():
    # Taking the book needed to be searched as input from the user
    # Convert to lowercase to avoid character specification search
    query = input("Enter book title or author to search : ").lower()
    books = read_file('books.txt')
    found = False
    for book in books:
        _,title,author,_,status=book.strip().split(',')
        # If the searched book by its name or author name is found
        # All information of book is given as output
        if query in title.lower() or query in author.lower(): # both are converted to lowercase to search without error
            print(f"Title:{title},Author:{author},Status:{status}")
            found=True
    # If the searched book is not found
    if not found:
        print("No matching books found")

# 4. Function to delete a book record
def delete_book():
    # The book ID of the book needed to be deleted is taken as input from user
    book_id = input("Enter Book ID to Delete: ")
    books = read_file('books.txt') # Reading data from the file
    updated_books = [book for book in books if not book.startswith(book_id)] 
# Enters all the books in the file books.txt except the one entered by the user to delete

    with open('books.txt', 'w') as f:
        for book in updated_books:
            f.write(book)
    #Deletes book from the file Book.txt
    print("Book deleted successfully!")

#5. Menu system using a dictionary-based switch
def menu():
    while True: # Infinite loop which will keep on looping until we break
        #Library Management System Menu bar is showed
        print("\n Library management System")
        print("1. Add Book")
        print("2. View Book")
        print("3. Search books")
        print("4. Delete a book")
        print("5. Exit")

        # Taking which is the choice from the menu as input from the user 
        choice = input("Enter your choice : ")
        actions = {
            '1' : add_book,
            '2' : view_books,
            '3' : search_books,
            '4' : delete_book,
            '5' : exit
        } # Function call are mapped with respect to the User choice
        action = actions.get(choice)
        if action:
            action() # Calling the respective function 
        else:
            print("invalid choice! please try again")
# Entry point of the program
if __name__ == "__main__":  # Built in variable
    # Python file is being run
    menu()
