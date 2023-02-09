import random

geheimen_getal = random.randint(1, 1000)
pogingen = 0
score = 0
round_count = 0

while round_count < 20:
    geraden_getal = int(input("raad maar een nummer between 1 and 1000: "))
    pogingen += 1

    if geraden_getal == geheimen_getal:
        print("Correct! je hebt deze ronde gewonnen.")
        score += 1
        round_count += 1
        geheimen_getal = random.randint(1, 1000)
        pogingen = 0
        if round_count == 20:
            break
        nog_een_keer = input("wil je nog een ronde spelen? (j/n) ")
        if nog_een_keer == "n":
            break
    elif geraden_getal < geheimen_getal:
        print("The nummer is hoger.") 
    else:
        print("de nummer is lager.")

    if abs(geraden_getal - geheimen_getal) < 50:
        print("je bent warm.")
    if abs(geraden_getal - geheimen_getal) < 20:
        print("je bent heel warm.")

    if pogingen == 10:
        print("je hebt de max pogingen voor deze ronden")
        round_count += 1
        geheimen_getal = random.randint(1, 1000)
        pogingen = 0
        if round_count == 20:
            break
        nog_een_keer = input("wil je nog een ronde spelen? (j/n) ")
        if nog_een_keer == "n":
            break

print("je uiteindelijke score is", score)
