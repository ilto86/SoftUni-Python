# import re

# text= input()

# matches = re.findall(r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b", text)

# print(", ".join(matches))




# text= input()
#
# matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)
#
# output = list()
# for match in matches:
#     output.append(match.group())
# print(", ".join(output))



# pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})"
# text = input()
#
# matches = re.finditer(pattern, text)
# valid_phones = [match.group() for match in matches]
# print(", ".join(valid_phones))




import re

text = input()

pattern = r"\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b"   # "\+359 2 [0-9]{3} [0-9]{4}\b|\+359\-2\-[0-9]{3}\-[0-9]{4}\b"
matches = re.findall(pattern, text)

print(", ".join(matches))
