import random

geheimen_getal = random.randint(1, 1000)
attempts = 0
score = 0
round_count = 0

while round_count < 20:
    geraden_getal = int(input("geus a number between 1 and 1000: "))
    attempts += 1

    if geraden_getal == geheimen_getal:
        print("Correct! You've won this round.")
        score += 1
        round_count += 1
        geheimen_getal = random.randint(1, 1000)
        attempts = 0
        if round_count == 20:
            break
        nog_een_keer = input("Do you want to play another round? (y/n) ")
        if nog_een_keer == "n":
            break
    elif geraden_getal < geheimen_getal:
        print("The number is higher.") 
    else:
        print("The number is lower.")

    if abs(geraden_getal - geheimen_getal) < 50:
        print("You're warm.")
    if abs(geraden_getal - geheimen_getal) < 20:
        print("You're very warm.")

    if attempts == 10:
        print("You've reached the maximum number of attempts for this round.")
        round_count += 1
        geheimen_getal = random.randint(1, 1000)
        attempts = 0
        if round_count == 20:
            break
        nog_een_keer = input("Do you want to play another round? (y/n) ")
        if nog_een_keer == "n":
            break

print("Your final score is", score)
