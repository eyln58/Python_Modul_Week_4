
import json
import os


def member_file_read():
    if not os.path.exists ("Library_system/member.json") or os.path.getsize("Library_system/member.json") == 0:
        print("No members found! Please add a member.")
        return []
    with open("Library_system/member.json", "r", encoding="utf-8", errors="ignore") as json_file:
        try :
            saved_members = json.load(json_file)
            
            
        except json.JSONDecodeError as e:
            print("An error occurred while reading the file: ", e)
        finally:
            
            return saved_members
     
        


def member_file_write(saved_members):
    with open("Library_system/member.json", "w", encoding="utf-8") as json_file:
        json.dump(saved_members, json_file, ensure_ascii=False, indent=4)

def generate_unique_id(saved_members):

    if not saved_members:
        return 1

    max_id = max(member["member_ID"] for member in saved_members)
    return max_id + 1

def member_control():
    saved_members = member_file_read()
    if saved_members:
        print("---All Members---")
        for member in saved_members:
            print(
                f" ID : {member['member_ID']}\t "
                f"name: {member['member_name']}\t "
                f" phone_number : {member['phone_number']}\t"
                f" address : {member['address']}"
            )
        return True
    else:
        print("No members found!")
        return False

def add_new_member(member_name, phone_number, address):
    saved_members = member_file_read()

    for mem in saved_members:
        if mem["phone_number"] == phone_number:
            print(f"Phone number {phone_number} already exists!")
            return

    new_id = generate_unique_id(saved_members)
    
    member_dict = {
        "member_ID": new_id,
        "member_name": member_name,
        "phone_number": phone_number,
        "address": address
    }
    
    saved_members.append(member_dict)
    try:
        member_file_write(saved_members)
        print(f"Member {member_name} has been added successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while saving the member: {e}")
        return False

def members_search (phone_number,inter=0):
    
    saved_members = member_file_read()
    if saved_members:
        for member in saved_members:
            if phone_number == member["phone_number"]:
                if inter==0:

                    print(
                        f"ID: {member['member_ID']} | "
                        f"Name: {member['member_name']} | "
                        f"Phone: {member['phone_number']} | "
                        f"Address: {member['address']}"
                    )
                
                
                    return True
                else:
                    
                    return member
        print("Member not found.")
    else:
        print("No members exist.")
        return False


def members_delete(phone_number):
    saved_members = member_file_read()
    if not saved_members:
        print("There are no members to delete.")
        return False

    
    found_member = None

    for member in saved_members:
        if phone_number == member.get("phone_number"):
            found_member = member
            break

    if found_member:
        confirm = input(
            f"Are you sure you want to delete the member '{found_member['member_name']}'? (Y/N): ").strip().upper()
        if confirm == "Y":
            saved_members.remove(found_member)
            member_file_write(saved_members)
            print(f"Member deleted successfully: {found_member['member_name']}")
            return True
        elif confirm == "N":
            print("Member deletion canceled.")
            return False
        else:
            print("Invalid choice. Member deletion canceled.")
            return False
    else:
        print("Member not found.")
        return False
def member_update(phone):
    try:
        saved_members = member_file_read()
        if not saved_members:
            print("No members found!")
            return

        #name = input("Enter the name of the member to update: ").strip()
        for member in saved_members:
            if phone == member["phone_number"]:
                phone_number = input("Enter the new phone number: ")
                address = input("Enter the new address: ")

                member["phone_number"] = phone_number
                member["address"] = address

                member_file_write(saved_members)
                print(f"Member updated successfully: {member['member_name']}")
                print(f"New address: {member['address']}")
                print(f"New phone number: {member['phone_number']}")
                return True
        print("Member not found.")
    except ValueError:
        print("Invalid input. Please enter a name.")
        return False