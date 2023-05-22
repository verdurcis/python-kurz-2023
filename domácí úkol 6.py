
class Auto():
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True  

    def get_info(self):
        return f"Auto má registrační značku {self.registracni_znacka}, jmenuje se {self.typ_vozidla} a má najeto {self.najete_km} km."
    
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f"Potvrzujeme zapůjčení vozidla."
        return f"Omlouváme se, ale toto vozidlo není dostupné."
    
    def vrat_auto(self, stav_tachometru, pocet_dni):

        self.pocet_dni = pocet_dni
        self.stav_tachometru = stav_tachometru
        self.dostupne = True

        if pocet_dni < 7:
            cena_den = 400
        else:
            cena_den = 300

        konecna_cena = cena_den * pocet_dni
        return(f"Cena zapůjčení auta je {konecna_cena} Kč.")

    
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
skoda = Auto("1P3 4747", "Škoda Octavia", "41253")


def zapujceni_auta():
    zapujceni_auta = input("Auto jaké značky si přejete zapůjčit? ")
    if zapujceni_auta == "Peugeot":
        print(peugeot.get_info())
        print(peugeot.pujc_auto())
    elif zapujceni_auta == "Škoda":
        print(skoda.get_info())
        print(skoda.pujc_auto())
    else:
        print("Omlouváme se, ale toto auto v nabídce nemáme.")

zapujceni_auta()

uzivatel = input("Jaké auto vracíte? ")
stav_tachometru = input("Jaký máte stav na tachometru? ") 
pocet_dni = int(input("Kolik dní jste měli auto půjčené? "))

if uzivatel == "Peugeot":
    print(peugeot.vrat_auto(stav_tachometru, pocet_dni))
    print("Peugot byl vrácen.")
if uzivatel == "Škoda":
    print(skoda.vrat_auto(stav_tachometru, pocet_dni))
    print("Škoda byla vrácena.")

zapujceni_auta()