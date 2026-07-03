Menu = {
    'Expresso': 120,
    'Cappuccino': 150,
    'Latte': 200,
    'Americano': 150
}
print("Welcome to COFFEE CAFE")
print("Expresso=Rs120\nCappuccino=Rs150\nLatte=Rs200\nAmericano=Rs150")
order_total = 0
item_1 = input("Enter the item  you want to order = ")
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"your item{item_1}has been added to you order")
else:
    print(f"please order something else we can serve you {item_1} is not available")
another_order = input("Do you want to add another item? (yes/No)")
if another_order == "yes":
    item_2 = input("Enter the item you want to order= ")
    if item_2 in Menu:
        order_total += Menu[item_2]
        print(f"your item{item_2}has been added to you order") 
    else:
        print(f"please order something else we can serve you {item_2} is not available")
print(f" The total amount to pay is {order_total}")
