number = int(input())

prime_number = True

if number == 1 or (number != 2 and number % 2 == 0) or (number != 3 and number % 3 == 0) or \
        (number != 5 and number % 5 == 0) or (number != 7 and number % 7 == 0):
    prime_number = False
    print(prime_number)

else:
    print(prime_number)

