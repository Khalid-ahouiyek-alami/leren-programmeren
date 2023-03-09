from fruitmand import fruitmand
goeie_kleur= {}
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
if fruitmand('color') == kleur_keuze:
    for x in fruitmand:
        print(fruitmand('round'))
