class Kolejka:
    def __init__(self):
        self.elementy = []

    def is_empty(self):
        return len(self.elementy) == 0

    def enqueue(self, pacjent):
        self.elementy.append(pacjent)
        print(f"Zarejestrowano pacjenta {pacjent}")

    def dequeue(self):
        if self.is_empty():
            print("Kolejka jest pusta")
            return None
        else:
            wywolany = self.elementy.pop(0)
            print(f"Wywołano pacjenta do gabinetu {wywolany}")
            return wywolany

    def show_queue(self):
        if self.is_empty():
            print("Kolejka jest pusta")
        else:
            print(f"Aktualna kolejka {self.elementy}")

def main():
    kolejka = Kolejka()
    
    menu = '''\nWybierz działanie:
1. Zarejestruj pacjenta
2. Wywołaj pacjenta do gabinetu
3. Pokaż aktualną kolejkę
4. Zakończ działanie programu'''

    while True:
        print(menu)
        wybor = input("Podaj numer opcji")

        if wybor == '1':
            imie = input("Podaj imię i nazwisko pacjenta")
            kolejka.enqueue(imie)
        elif wybor == '2':
            kolejka.dequeue()
        elif wybor == '3':
            kolejka.show_queue()
        elif wybor == '4':
            print("Zakończono działanie programu")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie")

if __name__ == "__main__":
    main()