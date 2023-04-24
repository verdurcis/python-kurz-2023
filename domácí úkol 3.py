import json

with open("body.json", encoding='utf-8') as soubor:
     prospech = json.load(soubor)
print(prospech)

prospel = "Pass"
neprospel = "Fail"

for key,val in prospech.items():
    if val >= 60:
        prospech[key] = prospel
    else:
        prospech[key] = neprospel
    print(prospech)

    with open("prospech_json.json", mode="w", encoding='utf-8') as i:
        json.dump(prospech, i, ensure_ascii=False)


