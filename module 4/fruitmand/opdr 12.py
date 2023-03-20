from fruitmand import fruitmand
naam_fruit = ''
kleur_fruit = ''
gewicht_fruit = 0
letters_hoeveelheid = 0
for fruit in fruitmand:
    if letters_hoeveelheid < len(fruit['name']):
        naam_fruit = fruit['name']
        kleur_fruit = fruit['color']
        gewicht_fruit = fruit['weight']
        letters_hoeveelheid = len(fruit['name'])
print(f"De {naam_fruit} ({letters_hoeveelheid}) heeft een {kleur_fruit} kleur en een gewicht van {gewicht_fruit / 1000} kg.")