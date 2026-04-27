def selection_sort(wagi):
    n = len(wagi)
    liczba_porownan = 0

    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            liczba_porownan += 1  # Rejestrujemy każde porównanie
            if wagi[j] < wagi[min_idx]:
                min_idx = j
                
        wagi[i], wagi[min_idx] = wagi[min_idx], wagi[i]
        
        print(f"Iteracja {i + 1}: {wagi}")

    print(f"\nŁączna liczba porównań: {liczba_porownan}")
    return wagi

wagi_paczek = [18, 5, 12, 3, 9]

print(f"Stan początkowy: {wagi_paczek}\n")
selection_sort(wagi_paczek)