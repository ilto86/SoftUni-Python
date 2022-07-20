import re

planets = int(input())

planets_attacked = []
planets_destroyed = []

for planet in range(planets):
    raw_message = input()
    decryption_key = [key for key in raw_message.lower() if key == 's' or key == 't' or key == 'a' or key == 'r']
    decryption_key = len(decryption_key)
    new_message = ''
    raw_message = [r for r in raw_message]

    for raw in raw_message:
        value = ord(raw) - decryption_key
        new_message += chr(value)

    pattern = r'@(?P<planet_name>[A-Za-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)![^\@\-\!\:\>]*(?P<attack_type>[A|D])![^\@\-\!\:\>]*(?P<soldier_count>)->\d+'

    matches = re.finditer(pattern, new_message)

    for match in matches:
        if match.group('attack_type') == 'A':
            planets_attacked.append(match.group('planet_name'))
        elif match.group('attack_type') == 'D':
            planets_destroyed.append(match.group('planet_name'))

print(f"Attacked planets: {len(planets_attacked)}")
for planet in sorted(planets_attacked):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(planets_destroyed)}")
for des in sorted(planets_destroyed):
    print(f"-> {des}")










import re

key_pattern = r"([star])"
info_pattern = r"((?<=@)[A-Za-z]+)[^@!>\-]*((?<=:)\d+)[^@:>\-]*((?<=!)[AD](?=!))[^@:]*((?<=->)\d+)"
#
# name_pattern = r"(?<=@)([A-Za-z]+)"
# population_pattern = r"(?<=:)(\d+)"
# attack_type_pattern = r"(?<=!)([AD])(?=!)"
# soldier_count_pattern = r"(?<=->)\d+"
# sep = r"[^@!>:-]*"

attacked_planets = []
destroyed_planets = []

n = int(input())
for _ in range(n):
    encrypted = input()
    decrypted = ""
    key_matches = re.findall(key_pattern, encrypted, re.IGNORECASE)
    key = len(key_matches)
    for char in encrypted:
        decrypted += chr(ord(char) - key)

    match = re.findall(info_pattern, decrypted)
    if match:
        name = match[0][0]
        population = match[0][1]
        attack_type = match[0][2]
        soldier_count = match[0][3]
        if attack_type == "A":
            attacked_planets.insert(0, name)
        elif attack_type == "D":
            destroyed_planets.insert(0, name)

print(f"Attacked planets: {len(attacked_planets)}")
for name in attacked_planets:
    print(f"-> {name}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for name in destroyed_planets:
    print(f"-> {name}")







import re
from collections import defaultdict


planets = defaultdict(list)


def decrypt_message(message: str) -> str:
    """Decrypt message
    Args:
        message (str): Message to be decrypted
    Returns:
        message (str): Decrypted message
    """
    let_pattern = r'(?i)[s,t,a,r]'
    letters = re.findall(let_pattern, message)
    factor = len(letters)
    for i, c in enumerate(message):
        message = message[:i]+chr(ord(c)-factor)+message[i+1:]
    return message


def get_message_info(message: str, planets: dict) -> dict:
    """Add planets to the dictionary
    Args:
        message (str): Decrypted message
        planets (dict): Planets dict
    Returns:
        planets (dict): Updated Planets dict
    """
    # ! NOT WORKING pattern = r'(?:(?<=\@)(?P<name>[A-Za-z]+)[^@!:>-]*(?<=\:)(?P<population>\d+)[^@!:>-]*(?<=\!)(?P<attack>[AD])(?=\!)[^@!:>-]*(?<=\-\>)(?P<soldiers>[\d]+))'
    pattern = r'(?:@(?P<name>[A-Za-z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*!(?P<attack>A|D)![^@!:>-]*->(?P<soldiers>[\d]+))'
    m = re.search(pattern, message)

    if m:
        if m.group('attack') == 'A':
            planets['Attacked'].append(m.group('name'))
        if m.group('attack') == 'D':
            planets['Destroyed'].append(m.group('name'))
    return planets


n = int(input())

for _ in range(n):
    message = input()
    decrypted = decrypt_message(message)
    planets = get_message_info(decrypted, planets)

print(f'Attacked planets: {len(planets["Attacked"])}')
if planets['Attacked']:
    for attacked in sorted(planets['Attacked']):
        print(f'-> {attacked}')
print(f'Destroyed planets: {(len(planets["Destroyed"]))}')
if planets['Destroyed']:
    for destroyed in sorted(planets['Destroyed']):
        print(f'-> {destroyed}')





import re


def key(message: str):
    reg = r"[starSTAR]"
    return len(re.findall(reg, message))


def transform(message: str, value: int):
    return ''.join([chr(ord(x) - value) for x in message])


def register(message: str, log: dict):
    pattern = r"([^@\-\!\,\:\>]+)?@(?P<planet_name>[a-zA-Z]+)([^@\-\!\,\:\>]+)?:(?P<planet_population>\d+)([^@\-\!\,\:\>]+)?\!(?P<attack>[AD])\!([^@\-\!\,\:\>]+)?\-\>(?P<soldiers>\d+)"
    match = re.match(pattern, message)
    if match:
        el = match.groupdict()
        if el['attack'] == 'A':
            log['attacked_planets'].append(el['planet_name'])
        elif el['attack'] == 'D':
            log['destroyed_planets'].append(el['planet_name'])


text = []
for _ in range(int(input())):
    text.append(input())
status = {'attacked_planets': [], 'destroyed_planets': []}
for i in text:
    decr_message = transform(i, key(i))
    register(decr_message, status)

print(f'Attacked planets: {len(status["attacked_planets"])}')
[print(f'-> {x}') for x in sorted(status["attacked_planets"])]
print(f'Destroyed planets: {len(status["destroyed_planets"])}')
[print(f'-> {x}') for x in sorted(status["destroyed_planets"])]