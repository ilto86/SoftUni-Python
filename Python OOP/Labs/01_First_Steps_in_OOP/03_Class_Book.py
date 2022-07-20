class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.name}" by {self.author} has {self.pages} pages'


b = Book('Harry Potter and GoF', 'J.K. Rowling', 500)

print(b)
print(str(b))  # this calls `__str__`
print(b.name)
print(b.author)
print(b.pages)





# class Book:
#     def __init__(self, name: str, author: str, pages: int):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#
# book = Book("My Book", "Me", 200)
# print(book.name)
# print(book.author)
# print(book.pages)