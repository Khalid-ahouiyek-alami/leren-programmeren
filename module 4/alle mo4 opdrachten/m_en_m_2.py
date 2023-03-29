import random
kleurLijst = ["rood", "blauw", "groen", "geel", "bruin"]

hoeveel = int(input("Hoeveel M&M's moeten er gevoegd worden: "))
bagofmnms = {}
getal = 1

for x in range(hoeveel):
    kleur = random.choice(kleurLijst)  #hier kiest hij random kleuren uit de list hier boven 
    if kleur not in bagofmnms:
        bagofmnms.update({kleur : getal}) #bij zin 10/11 als de kleur niet voor komt in de random gekozen kleuren dan word de het uit de dict gehaald

    elif kleur in bagofmnms:    #hier bij zin 13/14 word de kleur gevoegd met de hoeveelheid ervan
        bagofmnms[kleur] += 1
print(bagofmnms) #hier print hij de zak met M&M's met de value's (de hoeveelheid M&M's)