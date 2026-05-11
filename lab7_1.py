def wyszukiwanie_liniowe(lista, szukana_wartosc):
    for i in range(len(lista)):
        if lista[i] == szukana_wartosc:
            return i
            
    return -1

wynik1 = wyszukiwanie_liniowe([4, 7, 2, 9, 5], 9)
wynik2 = wyszukiwanie_liniowe([10, 20, 30, 40], 25)

print(f"wyszukiwanie_liniowe([4, 7, 2, 9, 5], 9) -> Wynik: {wynik1}")
print(f"wyszukiwanie_liniowe([10, 20, 30, 40], 25) -> Wynik: {wynik2}")