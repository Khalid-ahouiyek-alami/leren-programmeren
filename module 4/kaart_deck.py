from random import shuffle

kaart_kleur = ["harten", "klaveren", "schoppen ","ruiten"]
kaart_soort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "boer", "queen", "king", "ace"]
deck =[]

for x in range(4):
        for y in range(13):
            deck.append(kaart_kleur[x] + ' ' + str(kaart_soort[y]))   #hier haalt hij elke soort met de kleur uit de lists en zet het in de deck
        for z in range(2):             #deze zet 2 jokers in het deck
            deck.append('joker')      #hier zet hij het in de deck              
shuffle(deck)# deze laat de alle kaarten schudden
print(deck)
for a in range(1, 8): #deze regel zorgt er voor dat er 8 kaarten worden gepakt voor de speler
    print(f'kaart {a}: {deck[0]}')
    deck.pop(0) #door de "pop" worden die kaarten die zijn gepakt uit de list gehaald

print(deck)