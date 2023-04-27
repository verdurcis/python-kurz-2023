import json

with open("body.json", encoding='utf-8') as soubor:
     prospech = json.load(soubor)

with open("bonusy.json", encoding='utf-8') as soubor2:
     body_navic = json.load(soubor2)

for key,val in prospech.items():
    for jmeno,body in body_navic.items():
        if jmeno not in key:
            pass
        else:
            jednicka = 1
            dvojka = 2
            trojka = 3
            ctyrka = 4
            petka = 5

            if prospech[key] + body_navic[jmeno] >= 90:
                body_navic[jmeno] = jednicka
            elif prospech[key] + body_navic[jmeno] > 70 and prospech[key] + body_navic[jmeno] < 89:
                body_navic[jmeno] = dvojka
            elif prospech[key] + body_navic[jmeno] > 50 and prospech[key] + body_navic[jmeno] < 69:
                body_navic[jmeno] = trojka
            elif prospech[key] + body_navic[jmeno] > 30 and prospech[key] + body_navic[jmeno] < 49:
                body_navic[jmeno] = ctyrka
            else:
                body_navic[jmeno] = petka

            with open("znamky.json", mode="w", encoding='utf-8') as i:
                json.dump(body_navic, i, ensure_ascii=False)

