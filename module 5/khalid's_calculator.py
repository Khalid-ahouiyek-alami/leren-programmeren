def addition(nummer1: float, nummer2: float) -> float:
    antwoord = nummer1 + nummer2
    return antwoord

def subtraction(nummer1: float, nummer2: float) -> float:
    antwoord = nummer1 - nummer2
    return antwoord

def multiplication(nummer1: float, nummer2: float) -> float:
    antwoord = nummer1 * nummer2
    return antwoord

def division(nummer1: float, nummer2: float) -> float:
    antwoord = nummer1 / nummer2
    return antwoord

def square(nummer1: float) -> float:
    antwoord = nummer1 * nummer1
    return antwoord


nummer1 = float(input('welk getal wil je mee beginen'))

while True:
    choice = input('wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) kwadrateren q|')
    
    if choice == 'a':
        nummer2 = float(input('met welk getal wilt u het vermenigvuldigen'))
        print(addition(nummer1, nummer2))
        nummer1 = addition(nummer1, nummer2)
    
    elif choice == 'b':
        nummer2 = float(input('welk tweede getal wil je'))
        print(subtraction(nummer1, nummer2))
        nummer1 = subtraction(nummer1, nummer2)
   
   
    elif choice == 'c':
        nummer2 = float(input('welk tweede getal wil je'))
        print(multiplication(nummer1, nummer2))
        nummer1 = multiplication(nummer1, nummer2)
    
    
    elif choice == 'd':
        nummer2 = float(input('welk tweede getal wil je'))
        print(division(nummer1, nummer2))
        nummer2 = division(nummer1, nummer2)
    
   
    elif choice == 'e':
        nummer2 = 1
        print(addition(nummer1, nummer2))
        nummer1 = addition(nummer1, nummer2)
    
    
    elif choice == 'f':
        nummer2 = 1
        print(subtraction(nummer1, nummer2))
        nummer1 = subtraction(nummer1, nummer2)
   
   
    elif choice == 'g':
        nummer2 = 2
        print(multiplication(nummer1, nummer2))
        nummer1 = multiplication(nummer1, nummer2)
    
    
    elif choice == 'h':
        nummer2 = 2
        print(division(nummer1, nummer2))
        nummer1 = division(nummer1, nummer2)

    elif choice == 'q':
        print(square(nummer1))
        nummer1 = square(nummer1)

    elif choice == 'i':
        break





    