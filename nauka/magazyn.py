
def sprawdz_stan (produkt, ilosc, baza_magazynowa):
    for pozycja in baza_magazynowa:    #iterowanie po kazdym
        if pozycja['nazwa'] == produkt:
            if pozycja['ilosc'] >= ilosc:
                return True
            else:
                return False
    return False

s