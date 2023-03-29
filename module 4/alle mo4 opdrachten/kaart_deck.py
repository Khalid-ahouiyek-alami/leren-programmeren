from random import shuffle

kaart_kleur = ["harten", "klaveren", "schoppen ","ruiten"]
kaart_soort = ["boer", "queen", "king", "ace"]
deck =["joker1", "joker2"]

for kleur in kaart_kleur:
        for soorten in kaart_soort:
            deck.append(kleur + ' ' + (soorten))   #hier haalt hij elke soort met de kleur uit de lists en zet het in de deck
        for nummer in range(2, 11):
             kaart= kleur + '  ' + str(nummer)
             deck.append(kaart)
#-------------------------------------------------------------------------------------------------------------------------------#
shuffle(deck)# deze laat de alle kaarten schudden
print(deck)
for a in range(1, 8): #deze regel zorgt er voor dat er 8 kaarten worden gepakt voor de speler
    print(f'kaart {a}: {deck[0]}')
    deck.pop(0) #door de "pop" worden die kaarten die zijn gepakt uit de list gehaald

print(deck) 