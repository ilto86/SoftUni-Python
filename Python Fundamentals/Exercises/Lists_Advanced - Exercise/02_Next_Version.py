def next_version(version_number):
    version_number = int("".join(version_number)) + 1
    result = [str(num) for num in str(version_number)]
    print(".".join(result))

data = input().split(".")
next_version(data)


# def next_version():
#     data = input().split(".")
#     version_number = int("".join(data)) + 1
#     result = [str(num) for num in str(version_number)]
#     print(".".join(result))
#
# next_version()