def addition(number1: float, number2: float) -> float:
    antwoord = number1 + number2
    return antwoord

def subtraction(nummer1: float, nummer2: float) -> float:
    antwoord2 = nummer1 - nummer2
    return antwoord2

def multiplication(nb1: float, nb2: float) -> float:
    antwoord3 = nb1 * nb2
    return antwoord3

def division(nb3: float, nb4: float) -> float:
    antwoord4 = nb3 / nb4
    return antwoord4

nummer2 = float(input('welk getal wil je mee beginen'))

while nummer2 == True:
    choice = input('wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?')
    
    if choice == 'a':
        nummer2 = float(input('met welk getal wilt u het vermenigvuldigen'))
        print(addition(nummer2, nummer2))
        nummer2 = addition(nummer2, nummer2)
    
    elif choice == 'b':
        nummer2 = float(input('welk tweede getal wil je'))
        print(subtraction(nummer2, nummer2))
        nummer2 = subtraction(nummer2, nummer2)
   
   
    elif choice == 'c':
        nummer2 = float(input('welk tweede getal wil je'))
        print(multiplication(nummer2, nummer2))
        nummer2 = multiplication(nummer2, nummer2)
    
    
    elif choice == 'd':
        nummer2 = float(input('welk tweede getal wil je'))
        print(division(nummer2, nummer2))
        nummer2 = division(nummer2, nummer2)
    
   
    elif choice == 'e':
        nummer2 = 1
        print(addition(nummer2, nummer2))
        nummer2 = addition(nummer2, nummer2)
    
    
    elif choice == 'f':
        nummer2 = 1
        print(subtraction(nummer2, nummer2))
        nummer2 = subtraction(nummer2, nummer2)
   
   
    elif choice == 'g':
        nummer2 = 2
        print(multiplication(nummer2, nummer2))
        nummer2 = multiplication(nummer2, nummer2)
    
    
    elif choice == 'h':
        nummer2 = 2
        print(division(nummer2, nummer2))
        nummer2 = division(nummer2, nummer2)
   
   
    elif choice == 'i':
        break







    