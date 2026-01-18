from magazyn import sprawdz_stan

magazyn = [
    {'nazwa': 'Laptop', 'ilosc': 10},
    {'nazwa': 'Myszka', 'ilosc': 5},
]

print("Test 1: Dostepny produkt...")
assert sprawdz_stan('Laptop', 5,magazyn) == True

print("Test 2: Za mala ilosc...")
assert sprawdz_stan('Myszka', 10,magazyn) == False

print("wszystkie testy manualne zaliczone!")