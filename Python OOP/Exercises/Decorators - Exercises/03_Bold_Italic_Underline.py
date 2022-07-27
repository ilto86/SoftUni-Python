# First Solution

# def make_bold(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         return f"<b>{result}</b>"
#     return wrapper
#
#
# def make_italic(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         return f"<i>{result}</i>"
#     return wrapper
#
#
# def make_underline(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         return f"<u>{result}</u>"
#     return wrapper
#
#
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))
#
#
# @make_bold
# @make_italic
# @make_underline
# def greet_all(*args):
#     return f"Hello, {', '.join(args)}"
#
#
# print(greet_all("Peter", "George"))





# Second Solution

def format_text(tag, text):
    return f"<{tag}>{text}</{tag}>"


def make_bold(func_ref):
    def wrapper(*args):
        func_res = func_ref(*args)
        return format_text("b", func_res)
    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        func_res = func_ref(*args)
        return format_text("i", func_res)
    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        func_res = func_ref(*args)
        return format_text("u", func_res)
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet("Peter"))

print(greet_all("Peter", "George"))