#Task 1: Restaurant Menu Update

# Initial restaurant menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# 1. Add a new category "Beverages" with two items
restaurant_menu["Beverages"] = {"Coffee": 2.99, "Tea": 2.50}

# 2. Update the price of "Steak" to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# 3. Remove "Bruschetta" from "Starters"
restaurant_menu["Starters"].pop("Bruschetta")

# Display the updated menu
print("Updated Restaurant Menu:")
for category, items in restaurant_menu.items():
    print(f"\n{category}:")
    for item, price in items.items():
        print(f"  {item}: ${price:.2f}")
