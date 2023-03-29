from fruitmand import fruitmand
teller_rond= 0
teller_niet_rond= 0
kleuren = []
for x in fruitmand:
    kleuren.append(x['color'])
print(kleuren) 

kleur_keuze=input("noem een kleur:  ")
while True:
    if kleur_keuze not in kleuren:
        print(f"De kleur :{kleur_keuze} zit er niet in de fruitmand")
        break
    else:
        print("het zit er in")
        
        break
#--------------------------------------------------------------------------#    
for fruit in fruitmand:
    if kleur_keuze in fruit["color"]:
        if fruit['round'] :
            teller_rond += 1
        elif fruit['round']:
            teller_niet_rond += 1

print(teller_niet_rond) 
print(teller_rond)

meer_ronde = teller_rond - teller_niet_rond
meer_niet_teller = teller_niet_rond - teller_rond

if teller_rond > teller_niet_rond:
    print(f"Er zijn {teller_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur_keuze}")
elif teller_rond < teller_niet_rond:
    print(f"Er zijn {teller_niet_rond} meer niet ronde vruchten dan ronde vruchten in de kleur {kleur_keuze}")
elif teller_rond == teller_niet_rond:
    print(f"Er zijn {teller_rond} ronde vruchten en {teller_niet_rond} niet ronde vruchten in de kleur {kleur_keuze}")