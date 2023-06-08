def functie(lijst: list, aantal: int):
    print(lijst)
    for x in range(aantal -2):
        lijst.append(lijst[-1] + lijst[-2])
        print(lijst)


    gulden_snede= lijst[-1] / lijst[-2]
    return gulden_snede
gulde = functie([0, 1], 10)
print(gulde)




