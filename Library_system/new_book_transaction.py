# For JSON operations
import json
import random
# For file checking
import os
from lending import tracking_read


#from tracking_module import book_lending_read

# Read book.json file
def read():
   
    try:
        if not os.path.exists("Library_system/book.json") or os.path.getsize("Library_system/book.json") == 0:
            
            return []
            
        with open("Library_system/book.json", "r", encoding="utf-8", errors="ignore") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []


# Write data to book.json file
def save(data):
    try:
        with open("Library_system/book.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        f"An error occurred while saving: {e}"
        return None


# Add a book


def add_book(Book_Title, Author, Publisher, Barcode=0):
   
    try:
       
        if not all([Book_Title, Author, Publisher]):
            return "All fields must be filled!"

        books = read()
        lend= tracking_read()
        
        if books!=[]:        
            for book in books:
                
                if (
                    
                    book["Book_Title"].lower() == Book_Title.lower().strip()
                    and book["Author"].lower() == Author.lower().strip()
                    and book["Publisher"].lower() == Publisher.lower().strip()
                ):
                    
                    
                    return None  # already exists
            for lend_book in lend:
                if (
                    
                    lend_book["Book_Title"].lower() == Book_Title.lower().strip()
                    and lend_book["Author"].lower() == Author.lower().strip()
                    and lend_book["Publisher"].lower() == Publisher.lower().strip()
                ):
                    
                    
                    return None #already exists
         
        
        if books == [] or Barcode == 0:
            new_barcode = random.randint(100000, 999999)
        else:
        
            
                
                
                barcodes = [book["Barcode"] for book in books]+[lend_book["Barcode"] for lend_book in lend]
                new_barcode = random.randint(100000, 999999)
                while new_barcode in barcodes:
                    
                    new_barcode = random.randint(100000, 999999)
          
        
        
        new_book = {
            "Barcode": str(new_barcode),
            "Book_Title": Book_Title.strip(),
            "Author": Author.strip(),
            "Publisher": Publisher.strip(),
        }
        
        books.append(new_book)

        if save(books):
            
            return True 

        else:
            return False
    except Exception as e:
        
        f"An error occurred: {str(e)}"
        return None


# Delete a book
def delete_book(barcode):
    
    try:
        

        books = read()
        
        
        
        
        
        filtered_books = [
            book for book in books if str(book["Barcode"]) != barcode
        ]
        
        
        if len(books) == len(filtered_books):
            
            return False

        if save(filtered_books):
            return True

    except Exception as e:
        return f"Error: {e}"


# Search for a book
def search_book(barcode):
    
    books = read()
    print(books)
    if books == []:
        return False
    else:
        print("else section")
        try:

            
            
            if not barcode.isdigit():
                print("this not barcode section")
                
                for book in books:
                    if book["Book_Title"].lower() == barcode.lower().strip():
                        
                        return book
            elif barcode.isdigit():

                print ("it is a digit")
                
                for book in books:
                    print("searching for book")
                    if book["Barcode"] == barcode:
                    
                        print("book found")
                        return book
                    else:
                        
                        return False
            else:
                print("Book not found")
                return False
            
            

        except Exception as e:
            print("try catch") 
            print(f"An error occurred: {e}")
            return False


def books():
    books = read()
    
    if books == []:
        print("No books found")
        return False
    else:
        for book in books:
            print(f"Title: {book['Book_Title']}\nAuthor: {book['Author']}\nPublisher: {book['Publisher']}\nBarcode: {book['Barcode']}\n{"="*20}")
        


if __name__ == "__main__":
    pass
