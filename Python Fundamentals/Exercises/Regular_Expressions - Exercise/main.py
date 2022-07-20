import re

# text = 'The movie was very good but Scary'
# result = re.search('^The.*Scary$', text)
# print(result)


# text = 'The weather in Spain is nice'
# result = re.findall('in', text)
# print(result)


# text = 'The price of OLIVEOIL is 4 leva'
# result = re.search(r'(\b[A-Z]+\b).+(\b\d+)', text)
# print(result.groups())
# print(result.group(1))
# print(result.group(2))



# FLAGS ---->  re.IGNORECASE
text = 'MArio is Python developer at a BioPharmacy. Mario loves ML and AI and mArIo is not Super mARIO'
result = re.findall('Mario', text, re.IGNORECASE)
print(result)


# FLAGS ---->  re.X  re.VERBOSE
text = 'Mario is Python developer at a BioPharmacy, his age is 32'
result = re.search(r'''(^\w{5}) # match 5 letters at the start
                       .+(\d{2}$) # match 2 digits at the end''', text, re.VERBOSE) # re.X
print(result.group(1))
print(result.group(2))



# FLAGS ----> re.M   re.MULTILINE

text = 'Mario is Python developer at a BioPharmacy, his age is 32'
result = re.findall(r'^\w{3}', text, re.MULTILINE) # re.M
print(result)
result = re.findall(r'\d{2}$', text, re.MULTILINE) # re.M
print(result)