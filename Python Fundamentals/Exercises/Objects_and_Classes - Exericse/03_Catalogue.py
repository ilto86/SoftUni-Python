# class Catalogue:
#     products = []
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def add_product(self, product_name: str):
#         Catalogue.products.append(product_name)
#
#     def get_by_letter(self,first_letter: str):
#         return [el for el in Catalogue.products if el.startswith(first_letter)]
#
#     def __repr__(self):
#         returned_string =  f"Items in the {self.name} catalogue:\n"
#         returned_string += '\n'.join(sorted(Catalogue.products))
#         return  returned_string



# class Catalogue:
#     def __init__(self, name: str):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product_name: str):
#         self.products.append(product_name)
#
#     def get_by_letter(self,first_letter: str):
#         return [el for el in self.products if el.startswith(first_letter)]
#
#     def __repr__(self):
#         returned_string =  f"Items in the {self.name} catalogue:\n"
#         returned_string += '\n'.join(sorted(self.products))
#         return  returned_string
#
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)



class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)
        self.products.append(product_name)

    def get_by_letter(self,first_letter: str):
        return [el for el in self.products if el.startswith(first_letter)]

    def __repr__(self):
        returned_string =  f"Items in the {self.name} catalogue:\n"
        returned_string += '\n'.join(sorted(self.products))
        return  returned_string

catalogue = Catalogue("Mebeli")
catalogue1 = Catalogue("Technika")
catalogue.add_product("Divan")
catalogue.add_product("Leglo")
catalogue1.add_product("Televizor")
catalogue1.add_product("Hladilnik")
print(Catalogue.products)
print(catalogue.products)
print(catalogue1.products)