class vowels:
    vowel_chars = "AEUIOY"

    def __init__(self, text):
        self.text = text
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.text):
            if self.text[self.idx].upper() not in self.vowel_chars:
                self.idx += 1
                continue

            value_to_return = self.text[self.idx]
            self.idx += 1
            return value_to_return

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
 print(char)


'''  ----  Whit Generator Expression  ----  '''
# class vowels:
#     vowel_chars = "AEIUYOaeiuyo"
#
#     def __init__(self, text):
#         self.text = text
#         self.index = 0
#
#     def __iter__(self):
#         return (x for x in self.text if x in self.vowel_chars)
#
#
#
# my_string = vowels('Abcedifuty0o')
#
# for char in my_string:
#     print(char)