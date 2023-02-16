import random 


kleur = ("oranje", "blauw", "groen", "bruin") #hier zet hij alle kleuren in de tuple
zak = int(input("Hoeveel m&m's wilt u in de zak")) #hier vraagt hij hoeveel M&M's je wilt
lijst = [] #dit is een lege lijst waar ze straks allemaaal ingaan

for i in range(zak): #hier verwerkt hij hoeveel M&Ms jij wilt
    hoeveel = random.randint(0,4) #hier kiest hij vier random kleuren uit de tuple
    print(kleur[hoeveel]) #hier print hij welke kleuren je hebt
    lijst.append(kleur[hoeveel]) #hier append hij hoeveel M&M"s je hebt aan gegeven
print(lijst) #hier print hij zak waar de M&M's in zitten en welke kleuren