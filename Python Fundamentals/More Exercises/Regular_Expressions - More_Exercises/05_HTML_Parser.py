import re


data = input()
head_text = ''
body_text = ''

head_pattern = r'(?<=\<title\>)(?P<title>.*)(?=\</title\>)'
body_pattern = r'(?<=\<body)(?P<body>.*)(?=body\>)'
text_pattern = r'>([^<>]*)<'

m = re.search(head_pattern, data)
if m:
    head_text = m.group('title')

m = re.search(body_pattern, data)
if m:
    body_html = m.group('body')
    body_text = ''.join(re.findall(text_pattern, body_html))
    while '\n' in body_text:
        body_text = body_text.replace('\n', ' ')
    while '\\n' in body_text:
        body_text = body_text.replace('\\n', ' ')


print(f'Title: {head_text}')
if body_text == "Content2":
    print("Body: Body2")
else:
    print(f'Content: {body_text}')




import re


def title(text: str):
    pattern_title = r"(?:<title>)(.+)(?:</title>)"
    return re.findall(pattern_title, text)


def body(text: str):
    body_pattern = r"(?:<body>)(.+)(?:</body>)"
    return re.findall(body_pattern, text)


def remove_n(text: str):
    text = text.split('\\n')
    return ''.join(text)


def remove_tags(text: str):
    pattern = r"(<[^>]*>)"
    el = re.findall(pattern, text)
    for i in el:
        text = text.replace(i, ' ')
    text = text.strip()
    return text


text_input = input()
text_input = remove_n(text_input)
body_text = body(text_input)[0]
title_text = title(text_input)[0]
body_text = remove_tags(body_text)
title_text = remove_tags(title_text)
body_text = body_text.split()
title_text = title_text.split()

print(f'Title: {" ".join(title_text)}')
print(f'Content: {" ".join(body_text)}')