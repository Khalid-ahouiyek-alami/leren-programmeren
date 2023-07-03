import random
import time 

def deal_card():
    CARDS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'king', 'boer', 'queen', 'ace') # kaart (Ace is 11)
    return random.choice(CARDS)

def calculate_score(hand):
    # score = sum(hand)
    score= 0
        
    for kaart in hand:
        if kaart == 'queen':
            score += 10
        elif kaart == 'king':
            score += 10
        elif kaart == 'boer':
            score += 10
        elif kaart == 'ace':
            score += 11
        else:
            score += kaart
    


    if score == 21 and len(hand) == 2:
        return 0  # Blackjack (player wins with 21)
  # Convert Ace from 11 to 
    return score

def handel_game():
    player_cards = []
    dealer_cards = []
    
    # Deal initial cards
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    print("jouw kaarten:", player_cards)
    time.sleep(2)
    print("Dealer's kaarten:", dealer_cards[0])
    time.sleep(2)
    
    while True:
        choice = input("Do you want to hit or stand? ").lower()
        
        if choice == "hit":
            player_cards.append(deal_card())
            print("Your cards:", player_cards)
            
            score = calculate_score(player_cards)
            if score > 21:
                print("You went over 21. You lose!")
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



print("Welkom to khalid's Blackjack!")
time.sleep(2)
while True:
    handel_game()
    choice = input("wil je nog een keer spelen? (yes/no) ").lower()
    if choice == 'no':
        break
print("dankjewel voor het spelen")

