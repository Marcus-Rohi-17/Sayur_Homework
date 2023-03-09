'''
Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''
items = ["Coffee", "Tea", "Muffin", "Sandwich"]
stock = [50, 30, 20, 10]
sales = [0, 0, 0, 0]
profits = [1.50, 1.00, 2.00, 3.50]

def print_items():
    print("\nMenu:")
    for i in range(len(items)):
        print(f"{items[i]}: {stock[i]}")

def restock():
    for i in range(len(items)):
        if stock[i] <= 0:
            print(f"{items[i]} is out of stock!")
        elif stock[i] <= 0.2*stock[i]:
            print(f"{items[i]} stock is running low. Restocking...")
            stock[i] = 50
                
def sell(item, quantity):
    if item not in items:
        print(f"Sorry, we don't have {item} on the menu.")
    else:
        i = items.index(item)
        if stock[i] == 0:
            print(f"Sorry, we are out of {item}.")
        elif stock[i] < quantity:
            print(f"Sorry, we only have {stock[i]} {item}(s) left.")
        else:
            stock[i] -= quantity
             
            sales[i] += quantity
            revenue = profits[i] * quantity
            print(f"You bought {quantity} {item}(s) for {revenue:.2f}$. Thank you for your purchase!")
            
def print_summary():
    print("\nInventory Summary:")
    for i in range(len(items)):
        print(f"{items[i]}: {stock[i]}")
    # print_sales()
    # print_profits()
 

print_items()
item = input("enter the item: ")
quantity = int(input("enter the quantity: "))
sell(item,quantity)
#print_profits()
print_summary()

