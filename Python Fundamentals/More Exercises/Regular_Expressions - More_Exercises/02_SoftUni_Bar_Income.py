import re

pattern = r"%(?P<name>[A-z][a-z]+)%([^\|\$\%\.]?)+<(?P<product>\w+)>([^\|\$\%\.]?)+\|(?P<count>\d+)\|([^\|\$\%\.0-9]?)+(?P<price>\d+\.?\d+)\$"
total_income = 0
text = input()

while not text == 'end of shift':
    match = re.match(pattern, text)
    if match:
        x = match.groupdict()
        print(f"{x['name']}: {x['product']} - {int(x['count']) * float(x['price']):.2f}")
        total_income += int(x['count']) * float(x['price'])

    text = input()
print(f'Total income: {total_income:.2f}')



import re

pattern = r'%(?P<name>[A-Z][a-z]+)%[^\|\$\%\.]*<(?P<product>[\w]+)>[^\|\$\%\.]*\|(?P<count>\d+)\|([^\|\$\%\.]*?(?P<price>\d+\.\d+|\d+)\$)'

Total_income = 0
while True:

    command = input()
    if command == "end of shift":
        break
    matches = re.finditer(pattern, command)

    for m in matches:
        Total_income += int(m.group('count')) * float(m.group('price'))
        price = int(m.group('count')) * float(m.group('price'))
        print(f"{m.group('name')}: {m.group('product')} - {price:.2f}")
print(f"Total income: {Total_income:.2f}")







# import re
#
# pattern = \
# 	r"^(%(?P<name>[A-Z][a-z]+)%).*(<(?P<product>\w+)>).*" \
# 	r"(\|(?P<count>\d+)\|)([^\d]*)((?P<price>\d+(\.\d+)?)\$)$"
# total = 0
#
# data = input()
# while not data == "end of shift":
# 	match = re.match(pattern, data)
# 	if match:
# 		name, product = match.group("name"), match.group("product")
# 		cost = int(match.group("count")) * float(match.group("price"))
# 		print(f"{name}: {product} - {cost:.2f}")
# 		total += cost
# 	data = input()
#
# print(f"Total income: {total:.2f}")






# import re
#
#
# cust_pattern = r'(?<=\%)([A-Z][a-z]+)(?=\%)'
# prod_pattern = r'(?<=\<)([\w]+)(?=\>)'
# count_pattern = r'(?<=\|)([\d]+)(?=\|)'
# price_pattern = r'([\d]+(\.[\d]+)?)(?=\$)'
# income = 0
# while True:
#     data = input()
#     if data == 'end of shift':
#         break
#     m_cust = re.search(cust_pattern, data)
#     m_prod = re.search(prod_pattern, data)
#     m_count = re.search(count_pattern, data)
#     m_price = re.search(price_pattern, data)
#     if m_cust and m_prod and m_count and m_price:
#         customer = m_cust.group()
#         product = m_prod.group()
#         count = int(m_count.group())
#         price = float(m_price.group())
#     else:
#         continue
#     total=count*price
#     print(f'{customer}: {product} - {total:.2f}')
#     income += total
#
# print(f'Total income: {income:.2f}')