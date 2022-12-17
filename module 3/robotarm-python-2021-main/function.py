# def vraagr_een_getal(vraag: str) -> int: #betekent definieer = maak aan
#     while True:
#         try:  
#             getal = int(input(vraag))
#             break
#         except ValueError:
#             print('je moet een getal invoeren')
#             continue
#     return getal



# leeftijd = vraagr_een_getal('voer u leeftijd in')
# geboorte_jaar = vraagr_een_getal('voer je geboorte jaar in')
# geboorte_maand = vraagr_een_getal('voer je geboorte maand in')
# geboorte_dag = vraagr_een_getal('voer je geboorte dag in')



# print(leeftijd)
# print(geboorte_jaar)



# while True:
#     try:  
#         geboorte_jaar = int(input('voer u leeftijd in'))
#         break
#     except ValueError:
#         print('je moet een getal invoeren')
#         continue
# --------------------------------------------------------------------------------------
def stel_vraag_return_anwoord_lower(vraag: str) -> str:
    antwoord = input(vraag).lower()
    return antwoord
print(stel_vraag_return_anwoord_lower)
s