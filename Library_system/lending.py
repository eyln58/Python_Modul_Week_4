import json
import os
import time_management
import new_book_transaction 
import membership 

def write_tracking(data):

    try:
        with open('Library_system/tracking.json', 'w',encoding="utf-8") as file:
            json.dump(data, file,ensure_ascii=False ,indent=4)
    except Exception as e:
        print(f"An error occurred while saving: {e}")
        return []



def tracking_read():

    try:
        if not os.path.exists("Library_system/tracking.json") or os.path.getsize("Library_system/tracking.json") == 0:
            return []
        with open("Library_system/tracking.json", "r", encoding="utf-8", errors="ignore") as file:
            tracking_data = json.load(file)
            return tracking_data
    except FileNotFoundError:
        tracking_data = []
        return tracking_data
    

def lending_book(phone_number,barcode):

    now_time,return_time = time_management.generate_return_date()
    
    searchBook = new_book_transaction.search_book(barcode)
    member_ = membership.members_search(phone_number,inter=1)
    print(member_)
    print(searchBook)
    if member_ and searchBook:
        new_track = searchBook|member_
        new_track["lend_date"] = now_time
        new_track["return_date"] = return_time
        tracking_data=tracking_read()
            
        new_book_transaction.delete_book(barcode)
        tracking_data.append(new_track)

        write_tracking(tracking_data)
    else:

        print("Member or book not found")
    


def return_book(barcode):  # 

    tracked_books = tracking_read()
  
    books = new_book_transaction.read()

    for tracked_book in tracked_books:
       
        if tracked_book["Barcode"]==barcode:
            new_book = {
                    "Barcode": tracked_book["Barcode"],
                    "Book_Title": tracked_book["Book_Title"],
                    "Author": tracked_book["Author"],
                    "Publisher": tracked_book["Publisher"],
                }
        
            books.append(new_book)
            new_book_transaction.save(books)

    tracked_books = [book for book in tracked_books if book["Barcode"] != tracked_book["Barcode"]]
    
    
    write_tracking(tracked_books)


def view_lent_books():
    
    tracking_data = tracking_read()
    if tracking_data!=[]:
        sorted_data = sorted(tracking_data, key=lambda x: x['return_date'])

        
        for track in sorted_data:
            print(f" Member ID: {track['member_ID']}\n Member Name: {track['member_name']}\n Member Phone: {track['phone_number']}\n Member Address: {track['address']}\n\n Book Title: {track['Book_Title']}\n Author: {track['Author']}\n Publisher: {track['Publisher']}\n Barcode: {track['Barcode']}\n Lend Date: {track['lend_date']}\n Return Date: {track['return_date']}\n {"="*20}")
    else:

        print("There is book lended")

