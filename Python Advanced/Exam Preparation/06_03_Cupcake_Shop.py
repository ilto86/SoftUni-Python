def stock_availability(cupcakes_lists, command, *args):
    if command == "delivery":
        cupcakes_lists.extend(args)
    else:
        if not args:
            cupcakes_lists.pop(0)
        elif type(args[0]) == int:
            for _ in range(args[0]):
                cupcakes_lists.pop(0)
        else:
            for cupcake in args:
                if cupcake in cupcakes_lists:
                    cupcakes_lists = list(filter(lambda x: x != cupcake, cupcakes_lists))

    return cupcakes_lists


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))



# Exception:
'''
['choco', 'vanilla', 'banana', 'caramel', 'berry'] 
['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
['vanilla', 'banana']
[]
['banana']
['cookie', 'banana']
['chocolate', 'vanilla', 'banana']
'''
