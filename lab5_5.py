kolejka = []

menu = '''\nWybierz działanie:
1. Dodaj klienta do kolejki
2. Obsłuż klienta
3. Pokaż kolejkę i czas oczekiwania
4. Zakończ'''

while True:
    print(menu)
    wybor = input("Wybór: ")

    if wybor == '1':
        imie = input("Imię klienta: ")
        czas = int(input("Czas obsługi (w minutach): "))
        kolejka.append((imie, czas))
        
    elif wybor == '2':
        if kolejka:
            imie, czas = kolejka.pop(0)
            print(f"Obsłużono: {imie}. Obsługa trwała {czas} min.")
        else:
            print("Kolejka jest pusta")
            
    elif wybor == '3':
        if kolejka:
            czas_czekania = 0
            for imie, czas in kolejka:
                print(f"Klient: {imie} | Czas obsługi: {czas} min | Musi czekać: {czas_czekania} min")
                czas_czekania += czas
        else:
            print("Kolejka jest pusta")
            
    elif wybor == '4':
        break