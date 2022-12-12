import random




print(input(" Je bent een persoon die in de woestijn loopt "))
print(input("je loopt langs een rune"))


antwoord_vraag_rune= input("loop je door??  | ja of nee   ")

if antwoord_vraag_rune =="ja":
    print("je bent uitgedroogt en je bent dood gegaan")
    quit()   

elif antwoord_vraag_rune == "nee":
    print("je gaat nu naar binnen")

print("je vind een rugtas")

antwoord_vraag_rugtas= (input("neem je de rugtas mee | ja of nee  "))

if antwoord_vraag_rugtas == 'ja' or 'nee':
    print("je loopt een stukje door")
    
    antwoord_vraag_links_of_rechts = input("je vind een plek waar je een keuze moet maken tussen |   links of rechts")
    
if antwoord_vraag_links_of_rechts == 'links':
        print("er is een val!!!")
        challenge_naar_de_tombe= input("ga je de challenge aan ??|   ja of nee")
        if challenge_naar_de_tombe == "ja":
            challenge_rekensom = random.randint(0,20)
            som1 = challenge_rekensom * challenge_rekensom
            som2 = (f'wat is de antwoord van de rekensom??|   {challenge_rekensom} x {challenge_rekensom}')
            print(som2)
            antwoord_som = int(input('wat is je antwoord'))
            if antwoord_som == som1:
                print("omdat je de som goed hebt mag je naar de tombe als beloning")
            else:
                print("je wordt gestraft jij dombo")
if antwoord_vraag_links_of_rechts == 'rechts':
        print("je komt aan bij een soort van glijbaan en glijdt naar beneden")
        print("je bent  in de tombe aangekomen")

        vraag_beeldtje_menemen= input("wil je de beeldtje menemen|   ja of nee")
        if vraag_beeldtje_menemen == "ja" or "nee":
            print("je bent nu buiten en je wacht op de helicopter")
            print('de helicopter is aangekomen')
   
antwoord_vraag_rugtas2= (input("heb je de rugtas bij |   ja of nee"))
if antwoord_vraag_rugtas2 == "ja":
        print("je mag mee met de helikipoter")
        print("je hebt gewonnen")
    
if antwoord_vraag_rugtas2 == "nee":
    antwoord_rugtas_terug_gaan= (input("ga je terug om de tas te halen|    ja of nee"))
    if antwoord_rugtas_terug_gaan == "nee":
        print("je wordt achter gelaten in de woestijn")
    else: 
        print("je mag mee met de helicopter")
        print("je hebt gewonnen")