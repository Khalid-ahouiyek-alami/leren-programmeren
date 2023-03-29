boodschappenlijst = {} # hier maakt hij een dict aan voor de producten(keys) en de hoeveelheid(value)
extra_invoegen = "ja"
while extra_invoegen == "ja": #als de antwoord bij zin 10 ja is dan voert hij de loop nog een x uit 
    product = input("Welk product wil je: ")
    aantal = int(input(f"Hoeveel {product} wil je: "))
    if product not in boodschappenlijst:    #hier in zin 6/7 als de product niet in de dict staat dan maakt hij een nieuwe key en value aan in de dict
        boodschappenlijst.update({product : aantal})    
    else:
        boodschappenlijst[product] += aantal
    extra_invoegen = input("Wil je nog een product toevoegen ja/nee: ")#hier vraagt de progamma of je nog wil invoegen "zo ja" dan voert hij de vraag nog een x uit
print("----{MOOIE BOOTSCHAPPENlijs}----")
for p , a in boodschappenlijst.items():
    print(f"{p}x {a}") #hier in zin 12 t/m 13 print hij de hele dict uit 
print("---------------------------")