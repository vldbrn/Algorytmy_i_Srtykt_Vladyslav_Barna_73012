# Wczytujemy liczbę n (ilość elementów w ciągu)
n = int(input("Podaj liczbę n (n > 0): "))

# Sprawdzamy, czy n jest poprawne
if n <= 0:
    print("Błąd: n musi być większe od 0.")
else:
    licznik_parzystych = 0  # Licznik liczb parzystych

    # Pętla do wczytywania n liczb
    for i in range(n):
        liczba = int(input(f"Podaj liczbę {i + 1}: "))

        # Sprawdzamy, czy liczba jest parzysta
        if liczba % 2 == 0:
            licznik_parzystych += 1

    # Wypisujemy wynik
    print(f"Liczba parzystych liczb w ciągu: {licznik_parzystych}")