from fruitmand import fruitmand
teller_rond= 0
teller_niet_rond= 0
kleuren = {}
for x in fruitmand:
    kleuren.update ({x.get("color"): x.get("name")})
   

kleur_keuze=input("noem een kleur:  ")
while True:
    if kleur_keuze not in kleuren:
        print(f"De kleur :{kleuren} zit er niet in de fruitmand")
    else:
        print("het zit er in")
        
        
        
        break
#--------------------------------------------------------------------------#    
for fruit in fruitmand:
    if kleur_keuze:
        if teller_rond: