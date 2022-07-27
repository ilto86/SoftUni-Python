def multiply(num_time):
    def decorator(function):
        def wrapper(num):
            result = function(num)
            return result * num_time
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10
print(add_ten(3))

print("\n")
print("=" * 20)
print("\n")

@multiply(5)
def add_ten(number):
    return number + 10
print(add_ten(6))


