
import tkinter as tk
import blackjack_v1 as bj
import card_visuals as cv

#Create Window
GUI = tk.Tk()
GUI.title("Blackjack")
GUI.geometry("600x400")




def start_game():
    """
    Simulates the game of blackjack after player presses start game button
    """

    #global variables
    global balance
    global initial_bet
    global dealer_hand
    global player_hand
    global deck
    global p_value
    global d_value

    #define variables
    balance = int(money_entry.get())-int(bet_entry.get())
    initial_bet = int(bet_entry.get())
    

    #deck and hand
    deck = bj.create_shuffled_deck()
    deck += bj.create_shuffled_deck()
    deck += bj.create_shuffled_deck()
    deck += bj.create_shuffled_deck()
    deck += bj.create_shuffled_deck()
    deck += bj.create_shuffled_deck()
    dealer_hand = [deck.pop(0)]
    player_hand = [deck.pop(0)]
    dealer_hand += [deck.pop(0)]
    player_hand += [deck.pop(0)]





    #gameover
    def gameend():
            """
            Ends the game and allows the game to be played again after game is over
            """
            def no():
                """
                Executes when player does not want to play again 
                """
                gameover.config(text = "WHY STOP GAMBLING?!?!?")
            def yes():
                """
                Restarts game to play again after player chooses so while saving their current balance
                so it does not need to be entered again
                """
                #place_forget
                money.place_forget()
                gamestate.place_forget()
                pcards.place_forget()
                dcards.place_forget()
                plabel.place_forget()
                dlabel.place_forget()
                standd.place_forget()
                hitt.place_forget()
                doublee.place_forget()
                foldd.place_forget()
                gameover.place_forget()
                yess.place_forget()
                noo.place_forget()


                #place
                start.place(x = 0, y = 0)
                start_money.place(y = 25, x = 0)
                money_entry.place(y = 25, x = 180)
                bet.place(y = 50, x = 0)
                bet_entry.place(y = 50, x = 200)

                #text deletion
                money.config(state = tk.NORMAL)
                gamestate.config(state = tk.NORMAL)
                pcards.config(state = tk.NORMAL)
                dcards.config(state = tk.NORMAL)
                money.delete("1.0","end")
                gamestate.delete("1.0","end")
                pcards.delete("1.0","end")
                dcards.delete("1.0","end")
                money.config(state = tk.DISABLED)
                gamestate.config(state = tk.DISABLED)
                pcards.config(state = tk.DISABLED)
                dcards.config(state = tk.DISABLED)
                money_entry.delete(0,tk.END)
                bet_entry.delete(0,tk.END)
                money_entry.insert(tk.END, f"{str(balance)}")


            #buttons and labels
            gameover = tk.Label(GUI, text = "Gameover, Play Again?")
            yess = tk.Button(GUI, text = "Yes", command = lambda: yes())
            noo = tk.Button(GUI, text = "No", command = lambda: no())

            #place
            gameover.place(y = 130, x = 0)
            yess.place(y = 150, x = 0)
            noo.place(y = 150, x = 37)
    
    def handchecker() -> bool:
        """
        checks if hand is over/bust or black jack and returns gamestate (over or not) as boolean

        Returns:    (bool): if game is over or not

        Example:
        >>>handchecker(21,10,20)
        True
        """

        global balance
        global initial_bet

        #checks blackjack win
        if p_value == 21 and d_value != 21:
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END, "Blackjack!\n")
            balance += initial_bet * 2
            gamestate.insert(tk.END, f"Money: {balance}\n")
            gamestate.config(state = tk.DISABLED)
            return True

        #checks blackjack tie
        elif p_value == 21 and d_value == 21:
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END, "Tie! Dealer and Player Blackjack!\n")
            balance += initial_bet
            gamestate.insert(tk.END, f"Money: {balance}\n")
            gamestate.config(state = tk.DISABLED)
            return True

        #checks bust
        elif p_value > 21:
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END,"Bust\n")
            gamestate.insert(tk.END, f"Money: {balance}\n")
            gamestate.config(state = tk.DISABLED)
            return True
        else:
            return False

    def showdown():
        """
        Simulates what the dealer does after a player stands or double downs
        """
        
        global balance
        global dealer_hand
        global d_value
        
        #show dealer hand
        dcards.config(state = tk.NORMAL)
        dcards.delete("1.0","end")
        dcards.insert(tk.END,f"{cv.card_to_art(dealer_hand)}\n")
        dcards.config(state = tk.DISABLED)

        #draw cards until atleast 16
        while d_value < 17:
            dealer_hand += [deck.pop(0)]
            dcards.config(state = tk.NORMAL)
            dcards.delete("1.0","end")
            dcards.insert(tk.END,f"{cv.card_to_art(dealer_hand)}\n")
            dcards.config(state = tk.DISABLED)
            d_value = bj.value(dealer_hand)

        #check bust
        if d_value > 21:
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END,"Dealer Bust!\n")
            balance += initial_bet * 2
            gamestate.insert(tk.END, f"Money: {balance}\n")
            gamestate.config(state = tk.DISABLED)
        
        #check player loss
        elif d_value > p_value:
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END,"You Lose!\n")
            gamestate.insert(tk.END, f"Money: {balance}\n")
            gamestate.config(state = tk.DISABLED)
        
        #check player win
        elif p_value > d_value:
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END,"You Win!\n")
            balance += initial_bet * 2
            gamestate.insert(tk.END, f"Money: {balance}\n")
            gamestate.config(state = tk.DISABLED)
        
        #check tie
        else:
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END,"Tie!\n")
            balance += initial_bet
            gamestate.insert(tk.END, f"Money: {balance}\n")
            gamestate.config(state = tk.DISABLED)
        
    def fold() -> int:
        """
        simulates folding in blackjack
        """
        
        global balance

        #returns money
        balance += initial_bet//2

        #display money
        gamestate.config(state = tk.NORMAL)
        gamestate.insert(tk.END,f"Money left: {balance}\n")
        gamestate.config(state = tk.DISABLED)

        #end the game
        gameend() 

    def hit():
        """
        simulates hitting in blackjack
        """
        global player_hand
        global p_value

        #deal a card
        player_hand += [deck.pop(0)]

        #display hand
        pcards.config(state = tk.NORMAL)
        pcards.delete("1.0","end")
        pcards.insert(tk.END, f"{cv.card_to_art(player_hand)}\n")
        pcards.config(state = tk.DISABLED)

        #check for bust or blackjack and ends game if so
        p_value = bj.value(player_hand)
        result = handchecker()
        if result == True:
            gameend() 

    def stand():
        """
        simulates standing in blackjack
        """
        #gets value of hands, then the result, and ends the game
        showdown()
        gameend() 
        
    def double():
        """
        simulates a double down in blackjack
        """
        global balance
        global player_hand
        global initial_bet
        global p_value

        #check if player can double
        if balance >= initial_bet:

            #take extra money out of balance for double
            balance -= initial_bet
            initial_bet = initial_bet * 2

            #Change display for money
            moneyt = f"Money: {balance} \n Bet: {initial_bet}"
            money.config(state = tk.NORMAL)
            money.delete("1.0","end")
            money.insert(tk.END, moneyt)
            money.config(state = tk.DISABLED)

            #deal a card
            player_hand += [deck.pop(0)]

            #show hand
            pcards.config(state = tk.NORMAL)
            pcards.delete("1.0","end")
            pcards.insert(tk.END, f"{cv.card_to_art(player_hand)}\n")
            pcards.config(state = tk.DISABLED)

            #check bust and blackjack
            p_value = bj.value(player_hand)
            result = handchecker()

            #dealer deals to himself if not bust or blackjack
            if result == False:
                showdown()

            #ends the game
            gameend() 
        else:

            #tells player they can't double without ending game
            gamestate.config(state = tk.NORMAL)
            gamestate.insert(tk.END, "You can't do that!\n")
            gamestate.config(state = tk.DISABLED)
        


    #Starts game after initial bet requirement is met
    if balance >= 0 and initial_bet >= 5:

        #check first hand
        p_value = bj.value(player_hand)
        d_value = bj.value(dealer_hand)
        result = handchecker()
        if result == True:
            gameend() 

        #money
        moneyt = f"Money: {balance} \n Bet: {initial_bet}"
        money.config(state = tk.NORMAL)
        money.insert(tk.END, moneyt)
        money.config(state = tk.DISABLED)

        #buttons
        foldd = tk.Button(GUI, text = "Fold", font = (14), command = lambda: fold())
        standd = tk.Button(GUI, text = "Stand", font = (14),command = lambda: stand())
        hitt = tk.Button(GUI, text = "Hit", font = (14),command = lambda: hit())
        doublee = tk.Button(GUI, text = "Double Down", font = (14),command = lambda: double())
        #split = tk.Button(GUI, text = "Split")

        #place
        money.place(x = 0, y = 0)
        gamestate.place(x = 300, y = 0)
        pcards.place(x = 0, y = 200)
        dcards.place(x = 300, y = 200)
        plabel.place(x = 0, y = 180)
        dlabel.place(x = 300, y = 180)
        standd.place(y = 60, x = 0)
        hitt.place(y = 60, x = 55)
        doublee.place(y = 90, x = 0)
        foldd.place(y=90,x = 108)
        #split.place(y = 60, x = 150)

        #forget
        bet_entry.place_forget()
        bet.place_forget()
        start_money.place_forget()
        money_entry.place_forget()
        start.place_forget()

        #display hands
        pcards.config(state = tk.NORMAL)
        dcards.config(state = tk.NORMAL)
        pcards.insert(tk.END,f"{cv.card_to_art(player_hand)}\n")
        dcards.insert(tk.END,f"{cv.card_to_art([dealer_hand[0]])}\U0001F0A0 \n")
        pcards.config(state = tk.DISABLED)
        dcards.config(state = tk.DISABLED)









#labels
bet = tk.Label(GUI, text = "Please enter initial bet of at least $5:")
start_money = tk.Label(GUI, text = "How much money do you have?")
plabel = tk.Label(GUI, text = "Player Hand")
dlabel = tk.Label(GUI, text = "Dealer Hand")

#entrys
bet_entry = tk.Entry(GUI)
money_entry = tk.Entry(GUI)

#startgame button
start = tk.Button(GUI, text = "Startgame", command = start_game)

#text
money = tk.Text(GUI, height = 3, width = 12, wrap=tk.WORD)
gamestate = tk.Text(GUI, height = 11, width = 37, wrap=tk.WORD)
pcards = tk.Text(GUI, height = 13, width = 30, font = ("Arial", 80), wrap=tk.WORD)
dcards = tk.Text(GUI, height = 13, width = 30, font = ("Arial", 80), wrap=tk.WORD)

#placing text
start.place(x = 0, y = 0)
start_money.place(y = 25, x = 0)
money_entry.place(y = 25, x = 180)
bet.place(y = 50, x = 0)
bet_entry.place(y = 50, x = 200)



GUI.mainloop()

