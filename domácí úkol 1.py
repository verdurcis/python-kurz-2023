jmeno = "Veronika"
domena = "czechitas.cz"

print(jmeno + "@" + domena)
print(f"Email uživatele je: {jmeno}@{domena}.")

#bonus

#1
jmeno_prijmeni = input("Jak se jmenuješ? ")

print(jmeno_prijmeni.upper())

#2
print(jmeno_prijmeni.lower())

#3

list = jmeno_prijmeni.split(" ")

jmeno = list[0].capitalize()
prijmeni = list[1].capitalize()

print(jmeno + " " + prijmeni)

#4 - 1. varianta

jmeno = list[0][0].upper()
prijmeni = list[1][0].upper()

print(jmeno + "." + prijmeni + ".")


#4 -.2. varianta
def inicialy(jmeno_prijmeni):
    inicial = ""
    if (len(jmeno_prijmeni) == 0):
        return
    
    prvni_druhe = jmeno_prijmeni.split(" ")
    for jmeno in prvni_druhe:
        inicial = inicial + jmeno[0].upper() + "."
    return inicial

jmeno_prijmeni = input("Jak se jmenuješ? ")
print(f"Iniciály tohoto jména jsou: {inicialy(jmeno_prijmeni)}")

#5

jmeno_a_prijmeni = input("Jak se jmenuješ? ")
zkraceno = jmeno_a_prijmeni.split(" ")

for jmeno in zkraceno:
    if len(zkraceno[0]) <= 5:
        print(jmeno_a_prijmeni)
        break
    else:
        print(zkraceno[0][0] + "." + zkraceno[1])
        
# Jak printnout jen 1x ? 


