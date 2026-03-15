def czy_palindrom(napis):
    if len(napis) <= 1:
        return True

    if napis[0] != napis[-1]:
        return False

    return czy_palindrom(napis[1:-1])


print(f"kajak: {czy_palindrom('kajak')}")
print(f"radar: {czy_palindrom('radar')}")
print(f"python: {czy_palindrom('python')}")
print(f"anna: {czy_palindrom('anna')}")