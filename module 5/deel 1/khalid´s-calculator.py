

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
    antwoord = nummer1 ** 2
    return antwoord

def sqaure_root(nummer1:float) -> float:
    antwoord =nummer1 ** 0.5 #die 2 sterretjes zijn net als ^....
    return antwoord

def to_the_power_of(nummer1:float, nummer2= float) -> float:
    antwoord =nummer1 ** nummer2 #die 2 sterretjes zijn net als ^....
    return antwoord


nummer1 = float(input('welk getal wil je mee beginen'))

while True:
    choice = input('wat wilt u doen?  getallen optellen A) ,  getallen aftrekken B) ,  getallen vermenigvuldigen C),  getallen delen D),  getal ophogen E),  getal F) verlagen, G) getal verdubbelen of H) kwadrateren q) sqaure root s) to_the_power_of p)')
    
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
        nummer1 = division(nummer1, nummer2)
        print(nummer1)

    elif choice == 'q':
        print(square(nummer1))
        nummer1 = square(nummer1)

    elif choice == 's':
        nummer1 = sqaure_root(nummer1)
        print(nummer1)

    elif choice == 'p':
        nummer2 = float(input('welk tweede getal wil je'))
        print(to_the_power_of(nummer1, nummer2))
        nummer1 = to_the_power_of(nummer1, nummer2)
       
    
    
    elif choice == 'i':
        print("""het je hebt het gestopt
run het weer opnieuw als je het wilt gebruiken""")
        break





    