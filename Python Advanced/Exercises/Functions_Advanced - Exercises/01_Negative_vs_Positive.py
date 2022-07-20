def find_positive_and_negative_sums(*args):
    positive_sum = 0
    negative_sum = 0

    for el in args:
        if el > 0:
            positive_sum += el
        else:
            negative_sum += el

    return positive_sum, negative_sum



nums = [int(x) for x in input().split()]

positive_result, negative_result = find_positive_and_negative_sums(*nums)

print(negative_result)
print(positive_result)

if abs(negative_result) > positive_result:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")