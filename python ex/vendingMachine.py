milk_price = 1.20
curd_price = 1.00

print("Welcome TO Diary Vending Machine!!!")

user_input = input("Please select the product you want to buy milk, curd or both: ")
user_input = user_input.upper()
while True:

 if user_input == "milk":
    print("Thank you for selection!!")
    milk_quantity = int(input("Please enter the quantity you want to buy: "))
    milk_cost = milk_quantity * milk_price
    print("Kindly the pay amount in euros " + str(milk_cost) + " below")

    cus_paid = int(input("Enter the amount to be paid: "))
    if cus_paid == milk_cost:
        print("Thank you, Please collect" + user_input)
 elif user_input == "curd":
    print("Thank you for selection!!")
    curd_quantity = int(input("Please enter the quantity you want to buy: "))
    curd_cost = curd_quantity * curd_price
    print("Kindly the pay amount in euros " + str(curd_cost) + " below")

    cus_paid = int(input("Enter the amount to be paid: "))
    if cus_paid == curd_cost:
        print("Thank you, Please collect" + user_input)
 elif user_input == "both":
    print("Thank you for selection!!")
    milk_quantity = int(input("Please enter the quantity of milk you want to buy: "))
    milk_cost = milk_quantity * milk_price
    curd_quantity = int(input("Please enter the quantity of curd you want to buy: "))
    curd_cost = curd_quantity * curd_price
    total_cost = milk_cost + curd_cost
    print("Kindly the pay amount in euros " + str(total_cost) + " below")
    cus_paid = int(input("Enter the amount to be paid: "))
    if cus_paid == total_cost:
        print("Thank you, Please collect" + user_input)
    else:
        print("Please enter Valid amount!!")

 else:
    print(" Please enter a Valid selection...")
    break
