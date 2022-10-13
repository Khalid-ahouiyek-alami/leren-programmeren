

name = input("what's your name? ")
if name == 'John':
    raise NameError('John is not welcome here!')
gender = input('bent u een man of vrouw? M/V ')                                               # M/V
if gender == 'M':
    snor = input('Heeft u een snor? J/N ')                                                    #J
    if snor == 'J':                                                                           
        snor_lengte = int(input('Hoeveel CM is uw snor? '))                                   # >10
elif gender == 'V':                                                       
    haar_kleur = input('Draagt u rood krulhaar? J/N ')                                        # J
    haar_lengte = int(input('Hoeveel CM is de lengte uw haar? '))                             # >20
hoed = input('Heeft u een hoge hoed? J/N ')
kleur_hoed = input("welke kleur is uw hoed? ")
rijbewijs = input('Heeft u een geldig Vrachtwagen rijbewijs? J/N ')                           # J
diploma = input('Heeft u een MBO-4 diploma? J/N ')                                            # J
lengte = int(input('Wat is uw lengte in CM? '))                                               # >150 and <220 
gewicht = int(input('hoeveel weegt u in KG? '))                                               # >90 and <120  
leeftijd = int(input("wat is uw leeftijd in jaren? "))
if leeftijd >=99:
    raise NameError('u bent te oud!')                                                         
certificaat = input('Heeft u de Certificaat overleven met gevaarlijk personeel? J/N ')        # J
dieren_dressuur = int(input('Hoeveel jaar praktijkervaring met dieren-dressuur heeft u? '))   # >4
jongleren = int(input('Hoeveel jaar ervaring met jongleren heeft u? '))                       # >5
acrobatiek = int(input('Hoeveel jaar praktijkervaring met acrobatiek heeft u? '))             # >3
ervaring = dieren_dressuur >=4 or jongleren >=5 or acrobatiek >=3

if gender == 'M' and ervaring and certificaat == 'J' and  diploma == 'J' and  rijbewijs == 'J' and  hoed == 'J' and snor == 'J' and snor_lengte >=10 and lengte >=150 <=220 and gewicht >=90 <=120:
    print('u bent geschikt ')

elif gender == 'V' and ervaring and certificaat == 'J' and  diploma == 'J' and  rijbewijs == 'J' and  hoed == 'J' and haar_kleur == 'J' and haar_lengte >=20 and lengte >=150 <=220 and gewicht >=90 <=120:
        print('u bent geschikt')

else:
    print('u bent niet geschikt')