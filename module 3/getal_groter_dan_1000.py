getal = 50
som = 50
zin = '50'

while som < 1000:
    getal += 1 #zo lang dat de getal onder de duizend blijft doet het plus 1 bij de getal doen tot dat het de duizend berijkt 
    som = som + getal #hier word de som bij elkaar geteld en bij de variable "som" gezet
    zin += (f' + {getal}') #dit zorgt ervoor dat de hele som word geprint naast het getal
    print(f'{zin} = {som}') #dit print de geheel van de som uit 