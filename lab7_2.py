def wyszukiwanie_interpolacyjne(lista, szukana):
    start = 0
    end = len(lista) - 1

    while start <= end and szukana >= lista[start] and szukana <= lista[end]:
        if start == end:
            if lista[start] == szukana:
                return start
            return -1

        mid = start + ((szukana - lista[start]) * (end - start)) // (lista[end] - lista[start])

        if lista[mid] == szukana:
            return mid
        elif lista[mid] < szukana:
            start = mid + 1
        else:
            end = mid - 1

    return -1

# Część 1 i 2: Obliczenia i tabela kroków

# Krok 1:
# start = 0, end = 8
# mid = 0 + ((36 - 12) * (8 - 0)) / (60 - 12)
# mid = 0 + (24 * 8) / 48
# mid = 0 + 192 / 48
# mid = 4

# Wartość lista[4] to 36.
# lista[mid] jest RÓWNA szukanej (36 == 36). Wartość znaleziona, koniec algorytmu.

# Krok   start    end    mid    lista[mid]

#   1      0       8      4        36        

# Część 3: Podsumowanie

# - Czy szukana wartość została znaleziona: Tak
# - Na której pozycji się znajduje: Na pozycji o indeksie 4
# - Ile kroków było potrzebnych: 1 krok
# - Rozłożenie danych i wpływ na szybkość: Dane są idealnie równomiernie rozłożone (wzrastają o stałą wartość 6)
# Dzięki temu wzór interpolacyjny dokładnie przewidział pozycję szukanej wartości od razu, 
# co zapewniło maksymalną możliwą szybkość działania algorytmu
