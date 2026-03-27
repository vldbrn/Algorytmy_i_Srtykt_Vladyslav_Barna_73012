def szukaj_rek(tab, x, l, p):
    if l > p:
        return -1

    srodek = (l + p) // 2

    if tab[srodek] == x:
        return srodek
    elif tab[srodek] > x:
        return szukaj_rek(tab, x, l, srodek - 1)
    else:
        return szukaj_rek(tab, x, srodek + 1, p)


tablica = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
wynik = szukaj_rek(tablica, 55, 0, len(tablica) - 1)
print(wynik)