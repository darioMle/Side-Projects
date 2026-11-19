#trying to use OOP
#UNO game


#imports
import time
import random


class Card:
    #the two arrays for cards
    player_cards = []
    bot_cards = []

    #general
    colours = ["green", "red", "blue", "yellow"]
    rare_cards = ["colour_change"]
    normal_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    
    def __init__ (self, number, colour: str, owner: str):

        #errors
        if number != "colour_change":
            assert number >= 1 and number <= 9, f"Your number ({number}) has to be between 1 and 9"
        
        if colour != "special!":
            assert colour in self.colours, f"Your colour ({colour}) has to be a real colour or special"
            
        assert owner in ("bot", "player"), f"Your player ({owner}) has to be either bot or player"

        #variables
        self.number = number
        self.colour = colour
        self.owner = owner

        #owner appending
        if owner == "player":
            Card.player_cards.append(self)

        else:
            Card.bot_cards.append(self)



        
    def playable(self, current_card, current_colour):
        
        #is it playable?
        if current_card is None or self.number == current_card.number or self.colour == current_colour or self.colour == "special!":
             return True

        else:
            return False
    


    def __repr__ (self):
        #stores each object readably
        return f"{self.number} {self.colour}"






class Game:

    def __init__(self):
        self.current_card = None
        self.current_colour = None
        self.lp = None

    def __repr__(self):
        return f"The current colour is {self.current_colour} and the current card is {self.current_card}"


    def typeout(self, text, delay=0.01):
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(delay)
        print()


    def show_player_cards(self):
        print(f"These are your {len(Card.player_cards)} cards:")
        print()

        for card in Card.player_cards:
            print(card)

        print()
        print("Or 'pass' to gain a new card.")

    def generate_card(self, user):
        number = random.choice(Card.normal_cards)
        colour = random.choice(Card.colours)

        if number >= 10:
            number = "colour_change"
            colour = "special!"

        Card(number, colour, user)


    def bot_starts(self):
        i = random.randrange(len(Card.bot_cards))

        self.current_card = Card.bot_cards[i]

        if self.current_card.colour == "special!":
            self.current_colour = random.choice(Card.colours)
            
        else:
            self.current_colour = self.current_card.colour


        print("-------------------------------")

        if self.current_card.colour == "special!":
            print("The bot puts down", self.current_card, "and chooses", self.current_colour)
        
        else:
            print("The bot puts down", self.current_card)

        print("-------------------------------")

        Card.bot_cards.pop(i)
        self.lp = "bot"

    def player_starts(self):
        while True:
            print("-------------------------------")
            print("What card do you want to put down?")
            which = input().strip().split()

            if len(which) < 2:
                print("Try again")
                continue

            found = False

            for i in range(len(Card.player_cards)):
                card = Card.player_cards[i]

                if str(card.number) == which[0] and card.colour == which[-1].lower():
                    self.current_card = card

                    if card.colour == "special!":
                        print("What colour do you choose?")
                        self.current_colour = input().strip().lower()

                        while self.current_colour not in Card.colours:
                            print("Try again")
                            self.current_colour = input().strip().lower()

                    else:
                        self.current_colour = card.colour

                    print("You put down", self.current_card)

                    Card.player_cards.pop(i)
                    found = True
                    break

            if found:
                break
    
            else:
                print("Try again - note that you cannot pass")


    def play(self):
        
        while True:
            if self.lp == "bot":
                print(f"What card do you want to put down?  (Current Card: {self.current_card}, Current Colour: {self.current_colour})")
                possible_card = input().strip().split()
                print("-------------------------------")

                if possible_card and possible_card[0].lower() == "pass": 
                    self.generate_card("player")
                    print("Your new card is", Card.player_cards[-1])
                    self.lp = "player"
                    break

                if len(possible_card) < 2:
                    print("Try again")
                    print("-------------------------------")
                    continue

                found = False
                for i in range(len(Card.player_cards)):
                    
                    card = Card.player_cards[i]

                    if str(card.number) == possible_card[0] and card.colour == possible_card[1]:

                        if Card.player_cards[i].playable(self.current_card, self.current_colour):
                            
                            if Card.player_cards[i].colour == "special!":
                                print("What colour do you choose?")
                                self.current_colour = str(input()).strip().lower()

                                while self.current_colour not in Card.colours:
                                    print("Try again")
                                    self.current_colour = str(input()).strip().lower()


                                self.current_card = Card.player_cards[i]
                                print("You put down", self.current_card, "and chose", self.current_colour)
                                print("-------------------------------")
                                found = True
                                Card.player_cards.pop(i)
                                self.lp = "player"
                                break

                            print("You have put down", Card.player_cards[i])
                            print("-------------------------------")
                            found = True
                            self.current_card = Card.player_cards[i]
                            self.current_colour = Card.player_cards[i].colour
                            Card.player_cards.pop(i)
                            self.lp = "player"
                            break

                if not found:
                    print("Try again")

                self.show_player_cards()
                
                if not Card.player_cards:
                    break




            elif self.lp == "player":
                possible_choices = []
                
                for i in range(len(Card.bot_cards)):
                    Card.bot_cards[i].playable(self.current_card, self.current_colour)

                    if Card.bot_cards[i].playable(self.current_card, self.current_colour):
                        possible_choices.append(i)


                if len(possible_choices) == 0:
                    print("-------------------------------")
                    print("The bot passed and gained a card")
                    print("-------------------------------")  
                    self.generate_card("bot")	 
                    self.lp = "bot"
                    break
        
                choice = random.choice(possible_choices)

                if Card.bot_cards[choice].colour == "special!":
                    self.current_colour = random.choice(Card.colours)
                    self.current_card = Card.bot_cards[choice]
                    print("-------------------------------")
                    print("The bot puts down", self.current_card, "and chooses", self.current_colour)
                    print("-------------------------------")  
                    Card.bot_cards.pop(choice)
                    self.lp = "bot"
                    break

                print("-------------------------------")  
                print("The bot puts down", Card.bot_cards[choice])
                print("-------------------------------")  
                self.current_card = Card.bot_cards[choice]
                self.current_colour = Card.bot_cards[choice].colour
                Card.bot_cards.pop(choice)
                self.lp = "bot"
                break



game = Game()


#that's me!
game.typeout("Hello, this is UNO made by dario!")
print("-------------------------------")

#generate cards
for loop in range(7):
    game.generate_card("player")

for loop in range(7):
    game.generate_card("bot")


#display cards
game.show_player_cards()

#chooses who starts
starting = ["player", "bot"]
starts = random.choice(starting)
game.typeout(f"the {starts} is starting!")


#uses correct function depending
if starts == "bot":
    game.bot_starts()
    game.lp = "bot"

else:
    game.player_starts()
    game.lp = "player"



while len(Card.player_cards) != 0 and len(Card.bot_cards) != 0:
    game.play()

if len(Card.player_cards) == 0:
    print("-------------------------------")
    print("You win!")
else:
    print("-------------------------------")
    print("The bot wins!")

    
