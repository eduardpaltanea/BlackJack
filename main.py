import random
from replit import clear
from art import logo
############### Blackjack Project #####################
def deal_card(list_of_cards):
    random_card = random.choice(list_of_cards)
    return random_card


def compare(score_calculator, score_player):
    if score_calculator == score_player:
        return "It's a draw!"
    elif score_calculator == 0:
        return "You lost! Computer has a BlackJack!"
    elif score_player == 0:
        return "You win with a BlackJack!"
    elif score_player > 21:
        return "You lost! Over 21"
    elif score_calculator > 21:
        return "You win! Computer over 21"
    elif score_player > score_calculator:
        return "You win! You had more points!"
    else:
        return "You lost! Computer had more points!"

def calculate_score(list_of_cards):
    score = sum(list_of_cards)
    if 11 in list_of_cards and 10 in list_of_cards and len(list_of_cards) == 2:
        return 0 #Blackjack
    elif 11 in list_of_cards and score > 21:
       list_of_cards.remove(11)
       list_of_cards.append(1)
    else:
        return int(score)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for number in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    game_over = False


    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")
        if user_score > 21 or computer_score == 0 or user_score == 0:
            game_over = True
        else:
            another_card = input("Do you want to draw another card?").lower()
            if another_card == "yes":
                game_over = False
                user_cards.append(deal_card(cards))
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is : {user_score}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score, user_score))

while input("Do you want to play a game of BlackJack? ").lower() == "yes":
    clear()
    play_game()



