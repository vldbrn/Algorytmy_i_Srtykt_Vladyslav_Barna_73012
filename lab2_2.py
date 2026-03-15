def znajdz_min_max(macierz):
    najm_v = macierz[0][0]
    najm_r, najm_c = 0, 0

    najb_v = macierz[0][0]
    najb_r, najb_c = 0, 0

    for r in range(len(macierz)):
        for c in range(len(macierz[r])):
            if macierz[r][c] < najm_v:
                najm_v = macierz[r][c]
                najm_r, najm_c = r, c

            if macierz[r][c] > najb_v:
                najb_v = macierz[r][c]
                najb_r, najb_c = r, c


    print("Macierz:")
    for r in range(len(macierz)):
        for c in range(len(macierz[r])):
            if r == najm_r and c == najm_c:
                print("MIN", end="\t")
            elif r == najb_r and c == najb_c:
                print("MAX", end="\t")
            else:
                print(macierz[r][c], end="\t")
        print()

macierz = [
    [5, 2, 9, 8],
    [1, 7, 3, 4],
    [6, 0, 2, 5]
]

znajdz_min_max(macierz)