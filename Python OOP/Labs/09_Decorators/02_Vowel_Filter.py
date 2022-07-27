def vowel_filter(function):
    def wrapper():
        letters = function()
        return [char for char in letters if char.lower() in "aeyuio"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())

@vowel_filter
def get_other_letters():
    return ["S", "o", "f", "t", "U", "n", "i", "v", "e", "r", "s", "I", "t", "y"]
print(get_other_letters())