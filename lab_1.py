import math  # Importujemy moduł matematyczny dla funkcji sqrt()

# Pobieramy współczynniki od użytkownika
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

# Sprawdzamy, czy to faktycznie równanie kwadratowe (a != 0)
if a == 0:
    print("To nie jest równanie kwadratowe.")
else:
    # Obliczamy deltę
    delta = b ** 2 - 4 * a * c

    # Analizujemy wartość delty
    if delta > 0:
        # Dwa różne pierwiastki rzeczywiste
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Pierwiastki równania to: {x1} i {x2}")

    elif delta == 0:
        # Jeden pierwiastek podwójny
        x = -b / (2 * a)
        print(f"Równanie ma jeden pierwiastek: {x}")

    else:
        # Brak pierwiastków rzeczywistych
        print("Równanie nie ma pierwiastków rzeczywistych.")