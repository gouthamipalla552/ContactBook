contact={}
def display_contact():
      print("Name \t\t contact number")
      for key in contact:
          print("{} \t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input("\n 1.Add New contact \n 2.Search contact \n 3.Display contact \n 4.Edit contact \n 5.Delete contact \n 6.Exit \n Enter your choice"))
    if choice == 1:
        name= input("Enter the contact Name")
        phone=input("Enter the contact mobile number")
        contact[name]=phone
    elif choice == 2:
        search_name= input("Enter the contact name")
        if search_name in contact:
            print(search_name,"contact name is ",contact[search_name])
        else:
            print("name is not found in the contact book")
    elif choice == 3:
        if not contact:
            print("enter contact book")
        else:
            display_contact()

    elif choice == 4:
        edit_contact=input("enter the contact to be edited")
        if edit_contact in contact:
            phone=input("enter mobile number")
            contact[edit-contact]=phone
            print("contact update")
            display_contact()
        else:
            print("name is not found  in the contact book")
    elif choice == 5:
        del_contact = input("enter the contact to be deleted")
        if del_contact in contact:
            confirm=input("do you want yo delete this contact y/n?")
            if confirm=='y'or confirm=='Y':
                contact.pop(del_contact)
            display_contact()


        else:
            print("name is not found in contact book")


    else:
        break


                


            






















        
