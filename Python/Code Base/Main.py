class Node:
    def __init__(self, serial, price, name):
        self.serial = serial
        self.price = price
        self.name = name
        self.next = None

serial = 1
total = 0
head = None
temp = None
name1, address1, email1, phone1 = "", "", "", ""

def taking_input():
    global serial
    global temp
    name = input("\nEnter the item name: ")
    price = int(input("Enter the price: "))
    create(name, price)

def create(name, price):
    global serial
    global head
    global temp

    new_node = Node(serial, price, name)
    serial += 1

    if head is None:
        head = temp = new_node
    else:
        temp.next = new_node
        temp = new_node

    choice = int(input("\nDo you want to add more items? (1 for yes, 0 for no): "))
    if choice == 1:
        taking_input()

def display_menu():
    global head
    temp_node = head
    if temp_node is None:
        print("\nMenu is Empty!")
    while temp_node is not None:
        print(f"{temp_node.serial}\t\t{temp_node.name}\t\t\t{temp_node.price}")
        temp_node = temp_node.next

def order():
    global head
    global temp
    global total
    item = int(input("\nSelect the item: "))
    temp_node = head

    while temp_node.serial != item:
        temp_node = temp_node.next

    num_items = int(input(f"\nHow many {temp_node.name} do you want: "))
    bill = temp_node.price * num_items
    print(f"\nYour Bill for {num_items} no of {temp_node.name} is: {bill}")
    total += bill

    choice = int(input("\nDo you want to order more? (1 for yes, 0 for no): "))
    if choice == 1:
        order()

def choice():
    print("\n\nWe provide two types of orders:")
    print("1. By Hotel\n2. By Food\n3. Exit")
    n = int(input("\nEnter your choice: "))

    if n == 1:
        by_hotel()
    elif n == 2:
        by_food()
    elif n == 3:
        exit(1)
    else:
        print("\nPlease press the right key.")
        choice()

def by_hotel():
    print("\n1. Hotel Shreyan\n2. Tasty\n3. Tris Planet\n4. Lets Eat\n5. Dhakeshwari Restaurant\n6. Go to the choice\n7. Exit")
    choic = int(input("\nSelect the hotel name: "))
    if choic in range(1, 6):
        print("\n<---------THIS IS OUR MENU--------->\n")
        display_menu()
        order()
    elif choic == 6:
        choice()
    elif choic == 7:
        print("\nTHANK YOU FOR VISITING US \n")
        exit(1)
    else:
        print("\nPLEASE ENTER THE CORRECT CHOICE\n")
        by_hotel()

    print("\nGO TO THE PAYMENT GATEWAY (press 1) ->> ")
    n = int(input())
    if n == 1:
        payment()

def by_food():
    print("\n<-----------THIS IS OUR MENU----------->\n")
    display_menu()
    order()

    print("\nGO TO THE PAYMENT GATEWAY (press 1) ->> ")
    n = int(input())
    if n == 1:
        payment()

def payment():
    print("\n1. ONLINE PAYMENT\n2. CASH ON DELIVERY")
    n = int(input("ENTER YOUR CHOICE: "))

    if n == 1:
        print("\n1. PAYTM\n2. PHONEPAY\n3. GPAY\n4. CARD PAY")
        a = int(input("ENTER YOUR CHOICE: "))
        if a in range(1, 5):
            print("\nTHANK YOU !!!!!!! YOU WILL GET YOUR DELICIOUS FOOD JUST AFTER 30-40 MINUTES \n")
        else:
            print("PLEASE SELECT THE CORRECT OPTION\n")
            payment()
    elif n == 2:
        print("\nTHANK YOU !!!!!!! YOU WILL GET YOUR DELICIOUS FOOD JUST AFTER 30-40 MINUTES \n")
    else:
        print("PLEASE SELECT THE CORRECT OPTION\n")
        payment()

    c = int(input("WOULD YOU WANT TO GENERATE YOUR INVOICE? (press 1 for yes, 0 for no): "))
    if c == 1:
        invoice()
    else:
        print("\n THANK YOU!!! PLEASE COME AGAIN...")

def invoice():
    global total
    total2 = total + int(total * 0.18)
    print("\n\n\t|---------------------------------------------------------------------|")
    print("\t\t			 YOUR INVOICE				 ")
    print("\t|---------------------------------------------------------------------|\n")
    print(f"Name: {name1}\nAddress: {address1}\nPhone: {phone1}\nEmail: {email1}")
    print(f"\nYOUR TOTAL BILL IS--> {total2} (including 18 percent GST)\n")
    print("\n THANK YOU!!! PLEASE COME AGAIN...")


def OwnerLogin():
    global name1, email1, phone1
    print("\033[0;32m")
    name2 = input("\nEnter your name: ")
    phone2 = input("Enter your phone number: ")
    email2 = input("Enter your email: ")
    password2 = input("Enter your password: ")
    # You can use these values as needed, or store them in global variables for further use
    name1, email1, phone1 = name2, email2, phone2

def CustomerLogin():
    global name1, address1, email1, phone1
    print("\033[0;34m")
    name = input("\nEnter your name: ")
    address = input("Enter your full address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    name1, address1, email1, phone1 = name, address, email, phone



if __name__ == "__main__":
    print("\033[1;31m")
    print("\t\t\t|--------------------------------------------------------------------|")
    print("\t\t\t|                WELCOME TO THE FOOD DELIVERY SYSTEM                 |")
    print("\t\t\t|--------------------------------------------------------------------|\n")
    print("\nGo to the Owner Login Page ->> ")
    OwnerLogin()
    print("\033[1;32m")
    print("\n\aYOU HAVE LOGGED IN TO THE DELIVERY SYSTEM SUCCESSFULLY\n")
    print("\033[1;31m")
    print("\n\n\aPlease Insert Your Menu Items -->> \n")
    taking_input()
    print("\033[1;32m")
    print("\n\aYou Have Successfully Inserted Your Menu Items \n\n")
    print("\033[1;31m")
    print("\n\aGo to the Customer Login Page ->> ")
    CustomerLogin()
    print("\033[1;32m")
    print("\n\aYOU HAVE LOGGED IN TO THE DELIVERY SYSTEM SUCCESSFULLY")

    choice()