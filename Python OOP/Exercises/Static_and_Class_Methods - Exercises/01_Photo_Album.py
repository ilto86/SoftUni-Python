# from math import ceil
#
#
# class PhotoAlbum:
#     PHOTOS_PER_PAGE_LIMIT = 4
#
#     def __init__(self, pages: int):
#         self.pages = pages
#         self.photos = self.__init_photos(pages)
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE_LIMIT)
#         return cls(pages)
#
#     def add_photo(self, label: str):
#         for index, page in enumerate(self.photos):
#             if len(page) < PhotoAlbum.PHOTOS_PER_PAGE_LIMIT:
#                 page.append(label)
#                 return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
#         return "No more free slots"
#
#     def display(self):
#         separator = "-" * 11
#         result = separator + "\n"
#         for page in self.photos:
#             result += " ".join(["[]" for _ in page]) + "\n"
#             result += separator + "\n"
#         return result.strip()
#
#     def __init_photos(self, pages):
#         results = []
#         for _ in range(pages):
#             results.append([])
#         return results
#         # return [[] for _ in range(pages)]


# album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.display())


from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.build_photos()

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        delimeter = "-" * 11
        result = delimeter + "\n"

        for page in self.photos:
            page_str = " ".join(["[]" for _ in page])
            result += page_str + "\n" + delimeter + "\n"
        return result.strip()

    def build_photos(self):
        results = []
        for _ in range(self.pages):
            results.append([] * self.PHOTOS_PER_PAGE)
        return results
        # return [[] for _ in range(pages)]


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())


'''Expected Output:

baby photo added successfully on page 1 slot 1
first grade photo added successfully on page 1 slot 2
eight grade photo added successfully on page 1 slot 3
party with friends photo added successfully on page 1 slot 4
[['baby', 'first grade', 'eight grade', 'party with friends'], []]
prom photo added successfully on page 2 slot 1
wedding photo added successfully on page 2 slot 2
-----------
[] [] [] []
-----------
[] []
-----------

'''

# TEST Inputs and Outputs:

photos_album = PhotoAlbum.from_photos_count(9)
print(photos_album.add_photo("my first game"))
print(photos_album.add_photo("my second game"))
print(photos_album.add_photo("my third game"))
print(photos_album.add_photo("my fourth game"))
print(photos_album.add_photo("my fifth game"))
print(photos_album.add_photo("my sixth game"))
print(photos_album.display())


'''Expected Output:

my first game photo added successfully on page 1 slot 1
my second game photo added successfully on page 1 slot 2
my third game photo added successfully on page 1 slot 3
my fourth game photo added successfully on page 1 slot 4
my fifth game photo added successfully on page 2 slot 1
my sixth game photo added successfully on page 2 slot 2
-----------
[] [] [] []
-----------
[] []
-----------

-----------

'''