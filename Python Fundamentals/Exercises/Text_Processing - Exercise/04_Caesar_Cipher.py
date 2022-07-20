# def caesar_cipher(text):
#     result = [chr(ord(ch) + 3) for ch in text]
#     print("".join(result))
#
#
# text = input()
# caesar_cipher(text)



# text = input()
# encrypted_version = ""
#
# for char in text:
#     ascii_sum = ord(char) + 3
#     encrypted_version += chr(ascii_sum)
#
# print(encrypted_version)


# encrypted_version = [chr(ord(ch) + 3) for ch in input()]
# print("".join(encrypted_version))



print("".join([chr(ord(ch) + 3) for ch in input()]))