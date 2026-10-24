expenses = []
def add_expense():
    name = input("enter your item :")
    while True:
        try:
            price = int(input("enter your price :"))
        except ValueError:
            print("please enter a number!")
            continue
        else:
            if price >= 0:
                break
            else:
                print("dont enter negative number!")
                continue
    expe = {
            "name":name,
            "price":price
            }
    expenses.append(expe)
def show_expenses():
    for i,expe in enumerate(expenses,start=1):
        print(i,expe["name"],expe["price"])
def cal_total():
    total = 0
    for expe in expenses:
        total = total + expe["price"]
    return total
def highest_expense():
    highest = expenses[0]["price"]
    highest_n = expenses[0]["name"]
    for expe in expenses:
        if highest < expe["price"]:
            highest = expe["price"]
            highest_n = expe["name"]
    return highest,highest_n
def search():
    search_item = input("enter your item:")
    found = False
    for expe in expenses:
        if search_item in expe["name"]:
            print("found - ",expe["name"],"-",expe["price"])
            found = True
    if found == False:
        print("not found")
def delete_expense():
    for i,expe in enumerate(expenses,start=1):
        print(i,"-",expe["name"],"-",expe["price"])
    dele = int(input("choose your item to delete :"))
    if 1 <= dele <= len(expenses):
        expenses.pop(dele - 1)
    else:
        print("please enter valid choice!")
def menu():
    while True:
        print("1 - Add expense")
        print("2 - Show expenses")
        print("3 - Show total")
        print("4 - Highest expense")
        print("5 - Search")
        print("6 - Delete expense")
        print("7 - Exit")
        try:
            choice = int(input("enter your choice :"))
        except ValueError:
            print("please enter a number!")
            continue
        if choice == 1:
            add_expense()
        elif choice == 2:
            if expenses != []:
                show_expenses()
            else:
                print("no expenses found!")
        elif choice == 3:
            if expenses != []:
                result_total = cal_total()
                print("majmo:",result_total)
            else:
                print("no expenses found")
        elif choice == 4:
            if expenses != []:
                result_highest = highest_expense()
                print("gerantarin :",result_highest[0],"-",result_highest[1])
            else:
                print("no expenses found!")
        elif choice == 5:
            search()
        elif choice == 6:
            if expenses != []:
                delete_expense()
            else:
                print("no expenses found!")
        elif choice == 7:
            print("exiting ...")
            break
        else:
            print("ivalid choice!")
# menu()
print("git practice")
print("new change")
print("another change")
print("only in git-practice")
print("only in master")
print("Learning Git push")
print("Git review practice")