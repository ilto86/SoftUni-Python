'''
This function sorts the cheeses by their quantity descending,
then by name ascending,
Concats the string with the result and sorts the elements of the result.quantity descending for each cheese
return str --> the sorted result
:param kwargs:
'''

# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
#     result = ''
#     for name, quantities in sorted_cheeses:
#         result += name + "\n"
#         sorted_quantities = sorted(quantities, reverse=True)
#         result += "\n".join([str(el) for el in sorted_quantities]) + "\n"
#     return result


def sorting_cheeses(**cheeses_dict):
    result = ''
    cheeses_dict = sorted(cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in cheeses_dict:
        result += tuple_[0] + "\n"
        quantities_list = sorted(tuple_[1], reverse=True)
        result += "\n".join(map(str, quantities_list))
        result += "\n"
    result = result.strip()
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
 sorting_cheeses(
 Parmigiano=[165, 215],
 Feta=[150, 515],
 Brie=[150, 125]
 )
)