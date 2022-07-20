def shopping_cart(*args):
    meal_products = {"Soup": [], "Pizza": [], "Dessert": []}
    result = ""
    for commands in args:
        if commands == "Stop":
            break
        meal_type = commands[0]
        product = commands[1]
        if meal_type not in meal_products:
            meal_products[meal_type] = [product]
        elif meal_type == "Soup" and len(meal_products["Soup"]) < 3 and product not in meal_products["Soup"]:
                meal_products[meal_type].append(product)
        elif meal_type == "Pizza" and len(meal_products["Pizza"]) < 4 and product not in meal_products["Pizza"]:
                meal_products[meal_type].append(product)
        elif meal_type == "Dessert" and len(meal_products["Dessert"]) < 2 and product not in meal_products["Dessert"]:
                meal_products[meal_type].append(product)
    if len(meal_products["Soup"]) == 0 and len(meal_products["Pizza"]) == 0 and len(meal_products["Dessert"]) == 0:
        return "No products in the cart!"

    sorted_meal_products = sorted(meal_products.items(), key=lambda x: (-len(x[1]), x[0]))
    for products in sorted_meal_products:
        meal_name = products[0]
        product_name = products[1]
        sorted_product = sorted(product_name) 	#  sorted in ascending order (alphabetically) by the product's name.
        result += f"{meal_name}:\n"
        for prod in sorted_product:
            result += f" - {prod}\n"

    return result



# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
