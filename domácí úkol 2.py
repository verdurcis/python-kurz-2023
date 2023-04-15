sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadejte kód: ")
mnozstvi = int(input("Zadejte množství: "))

if kod in sklad:
    if mnozstvi > sklad[kod]:
        print(f"Omlouváme se, ale můžeme prodat pouze omezené množství kusů. Rezervujeme Vám všech {sklad[kod]} ks, které máme skladem.")
        sklad.pop(kod)
        print(f"Skladem zbývají tyto položky: {sklad}")
    elif mnozstvi <= sklad[kod]:
        print("Počet kusů dané položky je skladem.")
        sklad[kod] = sklad[kod] - mnozstvi
        print(f"Skladem zbývá {sklad[kod]} ks.")
elif kod not in sklad:    
    print("Omlouváme se, ale součástka není skladem.")

