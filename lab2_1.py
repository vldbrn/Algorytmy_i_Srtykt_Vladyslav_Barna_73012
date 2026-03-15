def druga_najwieksza(lista):
    najwieksza = float()
    druga = float()

    for liczba in lista:
        if liczba > najwieksza:
            druga = najwieksza
            najwieksza = liczba
        elif liczba > druga and liczba != najwieksza:
            druga = liczba

    return druga


print(druga_najwieksza([10, 20, 4, 45, 99, 99]))
print(druga_najwieksza([1, 2, 3, 4, 5]))
print(druga_najwieksza([10, 10, 10, 9]))