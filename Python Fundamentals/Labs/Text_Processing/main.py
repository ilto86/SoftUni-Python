# x = 'apples'
# y = 'lemons'
# w = 'strawberrys'
# z = "In the basket are %a, %a and %a" % (w, x, y)
# print(z)


# x = 'apples'
# y = 'lemons'
# w = 'strawberrys'
# z = "In the basket are {}, {} and {}".format (w, x, y)
# print(z)


# x = 'apples'
# y = 'lemons'
# w = 'strawberrys'
# z = f"In the basket are {w}, {x} and {y}"
# print(z)

#  Slice --->  [Начало : Край : Стъпка] ---> [1:], [:1], [1:5:2]
# text = "My name is Peter"
# name = text[-5:]
# new_name = text[11:]
# new_text = text[slice(-5, 16, 1)]
# print(name)
# print(new_name)
# print(new_text)



# String Methods

a = '1'.isdigit()  #  True
b = 'p'.isdigit()  #  False
c = 'P'.isupper()  #  True
d = 'P'.islower()  #  False
e = 'u'.islower()  #  True
f = "hello".upper() # "HELLO"
g = "HeLLo".lower() # "hello"


# Remove white spaces in start/end or both: strip()
#       rstrip(), lstrip()
" hello ".lstrip()  # "hello "
" hello ".rstrip()  # " hello"
" hello ".strip()  # "hello"



# Replace
# You can use the replace() method to replace all occurrences of a specified phrase with another specified phrase
txt = "I like bananas"
print(txt.replace("bananas", "apples"))  # I like apples

# If you only want to replace a certain number of phrases, add count
txt = "I like bananas bananas bananas"
x = txt.replace("bananas", "apples", 2)  # I like apples apples bananas
print(x)