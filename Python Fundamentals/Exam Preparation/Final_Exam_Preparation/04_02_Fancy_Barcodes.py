# import re
#
# number_of_iterations = int(input())
#
# for _ in range(number_of_iterations):
#     data = input()
#     pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
#     result = re.match(pattern, data)
#
#     if result is None:
#         print("Invalid barcode")
#     else:
#         extract_nums = re.findall(r'\d', result.group())
#
#         if not extract_nums:
#             print("Product group: 00")
#         else:
#             print(f"Product group: {''.join(extract_nums)}")





# import re
#
# count = int(input())
#
# for _ in range(count):
#     barcode = input()
#     pattern = r"([@][#]+)([A-Z][a-zA-Z0-9]{4,}[A-Z])\1"
#
#     matches = re.match(pattern, barcode)
#
#     if not matches:
#         print("Invalid barcode")
#
#     else:
#         nums_in_barcode = re.findall(r'\d', matches[2])
#
#         if not nums_in_barcode:
#             print("Product group: 00")
#         else:
#             print(f"Product group: {''.join(nums_in_barcode)}")





# import re
#
#
# numbers = int(input())
#
# for _ in range(numbers):
#     pattern = r"@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}"
#     text = input()
#     matches = re.findall(pattern, text)
#     product_group = ""
#     if matches:
#         for match in matches:
#             for num in match:
#                 if num.isdigit():
#                     product_group += num
#             if product_group:
#                 print(f"Product group: {''.join(product_group)}")
#             else:
#                 print("Product group: 00")
#     else:
#         print("Invalid barcode")




import re

numbers = int(input())

for _ in range(numbers):
    text = input()

    pattern = r"@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}"

    matches = re.findall(pattern, text)

    if matches:
        nums = re.findall(r"\d", text)

        if nums:
            print(f"Product group: {''.join(nums)}")
        else:
            print("Product group: 00")

    else:
        print("Invalid barcode")