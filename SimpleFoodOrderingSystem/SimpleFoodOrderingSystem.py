from menu_item import MenuItem

menu_item1 = MenuItem('Sandwich', 5)
menu_item2 = MenuItem('Chocolate cake', 4)
menu_item3 = MenuItem('Coffe', 3)
menu_item4 = MenuItem('Orange Juice', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('Enter order number: '))
selected_menu = menu_items[order]
print('Selected Items: ' + selected_menu.name)

# Terima input dari console, dan Berikan input ke variable count
count = int(input("Order Quantity (discount 10% for 3 or more): "))

# Panggil method get_total_price
result = selected_menu.get_total_price(count)

# Cetak 'Total harga adalah $____'
print("Total price is $ " + str(result))
