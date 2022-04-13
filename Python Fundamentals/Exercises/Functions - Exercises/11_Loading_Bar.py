# def loading_bar(num):
#     loading_status = f''
#     if num == 100:
#         print('100% Complete!')
#         print('[%%%%%%%%%%]')
#     else:
#         percent = (num//10) * '%'
#         dots = (10 - (num // 10)) * '.'
#
#         print(f'{num}% [{percent}{dots}]')
#         print('Still loading...')
#
# number = int(input())
# loading_bar(number)

def progress(loading_bar):
    if loading_bar == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{loading_bar}% [{'%' * (loading_bar // 10)}{'.' * (10 - loading_bar // 10)}]\nStill loading..."

loading_bar_value = int(input())
print(progress(loading_bar_value))