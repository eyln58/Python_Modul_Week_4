import new_book_transaction
import membership
from screening import screen
import os
import lending



def get_input(prompt, error_message="Field cannot be empty. Please try again."):
    while True:
        value = input(prompt).strip().lower()
        if value:
            return value
        print(error_message)


def main_menu():
    

    while True:
        try:
            screen("Welcome")
            option=input("\nPlease choose the options above and press Enter to continue:")
            
            if option == "1":
                
                
                
                while True:
                    screen("Membership")
                    mem_opt=input("\nPlease choose the options above and press Enter to continue:")

                    match mem_opt:
                        case "2":
                            
                            name = get_input("Enter name and surname: ")
                            address = get_input("Enter address: ")
                            phone = get_input("Enter phone number: ")
                            membership.add_new_member(name, phone, address)
                        
                        case "4":
                            if (membership.member_control()):
                                phone = get_input("Enter phone number of the member to delete: ")
                                membership.members_delete(phone)
                            else:
                                print("No Members")  
                        case "3":
                            if (membership.member_control()):
                                phone = get_input("Enter phone number of the member to view details:")
                                membership.member_update(phone)  
                            else:
                                print("No Members")  
                                
                                


                        case "1":
                                
                                membership.member_control()
                                
                                    
                                
                                
                        case "5":
                            
                                phone_number = get_input("Enter phone number of the member: ")
                                barcode = get_input("Enter the book barcode to lend: ")
                                lending.lending_book(phone_number, barcode)
                        case "6":
                            
                                barcode = get_input("Enter the book barcode to return: ")
                                lending.return_book(barcode)
                        case "7":
                                lending.view_lent_books()

                        case "0":   
                            break  

                        case _:
                            print("Invalid option, please try again")

            elif option == "2":
                while True:
                    screen("Book")
                    book_opt=input("\nPlease choose the options above and press Enter to continue:")
                    match book_opt:
                        case "1":

                            books=new_book_transaction.books()
                        case "2":
                            title = get_input("Enter the book title: ")
                            author = get_input("Enter the author: ")
                            publisher = get_input("Enter the publisher: ")
                            res=new_book_transaction.add_book(title, author, publisher)
                            if res:
                                print("Book added successfully")
                            else:
                                print("Book could not be added.Please try again")

                        case "4":
                            barcode = get_input("Enter the book barcode to delete: ")
                            res=new_book_transaction.delete_book(barcode)

                            if (res):
                                print("Book deleted successfully")
                            else:    
                                print("Book could not be found")
                        case "3":
                            title = get_input("Enter the book title to search: ")
                            res=new_book_transaction.search_book(title)
                            if (res):
                                print(f"Title: {res['Book_Title']}\nAuthor: {res['Author']}\nPublisher: {res['Publisher']}\nBarcode: {res['Barcode']}")
                            else:
                                print("Book not found")
                        case "0":
                            break
                        case _:
                            print("Invalid option, please try again")
                    
                
            elif option == "0":
                print("Thank you for using the Library System")
                break
            else:
                print("Please input a number between 0 - 2")
            
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main_menu()