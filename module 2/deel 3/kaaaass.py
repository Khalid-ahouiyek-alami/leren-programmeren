from cgi import print_arguments


geel = input('is de kaas geel?')
if geel == 'ja':
    gaten = input('zitten er gaten in?')
    if gaten == 'nee':
        hard = input('is deze kaas hard als steen?')
        if hard == 'ja':
            print('De kaas die jij bedoelt is de Parmigiano Reggiano.')
        if hard == 'nee':
            print('De kaas die jij bedoelt is de Goudse kaas.')
    elif gaten == 'ja':
        duur = input('is de kaas belachelijk duur?')
        if duur == 'ja':
            print('De kaas die jij bedoelt is de Emmenthaler.')
        if duur == 'nee':
            print('De kaas die jij bedoelt is de Leerdammer.')
elif geel == 'nee':
    blauwe_schimmel = input('heeft de kaas blauwe schimmel?')
    if blauwe_schimmel == 'nee':
        korst = input('heeft de kaas een korst?')
        if korst == 'ja':
            print('De kaas die jij bedoelt is de Camembert.')
        elif korst == 'nee':
            print('De kaas die jij bedoelt is de Mozzarella.')
    if blauwe_schimmel == 'ja':
        korst = input('heeft de kaas een korst?')
        if korst == 'ja':
            print('De kaas die jij bedoelt is de Blue de Rochbaron')
        elif korst == 'nee':
            print("De kaas die jij bedoelt is de Foume d'Ambert.")

        

        
