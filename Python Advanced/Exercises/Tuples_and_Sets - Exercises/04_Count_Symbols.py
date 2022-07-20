text = input()
symbols = {}

for ch in text:
    # if ch not in symbols:
    #     symbols[ch] = 0
    # symbols[ch] += 1
    if ch in symbols:
        symbols[ch] += 1
    else:
        symbols[ch] = 1

for key, value in sorted(symbols.items()):
    print(f"{key}: {value} time/s")






# text = input()
# unique_text = set(text)
# result = {}
#
#
# for ch in text:
#     count = 1
#     if ch in unique_text:
#         result[ch] = count
#         unique_text.remove(ch)
#     elif ch not in unique_text:
#         result[ch] += 1
#
# sorted_result = sorted(result.items())
# for key,value in sorted_result:
#     print(f"{key}: {value} time/s")
