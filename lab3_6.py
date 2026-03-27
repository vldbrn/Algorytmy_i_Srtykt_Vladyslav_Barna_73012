def plecak_rek(n, C, wartosci, wagi, memo=None):
    if memo is None:
        memo = {}

    if n == 0 or C == 0:
        return 0

    if (n, C) in memo:
        return memo[(n, C)]

    if wagi[n - 1] > C:
        wynik = plecak_rek(n - 1, C, wartosci, wagi, memo)
    else:
        bez_przedmiotu = plecak_rek(n - 1, C, wartosci, wagi, memo)
        z_przedmiotem = wartosci[n - 1] + plecak_rek(n - 1, C - wagi[n - 1], wartosci, wagi, memo)
        wynik = max(bez_przedmiotu, z_przedmiotem)

    memo[(n, C)] = wynik
    return wynik


n = 4
C = 7
wartosci = [1, 4, 5, 7]
wagi = [1, 3, 4, 5]

wynik = plecak_rek(n, C, wartosci, wagi)
print(wynik)