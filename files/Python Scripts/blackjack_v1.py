

import random

def create_shuffled_deck() -> list:
    """
    Returns a list containing strings that represent cards in a standard deck.

    Returns:
        deck (list):        Contains 52 elements representing the value and suit
                            for each card in a standard deck.
    """
    numbers = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    deck = []
    for j in "hdsc":
        for i in numbers:
            deck += i+j,
    random.shuffle(deck)
    return deck

def value(hand: list) -> int:
    """
    returns value of hand as an int

    Arg:
        hand    (list): list containing strings representing cards

    Returns     (int): int representing value of hand

    Example:
    >>>value["Ah"]
       11

    """
    hand_value = 0
    a = 0
    for i in hand:
        i = i[:-1]
        if i == "A":
            a += 1
        elif i not in "123456789":
            i = 10
            hand_value += int(i)
        else:
            hand_value += int(i)
    for i in range(a):
        if hand_value + 11 > 21:
            hand_value += 1
        else:
            hand_value += 11
    return hand_value

def handchecker(d_value: int, p_value: int, money: int, initial_bet: int) -> tuple:
    """
    checks if hand is over or is black jack and returns money of player and if
    game is over

    Arg:
        d_value (int): value of dealers hand
        p_value (int): value of players hand
        money   (int): players current money
        initial_bet (int): how much player bet

    Returns:    (tuple): two element tuple with a boolean to indicate if game is
    over and how much money player has

    Example:
    >>>handchecker(21,10,20)
       (50, True)
    """

    if p_value == 21 and d_value != 21:
        print("Blackjack!")
        money += initial_bet * 2
        print("Money:", money)
        return money, True

    elif p_value == 21 and d_value == 21:
        print("Tie! Dealer and Player Blackjack!")
        money += initial_bet
        print("Money:", money)
        return money, True

    elif p_value > 21:
        print("Bust")
        print("Money:", money)
        return money, True
    else:
        return money, False

def showdown(deck: list, dealer_hand: list, d_value: int, p_value: int, money: int, initial_bet: int) -> int:
    """
    Simulates what the dealer does after a player stands or double downs

    Arg:
        deck    (list): list of strings representing deck used in blackjack
        dealer_hand (list): list of strings representing hand of dealer
        d_value (int): int representing value of dealer hand
        p_value (int): int representing value of player hand
        money   (int): int representing how much money player has
        initial_bet (int): int representing how much money player bet

    Return  (int): int representing how much money player has
    """
    while d_value < 17:
        print("dealer hand:", dealer_hand)
        dealer_hand += [deck.pop(0)]
        print("dealer hand:", dealer_hand)
        d_value = value(dealer_hand)
    if d_value > 21:
        print("Dealer Bust!")
        money += initial_bet * 2
        print("Money:", money)
        return money
    elif d_value > p_value:
        print("You Lose!")
        print("Money:", money)
        return money
    elif p_value > d_value:
        print("You Win!")
        money += initial_bet * 2
        print("Money:", money)
        return money
    else:
        print("Tie")
        money += initial_bet
        print("Money:", money)
        return money

def blackjack(money: int) -> int:
    """
    Interactive Blackjack game

    Arg:
        money   (int): how much money player has

    Returns     (int): how much money player has after game

    """

    if money < 5:
        return "Too Poor Boo Hoo, Min 5$ to play"
    #create and combine 6 shuffuled decks
    deck = create_shuffled_deck()
    deck += create_shuffled_deck()
    deck += create_shuffled_deck()
    deck += create_shuffled_deck()
    deck += create_shuffled_deck()
    deck += create_shuffled_deck()


    #first hand
    initial_bet = int(input("Please enter an initial bet (min 5$)"))
    money -= initial_bet
    dealer_hand = [deck.pop(0)]
    player_hand = [deck.pop(0)]
    dealer_hand += [deck.pop(0)]
    player_hand += [deck.pop(0)]
    print("Hand:", player_hand)
    print("Dealer Faceup Card:", dealer_hand[0], ", ??")
    result = False

    #player action
    while result == False:
        action = input("F to fold, H to hit, S to stand, D to double down, SP to split")
        action = action.upper()

        #fold
        if action == "F":
            money += initial_bet//2
            result = True
            print("Money left: " + money)

        #hit
        #checks blackjack and bust
        elif action == "H":
            player_hand += [deck.pop(0)]
            print("Hand:", player_hand)
            p_value = value(player_hand)
            d_value = value(dealer_hand)
            money, result = handchecker(d_value, p_value, money, initial_bet)


        #stand
        #dealer and player "showdown"
        elif action == "S":
            d_value = value(dealer_hand)
            p_value = value(player_hand)
            money = showdown(deck, dealer_hand, d_value, p_value, money, initial_bet)
            result = True

        #double down
        #checks blackjack and bust
        #dealer and player "showdown"
        elif action == "D":
            money -= initial_bet
            initial_bet = initial_bet * 2
            player_hand += [deck.pop(0)]
            print("Hand:", player_hand)
            p_value = value(player_hand)
            d_value = value(dealer_hand)
            money, result = handchecker(d_value, p_value, money, initial_bet)
            if result == False:
                money = showdown(deck, dealer_hand, d_value, p_value, money, initial_bet)
                result = True

        #Invalid input
        else:
            print("Invalid Input")

    return money

def gameloop(money:int):
    """
    Allows player to play blackjack continously

    Arg:
        money   (int): how much money a player has

    Return: None

    """
    again = "Y"
    while again == "Y" and money >= 5:
        money = blackjack(money)
        again = input("play again? Y/N")
        again = again.upper()
    if money < 5:
        print("You suck at gambling ")
    else:
        print("WHY STOP GAMBLING?!?!?")
