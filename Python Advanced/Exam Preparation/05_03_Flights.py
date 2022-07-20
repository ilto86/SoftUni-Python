def flights(*args):
    flight_list = [*args]
    flight_dict = {}
    while True:
        if flight_list[0] == "Finish":
            break
        else:
            if flight_list[0] in flight_dict:
                flight_dict[flight_list[0]] += flight_list[1]
                flight_list.pop(0)
                flight_list.pop(0)
            else:
                flight_dict[flight_list[0]] = flight_list[1]
                flight_list.pop(0)
                flight_list.pop(0)

    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26,
'Morocco', 98, 'Paris', 115, 'Finish',
'Paris', 15))                               # {'Vienna': 282, 'Morocco': 98, 'Paris': 115}

print(flights('London', 0, 'New York', 9,
'Aberdeen', 215, 'Sydney', 2, 'New York',
300, 'Nice', 0, 'Finish'))                  # {'London': 0, 'New York': 309, 'Aberdeen': 215, 'Sydney': 2, 'Nice': 0}

print(flights('Finish', 'New York', 90,
'Aberdeen', 300, 'Sydney', 0))              # {}