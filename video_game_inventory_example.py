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
            if item == new_item:
                inventory[item] += 1


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
        inventory = sorted(inventory.items(), key = lambda count: count[1], reverse = True)
        inventory = dict(inventory)

    #creating the rows
    for i, c in inventory.items():
        print(f"{i:>9} |  {c:>4}\n")
        # print("".join(i.ljust(max_item_name) for c in i))

    print("-----------------\n")


print_table(bag, "count, desc")

#function to update file with inventory of items

def import_inventory(inventory, filename="import_inventory.csv"):

    items_from_file = []

    #list from file
    f = open(filename, "r")
    file_line = f.readlines()

    for it in file_line:
        list_from_file_items = it.split(",")
        for item in list_from_file_items:
            items_from_file.append(item)

    #for new items
    for item_f in items_from_file:
        if item_f not in inventory:
            inventory.update({item_f: 0 })

    #for items already in list, add the amount to the record

    for item in inventory:
        if item_f in items_from_file:
            if item == item_f:
                inventory[item] += 1


#create a test/default inventory and import file
import_inventory(bag, "test_inventory.csv")

#print table with updated data
print_table(bag, "count, desc")

#create a list of values of the inventory
list_values_inventory = (list, bag.values())

#create a list with keys for items in the inventory
list_key_inventory = list(bag)

#function to export all items and values to a new csv
def export_inventory(inventory, filename="export_inventory.csv"):

    with open("export_inventory.csv", mode="w") as items_export_file:

        #create template formate

        csv_fields = ["item_name", "number_of_items"]

        #settings for where the file is exported

        items_to_write = csv.DictWriter(items_export_file, fieldnames=csv_fields)

        #a loop to create a row for each item in inventory

        i = 0
        while i < len(list_key_inventory):
            items_to_write.writerow({"item_name": list_key_inventory[i], "number_of_items": list_values_inventory[i]})
            i += 1
export_inventory(bag)