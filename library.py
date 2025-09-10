# Add book to the library
def add(library: dict, id: str, title: str):
    library[id] = title
    print("Succesfully added the book details")

# Remove book
def remove(library: dict, id: str):
    if id not in library:
        print(f"There is no book in the library with the id {id}")
    else:
        library.pop(id)
    
# Search for a book
def search(library: dict, id: str):
    if id not in library:
        print(f"There is no book in the library with the id {id}")
    else:
        print(f"{id}: {library[id]}")

# Update title
def update(library: dict, id: str, title: str):
    if id not in library:
        print(f"There is no book in the library with the id {id}")
    else:
        library[id] = title
        print(f"Successfully updated the title")
        
# Display all books in the library
def display(library: dict):
    print("Details of books in the library are")
    for id, title in library.items():
        print(f"{id}: {title}")
        
# Total books in the library
def count_books(library: dict):
    print(f"There are{len(library)} books in the library")
    
# Check if a title exists in the library
def check_title(library: dict, title: str):
    if title not in library.values():
        print(f"There is no book in the library with the title {title}")
    else:
        print(f"There exists a book in the library with the title {title}")
        

# Print Menu
def print_menu():
    print("----------------------------------------------------------------------------------------------------")
    print("1.Add book")
    print("2.Remove book")
    print("3.Search for book")
    print("4.Update title")
    print("5.Display all books")
    print("6.Count total number of books")
    print("7.Check if a book title exists")
    print("8.Exit")
    print("----------------------------------------------------------------------------------------------------")
    
cond = True
library = {}
while cond:
    print_menu()
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            add(library, input("Enter the id of the book: "), input("Enter the title of the book: "))
        
        case 2:
            remove(library, input("Enter the id of the book: "))
        
        case 3:
            search(library, input("Enter the id of the book: "))
            
        case 4:
            update(library, input("Enter the id of the book: "), input("Enter the title of the book: "))
            
        case 5:
            display(library)
        
        case 6:
            count_books()
            
        case 7:
            check_title(library, input("Enter the title of the book: "))
        
        case 8:
            cond = False
            
    if not cond: break