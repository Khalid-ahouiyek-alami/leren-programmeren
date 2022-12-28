teller = 0 
antwoord = " "

while antwoord != "quit": #dus als antwoord niet gelijk is aan quit gaat het door 
    antwoord = input('?') #dus als je op enter hebt gedrukt print de progamma de (?)  
    teller += 1 # dit doet elke keer als je op enter drukt er een bij de teller (zie regel 1)
print(f'aantal enters: {teller}') #met dit print die de zin met de aantal keer dat je enter hebt gedrukt 