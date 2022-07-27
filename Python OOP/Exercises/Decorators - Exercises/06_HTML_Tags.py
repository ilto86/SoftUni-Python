# First Solution

# def format_text(tag, text):
#     return f"<{tag}>{text}</{tag}>"
#
#
# def tags(param):
#     def decorator(func_ref):
#         def wrapper(*args):
#             func_res = func_ref(*args)
#             return format_text(param, func_res)
#         return wrapper
#     return decorator
#
#
#
# @tags('p')
# def join_strings(*args):
#     return "".join(args)
#
#
# print(join_strings("Hello", " you!"))
#
#
# @tags('h1')
# def to_upper(text):
#     return text.upper()
#
#
# print(to_upper('hello'))




# Second Solution

def tags(tag):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))