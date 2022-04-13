# word = input().lower()
#
#
# final_counter = 0
# counter = 0
# while "Sand".lower() in word:
#
#     counter += 1
#     if counter == word.count('sand'):
#         final_counter += counter
#         break
# counter = 0
# while "Water".lower() in word:
#
#     counter += 1
#     if counter == word.count('water'):
#         final_counter += counter
#         break
# counter = 0
# while "Fish".lower() in word:
#
#     counter += 1
#     if counter == word.count('fish'):
#         final_counter += counter
#         break
# counter = 0
# while "Sun".lower() in word:
#
#     counter += 1
#     if counter == word.count('sun'):
#         final_counter += counter
#         break
# print(final_counter)

# string = input().lower()
#
# count_of_sand = string.count('sand', 0, len(string))
# count_of_water = string.count('water', 0, len(string))
# count_of_fish = string.count('fish', 0, len(string))
# count_of_sun = string.count('sun', 0, len(string))
#
# count_of_words = count_of_sand+count_of_water+count_of_fish+count_of_sun
#
# print(count_of_words)

word = input()
sum_of_beach = 0

sum_of_beach += word.lower().count('sand')
sum_of_beach += word.lower().count('water')
sum_of_beach += word.lower().count('fish')
sum_of_beach += word.lower().count('sun')

print(sum_of_beach)