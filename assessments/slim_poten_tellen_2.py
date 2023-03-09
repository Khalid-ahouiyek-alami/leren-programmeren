POTEN_GIRAF= 4
POTEN_STRUISVOGEL=2
POTEN_ZEBRA=4

aantal_zebra=int(input("aantal zebra's??? "))
aantal_giraf=int(input("aantal giraffen???"))
aantal_struisvogel=int(input("aantal struisvogels???"))

def berekenen_poten(giraffen, zebra, struisvogels):

    aantal_poten= zebra*POTEN_ZEBRA+giraffen*POTEN_GIRAF+struisvogels*POTEN_STRUISVOGEL

    return(aantal_poten)


print(berekenen_poten(aantal_zebra,aantal_giraf,aantal_struisvogel))
