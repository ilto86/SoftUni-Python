# # Keys List
# countries = input().split(", ")
# # Values list
# capitals = input().split(", ")
#
# country_capital_info = dict(zip(countries, capitals))
#
# for (country, capital) in country_capital_info.items():
#     print(f"{country} -> {capital}")


# # Keys List
# countries = input().split(", ")
# # Values list
# capitals = input().split(", ")
#
# zipped_tuples = zip(countries, capitals)
# country_capital_info = dict(zipped_tuples)
#
# for (country, capital) in country_capital_info.items():
#     print(f"{country} -> {capital}")


# # Keys List
# countries = input().split(", ")
# # Values list
# capitals = input().split(", ")
#
# zipped_tuples = zip(countries, capitals)
# country_capital_info = list(zipped_tuples)  # list of country_capital
#
# for (country, capital) in country_capital_info:
#     print(f"{country} -> {capital}")





def capitals():
    countries_data = input().split(", ")
    capitals_data = input().split(", ")
    result = dict(zip(countries_data, capitals_data))

    for (country, capital) in result.items():
        print(f"{country} -> {capital}")

capitals()