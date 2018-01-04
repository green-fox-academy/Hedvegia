
# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

shop_items = ["Cupcake", 2, "Brownie", False]

for n, i in enumerate(shop_items):
    if i == 2:
        shop_items[n] = "Croissant"
    elif i == False:
        shop_items[n] = "Ice Cream"

print(shop_items)
    
