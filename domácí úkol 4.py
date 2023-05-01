predvolba = "+420"

def telefonni_cislo(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and cislo[:4] == predvolba:
        return True
    else:
        return False
    
def konecna_cena(cena_sms):
    cena = 3
    cena_sms = cena * (len(zprava) // 180)
    cena_sms += cena
    return cena_sms

cislo = (input("Zadejte platné telefonní číslo: "))
telefonni_cislo(cislo)

if telefonni_cislo(cislo) == False:
    print("Zadejte platné telefonní číslo ve formátu bez mezer.")
elif telefonni_cislo(cislo) == True:
    zprava = (input("Zadejte zprávu: "))
    print(f"Konečná cena za Vaši sms je {konecna_cena(zprava)} Kč.")
          
          
          
          


    


    
    
    
        





    

    





