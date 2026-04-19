import heapq

kolejka = []

menu = '''\nWybierz działanie:
1. Dodaj zadanie z priorytetem
2. Obsłuż zadanie o najwyższym priorytecie
3. Pokaż kolejkę zadań
4. Zakończ działanie programu'''

while True:
    print(menu)
    wybor = input("Wybór: ")

    if wybor == '1':
        nazwa = input("Nazwa zadania: ")
        priorytet = int(input("Priorytet: "))
        heapq.heappush(kolejka, (priorytet, nazwa))
        
    elif wybor == '2':
        if kolejka:
            p, n = heapq.heappop(kolejka)
            print(f"Obsłużono: {n}")
        else:
            print("Kolejka jest pusta")
            
    elif wybor == '3':
        if kolejka:
            for p, n in sorted(kolejka):
                print(f"Priorytet {p} - {n}")
        else:
            print("Kolejka jest pusta")
            
    elif wybor == '4':
        break