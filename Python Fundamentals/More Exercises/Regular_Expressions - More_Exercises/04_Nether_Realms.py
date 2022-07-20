import re


def find_health(text: str):
    reg = r"[^0-9\+\-\*\/\.]"
    return sum([ord(x) for x in re.findall(reg, text)])


def find_damage(text: str):
    reg_2 = r"(?:\+|-)?[0-9]+(?:\.[0-9]+)?"
    reg_3 = r"[\*\/]"
    numbers = [float(x) for x in re.findall(reg_2, text)]
    damage = sum(numbers)
    manipulators = re.findall(reg_3, text)
    for i in manipulators:
        if i == '*':
            damage *= 2
        else:
            damage /= 2

    return damage


demons_list = input().split(',')
demons_list = [x.strip() for x in demons_list]
for demon in sorted(demons_list):
    print(f'{demon} - {find_health(demon)} health, {find_damage(demon):.2f} damage')







import re


demons = [i.strip() for i in input().split(',')]
pattern = r'(?P<h_chars>[^0-9\+\-\*\./]+)?(?P<d_chars>[+-]?\d+(\.[\d]+)*)?(?P<m_chars>[\*/]*)?'
demons_stats = {}
for demon in demons:
    demons_stats[demon] = {}
    demon_health = 0
    demon_damage = 0
    mods = ''
    for m in re.finditer(pattern, demon):
        h_chars = m.group('h_chars')
        d_chars = m.group('d_chars')
        m_chars = m.group('m_chars')
        if h_chars:
            for char in h_chars:
                demon_health += ord(char)
        if d_chars:
            demon_damage += float(d_chars)
        if m_chars:
            mods += m_chars
    demons_stats[demon] = {'health': demon_health,
                           'damage': demon_damage, 'mods': mods}

for demon, stats in sorted(demons_stats.items()):
    if 'mods' in stats:
        for char in stats['mods']:
            if char == '*':
                stats['damage'] *= 2
            elif char == '/':
                stats['damage'] /= 2
    print(f'{demon} - {stats["health"]} health, {stats["damage"]:.2f} damage')







import re
import itertools

initial_text = input()
res2 = re.findall(r'[^,\s]+', initial_text)
# res = [c.strip() for c in initial_text.split(',') if not c.isspace()]
demon_health = 0
demons_dict = {}
demon_name = ''
digits = []
for i in range(len(res2)):
    for s in res2[i]:
        if not s.isdigit() and s != "+" and s != "-" and s != "*" and s != "/" and s != ".":
            demon_health += ord(s)
        demon_name += s

    demons_dict[demon_name] = [demon_health]
    demon_health = 0
    demon_name = ''

demons_damage_lst = []

for ind in range(len(res2)):
    demon_damage = 0

    digits_pattern = r'([-|+]?[0-9]+\.[0-9]+)|([-|+]?[0-9]+)'
    digits_match = re.compile(digits_pattern)
    for k, v in re.findall(digits_match, str(res2[ind])):
        if v == '':
            demon_damage += float(k)
        elif k == '':
            demon_damage += float(v)
    symbols_pattern = r'([\*])|([\/])'
    symbols_match = re.compile(symbols_pattern)
    for st, xe in re.findall(symbols_match, str(res2[ind])):
        if xe == "/":
            demon_damage = demon_damage / 2
        elif st == "*":
            demon_damage *= 2
    demons_damage_lst.append(demon_damage)

for fr, va in itertools.zip_longest(demons_dict, demons_damage_lst):
    demons_dict[fr] += [va]

sorted_demons_dict = dict(sorted(demons_dict.items(),key=lambda x: x[0]))

for f_key, f_val in sorted_demons_dict.items():
    print(f"{f_key} - ", end='')
    print(f"{f_val[0]} health", end=", ")
    print(f"{f_val[1]:.2f} damage")