small_p=  7.99
medium_p = 9.99
large_p = 12.99

#Voorbeeld een klant bestelde 1 small , 2 medium en 2 large!

Besteling1 = 0
bestelding2 = 0
bestelding3 = 0
try:
    Besteling1 = int(input(" Hoeveel small pizza wilt u hebben?:"))
    bestelding2= int(input(" Hoeveel medium pizza wilt u hebben?:"))
    bestelding3 = int(input(" Hoeveel large pizza wilt u hebben?:"))
except ValueError:
    print("Vul een getal in !!!:")

antwoord_1= (small_p * Besteling1)
antwoord_2= (medium_p * bestelding2)
antwoord_3= (large_p * bestelding3)

totaal= antwoord_1 + antwoord_2 + antwoord_3

print("------------------------------------------")
print(F"|          khalid's heerlijke Pizza      ")  

print(F"|{Besteling1}  small pizza {antwoord_1} Euros")
print(F"|{bestelding2}  medium pizza {antwoord_2} Euros")
print(F"|{bestelding3}  large pizza {antwoord_3} Euros")
print(f"|Het totaal bedrag is = {totaal} Euros")

print("|Dankjewel voor het bestellen")
print("|------------------------------------------")