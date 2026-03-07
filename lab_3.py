# 1. Wczytujemy liczbę n (ilość elementów w ciągu)
n = int(input("Podaj liczbę n (n > 0): "))

# Sprawdzamy, czy n jest poprawne
if n <= 0:
    print("Błąd: n musi być większe od 0.")
else:
    # 2. Tworzymy listę i wczytujemy n liczb całkowitych
    ciag_liczb = []
    for i in range(n):
        liczba = int(input(f"Podaj liczbę {i+1}: "))
        ciag_liczb.append(liczba)

    # 3. Pobieramy liczbę do wyszukania
    szukana = int(input("Podaj liczbę do wyszukania: "))

    # 4 & 5. Sprawdzamy obecność i podajemy indeks
    if szukana in ciag_liczb:
        indeks = ciag_liczb.index(szukana) # Znajduje pierwsze wystąpienie
        print(f"Liczba {szukana} występuje w ciągu na pozycji {indeks}.")
    else:
        print(f"Liczba {szukana} nie występuje w ciągu.")