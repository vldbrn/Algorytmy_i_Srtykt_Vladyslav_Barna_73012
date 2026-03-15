def wynik_tabel():
    print(f"{'i':<5}  {'wynik(i)':<10}  {'Ilość wywołań':<15}")

    def wynik(i):
        nonlocal count
        if i < 5:
            return 2
        elif i % 2 == 0:
            count += 2
            return wynik(i - 4) + wynik(i - 2) + 2
        else:
            count += 1
            return wynik(i - 2) % 9

    for i in range(1, 16):
        count = 0 
        wartosc = wynik(i)
        print(f"{i:<5}  {wartosc:<10}  {count:<15}")

wynik_tabel()