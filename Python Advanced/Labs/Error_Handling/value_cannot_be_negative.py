# class ValueCannotBeNegative(Exception):
#  """Number is below zero"""
#  pass
#
# for i in range(5):
#  number = int(input())
#  if number < 0:
#   raise ValueCannotBeNegative

# 1
# 4
# -5
# 3
# 10

class ValueCannotBeNegative(Exception):
 pass

values = [int(input()) for _ in range(5)]

for value in values:
 if value < 0:
  raise ValueCannotBeNegative