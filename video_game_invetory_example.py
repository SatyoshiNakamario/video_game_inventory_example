##Fun inventory creation to practice Python. Special thanks to Automate the Bording Stuff with Python authors and CodeCoolGlobal Github.##

import csv 

#what you always have in your inventory
bag = {'torch': 1, 'sword': 6, 'rupees': 6000000, 'pocket dragon': 1, 'bow': 1, 'arrow': 100}

def displayInventory(inventory):
    print("This is what you got in that bag:\n")
    for item in inventory:
    
        print(f"{item}:{inventory[item]}")

        print("\n")


def add_to_inventory(inventory, added_items):

    #how to create a new item
    for new_item in inventory:
        if new_item not in inventory:
            inventory.update({new_item:0})

    #add item to file
    for item in inventory:
        for item in loot:
            if item ==new_item:
                inventory += 1


#new items from a loot of sorts

loot = ['shield', 'dagger', 'pocket dragon', 'arrow', 'rupees']

add_to_inventory(bag, loot)
displayInventory(bag)

#function to add the items and their amount in a table

def print_table(inventory, order=None):

    #making it pretty with the new lines, items' names and counts
    print("-----------------\n")
    print("item name | count\n")
    print("-----------------\n")

    #sorting ascending values

    if order == "count, asc":
        inventory = sorted(inventory.items(), key = lambda count: count[1])
        inventory = dict(inventory)

    #sorting descending values

    if order == "count, desc":
        inventory = sorted(inventory.items, key = lambda count: count[1], reverse = True)
        inventory = dict(inventory)

    #creating the rows
    for i, c in inventory.items():
        print(f"{i:>9} |  {c:>4}\n")
        # print("".join(i.ljust(max_item_name) for c in i))

    print("-----------------\n")


print_table(bag, "count, desc")
    





displayInventory(bag)