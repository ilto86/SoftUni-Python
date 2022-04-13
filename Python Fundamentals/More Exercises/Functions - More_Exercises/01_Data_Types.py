def data_type(text, nums):
    result = 0
    string = []
    if text_as_string == "int":
        result = int(num_as_string) * 2
        print(result)
    elif text_as_string == "real":
        result = float(num_as_string) * 1.5
        print(f"{result:.2f}")
    else:
        string.append(num_as_string)
        string.insert(0, "$")
        string.insert(len(string), "$")
        print("".join(string))

text_as_string = input()
num_as_string = input()
data_type(text_as_string, num_as_string)



def data_types(type, data):
    if type == "int":
        data = int(data) * 2
    elif type == "real":
        data = f"{float(data) * 1.5:.2f}"
    elif type == "string":
        data = f"${data}$"
    print(data)

data_type = input()
data_value = input()
data_types(data_type, data_value)