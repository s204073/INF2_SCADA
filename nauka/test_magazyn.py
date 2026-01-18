import pytest
from magazyn import sprawdz_stan

@pytest.fixture
def baza_testowa():
    return [
        {'nazwa': 'Klawiatura', 'ilosc':15},
        {'nazwa': 'Monitor', 'ilosc':3}
    ]

def test_produkt_dostepny(baza_testowa):
    wynik = sprawdz_stan('Klawiatura', 1,baza_testowa)
    assert wynik is True

def test_brak_produktu(baza_testowa):
    wynik = sprawdz_stan('Kamera', 1,baza_testowa)
    assert wynik is True

#parametrization
@pytest.mark.parametrize("produkt,ile, oczekiwany wynik", [
    ("Monitor", 3, True),
    ("Monitor", 4, False),
    ("Drukarka", 1, False)
])

def test_wielu_przypadkow(produkt, ile, oczekiwany_wynik, baza_testowa):
    wynik = sprawdz_stan(produkt, ile, baza_testowa)
    assert wynik == oczekiwany_wynik

