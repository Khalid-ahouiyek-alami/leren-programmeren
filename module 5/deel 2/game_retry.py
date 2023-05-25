import random

def start_game():
    print("Welkom to khalid's Blackjack!")
    
    player_cards = []
    dealer_cards = []
    
    # Deal initial cards
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    print("jouw kaarten:", player_cards)
    print("Dealer's kaarten:", dealer_cards[0])
    
    spelers_beurt(player_cards, dealer_cards)

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # kaart (Ace is 11)
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack (player wins with 21)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)  # Convert Ace from 11 to 1
    return score

def spelers_beurt(player_cards, dealer_cards):
    while True:
        choice = input("Do you want to hit or stand? ").lower()
        
        if choice == "hit":
            player_cards.append(deal_card())
            print("Your cards:", player_cards)
            
            score = calculate_score(player_cards)
            if score > 21:
                print("You went over 21. You lose!")
                play_again()
                break
        elif choice == "stand":
            dealer_turn(player_cards, dealer_cards)
            break
        else:
            print("Invalid choice. Try again.")

def dealer_turn(player_cards, dealer_cards):
    dealer_score = calculate_score(dealer_cards)
    
    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    
    print("Your cards:", player_cards)
    print("Dealer's cards:", dealer_cards)
    print("Your score:", calculate_score(player_cards))
    print("Dealer's score:", dealer_score)
    
    if dealer_score > 21:
        print("Dealer went over 21. You win!")
    elif dealer_score == calculate_score(player_cards):
        print("It's a draw!")
    elif dealer_score > calculate_score(player_cards):
        print("Dealer wins!")
    else:
        print("You win!")

    play_again()

def play_again():
    choice = input("wil je nog een keer spelen? (yes/no) ").lower()
    
    if choice == "yes":
        start_game()
    else:
        print("dankjewel voor het spelen")

start_game()