def pobierz_n_elementow(kolejka, n):
    if len(kolejka) == 0:
        return "Kolejka jest pusta"
    
    wynik = []
    ilosc = min(n, len(kolejka))
    
    for _ in range(ilosc):
        wynik.append(kolejka.pop(0))
        
    return wynik


