# def gen_html(article: dict) -> str:
#     """Generate HTML tags for the dict object, supplied
#     Args:
#         article (dict): Article dic, 'title: str', content: str', 'comments: list'
#     Returns:
#         str: HTML code
#     """
#     article_html = ''
#     nl = '\n'
#     head_html = f"<h1>{nl}    {article['title']}{nl}</h1>{nl}"
#     content_html = f"<article>{nl}    {article['content']}{nl}</article>{nl}"
#     article_html += head_html + content_html
#     for comment in article['comments']:
#         comment_html = f"<div>{nl}    {comment}{nl}</div>{nl}"
#         article_html += comment_html
#     return article_html
#
#
# article = {}
# article_title = input()
# article_content = input()
# article['title'] = article_title
# article['content'] = article_content
# article['comments'] = []
#
# while True:
#     data = input()
#     if data == 'end of comments':
#         break
#     article['comments'].append(data)
#
# print(gen_html(article))





# def print_title(text):
# 	print("<h1>")
# 	print(f"    {text}")
# 	print("</h1>")
#
#
# def print_content(text):
# 	print("<article>")
# 	print(f"    {text}")
# 	print("</article>")
#
#
# def print_comment(text):
# 	print("<div>")
# 	print(f"    {text}")
# 	print("</div>")
#
#
# title, content, comment = input(), input(), input()
# print_title(title)
# print_content(content)
# while not comment == "end of comments":
# 	print_comment(comment)
# 	comment = input()






# def read_input():
#     result = []
#     while True:
#         comment = input()
#         if comment == "end of comments":
#             break
#         result.append(comment)
#     return result
#
# def print_html(title, content, comments):
#     result = f"<h1>\n    {title}\n</h1>\n" + f"<article>\n    {content}\n</article>\n" +\
#             "\n".join(f'<div>\n    {comment}\n</div>' for comment in comments)
#     print(result)
#
#
# title = input()
# content = input()
# comments = read_input()
# print_html(title, content, comments)






# title_of_an_article = input()
# print(f"<h1>")
# print(title_of_an_article)
# print(f"</h1>")
# content_of_the_article = input()
# print(f"<article>")
# print(content_of_the_article)
# print(f"</article>")
#
# while True:
#
#     comment = input()
#
#     if comment == "end of comments":
#         break
#     print(f"<div>")
#     print(comment)
#     print(f"</div>")




print(f"""<h1>
    {input()}
</h1>""")

print(f"""<article>
    {input()}
</article>""")

text = input()

while not text == "end of comments":
    print(f"""<div>
    {text}
</div>""")

    text = input()