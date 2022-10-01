bag = {'torch': 1, 'sword': 6, 'rupees': 6000000, 'pocket dragon': 1, 'bow': 1, 'arrow': 100}

def displayInventory(inventory):
    print("inventory:")
    item_total = 0
    for k, v in bag.items():
        item_total = item_total + v.get(inventory, 0)
    print("This is what you got in that bag:" + str(item_total))

displayInventory(bag)