from json import dumps

def makeingredient(ingredient, inventory):
    inventoryDict = {}

    for i in inventory:
        if i not in inventoryDict:
            inventoryDict[i] = 1
        else:
            inventoryDict[i] += 1

    print(dumps(inventoryDict, indent=4))
    for i in ingredient:
        if i in inventoryDict:
            inventoryDict[i] -= 1
            if inventoryDict[i] == -1:
                return False
        else:
            return False
    return True


ingredient = ['apple','crust','orange']
inventory = ['apple','crust','orange','crust','orange']

makeingredient(ingredient, inventory)
