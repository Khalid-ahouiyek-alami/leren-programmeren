from fruitmand import fruitmand

watermeloen = { 
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermeloen)

volledig_gewicht = 0
for alle_fruit in fruitmand:
    volledig_gewicht = volledig_gewicht + alle_fruit['weight']
print(f' totaal gewicht van de fruitmand is: {volledig_gewicht}')
    