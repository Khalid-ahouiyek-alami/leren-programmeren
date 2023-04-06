def get_persoon():
    naam = input("Voer de naam in: ")
    leeftijd = int(input("Voer de leeftijd in: "))
    return {"naam": naam, "leeftijd": leeftijd}

alle_mensen = []
while True:
    doorgaan_of_niet = input("Toets enter om door te gaan of stop om te printen: ")
    if doorgaan_of_niet == "stop":
        break
    persoon = get_persoon()
    alle_mensen.append(persoon)

print("Lijst van persoonen:")
for persoon in alle_mensen:
    print(f"{persoon['naam']} ({persoon['leeftijd']} jaar)")