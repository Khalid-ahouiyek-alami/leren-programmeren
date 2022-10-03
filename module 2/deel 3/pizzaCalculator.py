# Naam= khalid ahouiyek alami pizzaria
# opdracht =  Pizza calculator

small_pizza=  7.99
medium_pizza= 9.99
large_pizza = 12.99

#Voorbeeld een klant bestelde 1 small , 2 medium en 2 large!

Besteling_1 = int(input( " Hoeveel small pizza wilt u hebben?:"))
bestelding_2= int(input( " Hoeveel medium pizza wilt u hebben?:"))
bestelding_3 = int(input( " Hoeveel large pizza wilt u hebben?:"))

antwoord_1= (small_pizza * Besteling_1)
antwoord_2= (medium_pizza * bestelding_2)
antwoord_3= (large_pizza * bestelding_3)

totaal= antwoord_1 + antwoord_2 + antwoord_3

print("------------------------------------------")
print(F"|          khalid's heerlijke Pizza                 ")  

print(F"|{Besteling_1}  small pizza {antwoord_1} Euros")
print(F"|{bestelding_2}  medium pizza {antwoord_2} Euros")
print(F"|{bestelding_3}  large pizza {antwoord_3} Euros")
print(f"|Het totaal bedrag is = {totaal} Euros")

print("|Dankjewel voor het bestellen")
print("|------------------------------------------")