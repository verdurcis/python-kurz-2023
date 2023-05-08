teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Vytvoř seznam průměrných teplot pro každý den.

prumerne_teploty = [sum(zaznam) / len(zaznam) for zaznam in teploty]
print(prumerne_teploty)

# Vytvoř seznam ranních teplot.

ranni_teploty = [zaznam[0] for zaznam in teploty]
print(ranni_teploty)

# Vytvoř seznam nočních teplot.

nocni_teploty = [zaznam[3] for zaznam in teploty]
print(nocni_teploty)

# Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

for zaznam in teploty:
    poledni_nocni = [zaznam[1], zaznam[3]]
    print(poledni_nocni)

# Bonus / slovnik = {den : průměrná teplota}

teploty_bonus = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]


def convert(teploty_bonus):
    keys = [den[0] for den in teploty_bonus]
    values = [sum(zaznam[1:]) / len(zaznam[1:]) for zaznam in teploty_bonus]
    slovnik = {keys[i]: values[i] for i in range(len(teploty_bonus))}
    return slovnik

print(convert(teploty_bonus))



