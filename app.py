import json
import os

data_file = "library.json"  # Changed to .json for consistency

def load_library():
    """Loads the library from a JSON file, handling errors and empty files."""
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as file:
            try:
                content = file.read().strip()
                return json.loads(content) if content else []
            except json.JSONDecodeError:
                print("Error: The data file is corrupted. Starting with an empty library.")
                return []
    return []  # Return an empty list if the file doesn't exist

def save_library(library):
    """Saves the library to a JSON file with formatting for readability."""
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(library, file, indent=4, ensure_ascii=False)

def add_book(library):
    """Adds a book to the library with user input."""
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    year = input("Enter the year of the book: ").strip()
    genre = input("Enter the genre of the book: ").strip()
    read = input("Have you read the book? (yes/no): ").strip().lower() == "yes"

    if not title or not author or not year or not genre:
        print("Error: All fields are required.")
        return

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    """Removes a book from the library by title."""
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library[:]:  # Iterate over a copy to safely remove items
        if book["title"].lower() == title:
            library.remove(book)
            save_library(library)
            print(f"Book '{title}' removed successfully!")
            return  # Exit after removing the first match

    print(f"Book '{title}' not found in the library!")

def search_library(library):
    """Searches for books by title or author."""
    search_by = input("Search by title or author? ").strip().lower()
    if search_by not in ["title", "author"]:
        print("Invalid choice. Please enter 'title' or 'author'.")
        return
    
    search_term = input(f"Enter the {search_by}: ").strip().lower()
    
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            status = "Read" if book["read"] else "Not read"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print(f"No books found for '{search_term}' in the {search_by} field.")

def display_all_books(library):
    """Displays all books in the library."""
    if library:
        print("\nLibrary Collection:")
        for book in library:
            status = "Read" if book["read"] else "Not read"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No books in the library.")

def display_statistics(library):
    """Displays statistics about the library."""
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({percentage_read:.2f}%)")

def main():
    """Main function to run the library system."""
    library = load_library()

    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)  # Ensure data is saved before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
