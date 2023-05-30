import Contact as Contact
from AddressBook import AddressBook

looping_menu_status="y"

def menu(menu):
    contact = Contact

    if menu == "1":
        contact.name = input("Input the name : ")
        contact.phone_number = input("\nInput the phone number : ")

        AddressBook.add_contact(contact.name, contact.phone_number)
    
    if menu == "2":
        contact.name = input("Input name : ")

        AddressBook.remove_contact(contact.name)
    
    if menu == "3" :
        contact.name = input("Input name : ")

        AddressBook.search_contact(contact.name)

    if menu not in ["1", "2", "3"]  :
        print("Wrong choice!")
    
    return menu

while(looping_menu_status=="y"):    
    menu_number=input("\nInput menu 1. Add Contact 2. Remove Contact 3. Search Contact : ")
    
    menu(menu_number)

    looping_menu_status=input("\nApa anda ingin mengulang(y/n) : ")