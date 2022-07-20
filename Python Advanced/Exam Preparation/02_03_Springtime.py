def start_spring(**kwargs):
    result = ''
    spring_objects = {}
    for value, key in kwargs.items():
        if key not in spring_objects:
            spring_objects[key] = [value]
        else:
            spring_objects[key].append(value)
    # sorted by their number of values in descending order -len(x[1] and when have same number of values in them, return them in ascending order (alphabetically) by the type's key x[0]
    sorted_spring = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0])) # sorted gives [list with (tuple)], in (tuple key "string" and [value list])
    for spring_elements in sorted_spring:
        type_name = spring_elements[0]
        objects_name = spring_elements[1]
        sorted_objects = sorted(objects_name) #  sorted in ascending order (alphabetically) by the object's name.
        result += f"{type_name}:\n"
        for object in sorted_objects:
            result += f"-{object}\n"

    return result

example_objects = {"Water Lilly": "flower",
 "Swifts": "bird",
 "Callery Pear": "tree",
 "Swallows": "bird",
 "Dahlia": "flower",
 "Tulip": "flower",}
print(start_spring(**example_objects))

'''Output must to be ----->     flower:
                                -Dahlia
                                -Tulip
                                -Water Lilly
                                bird:
                                -Swallows
                                -Swifts
                                tree:
                                -Callery Pear
'''


example_objects = {"Swallow": "bird",
 "Thrushes": "bird",
 "Woodpeckers": "bird",
 "Swallows": "bird",
 "Warblers": "bird",
 "Shrikes": "bird",}
print(start_spring(**example_objects))

'''Output must to be ----->     bird:
                                -Shrikes
                                -Swallow
                                -Swallows
                                -Thrushes
                                -Warblers
                                -Woodpeckers 
'''


example_objects = {"Magnolia": "tree",
 "Swallow": "bird",
 "Thrushes": "bird",
 "Pear": "tree",
 "Cherries": "tree",
 "Shrikes": "bird",
 "Butterfly": "insect"}
print(start_spring(**example_objects))

'''Output must to be ----->     bird:
                                -Shrikes
                                -Swallow
                                -Thrushes
                                tree:
                                -Cherries
                                -Magnolia
                                -Pear
                                insect:
                                -Butterfly
'''