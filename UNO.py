import time
import random

colours = ["green", "red", "blue", "yellow"]
rare_cards = ["colour_change"]
normal_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
current_card = None
current_colour = None
possible_card = None
lp = ""


def typeout(text, delay=0.01):
    for l in text:
        print(l, end="", flush=True)
        time.sleep(delay)
    print()



def bot_starts():
    global current_card, current_colour
    which = random.choice(bot_cards)

    for i in range(len(bot_cards)):
        if bot_cards[i] == which and bot_cards[i] not in rare_cards:
            print("-------------------------------")
            print("The bot puts down", bot_cards[i], bot_colours[i])
            current_card = bot_cards[i]
            current_colour = bot_colours[i]
            bot_cards.pop(i)
            bot_colours.pop(i)
            print("-------------------------------")
            break

    

def player_starts():
    global current_card, current_colour
    while True:
        print("-------------------------------")
        print("What card do you want to put down?")
        which = input().strip().split()

        found = False

        for i in range(len(player_cards)):
            if player_cards[i] == which[0] and player_colours[i] == which[-1]:
                print("You have put down", player_cards[i], player_colours[i])
                found = True
                current_card = player_cards[i]
                current_colour = player_colours[i]
                player_cards.pop(i)
                player_colours.pop(i)
                print("-------------------------------")
                break

        if found:
            break
        else:
            print("Try again")
            print("-------------------------------")

    print("Your cards are now", len(player_cards))
    
    for i in range(len(player_cards)):
        print(player_cards[i], player_colours[i])

    


def check(card_val, card_col):  
    global allowed, current_card, current_colour
    
    if card_val == current_card or card_col == current_colour or card_col == "special!":
        allowed = True
    else:
        allowed = False
        
    return allowed






def play(who):
    global current_card, current_colour, lp, player_cards, player_colours, bot_cards, bot_colours
    
    while len(player_cards) != 0 and len(bot_cards) != 0:
        if lp == "bot":
            print("-------------------------------")
            print("What card do you want to put down?")
            possible_card = input().strip().split()
        
            for i in range(len(player_cards)):
                if player_cards[i] == possible_card[0] and player_colours[i] == possible_card[-1]:
                    check(player_cards[i], player_colours[i])

                        
                    if allowed == True:
                        if player_colours[i] == "special":
                            print("What colour do you choose?")
                            current_colour = str(input())

                            while current_colour not in colours:
                                print("Try again")

                            found = True
                            current_colour = player_colours[i]
                            player_cards.pop(i)
                            player_colours.pop(i)
                            lp = "player"
                            break


                        print("You have put down", player_cards[i], player_colours[i])
                        found = True
                        current_card = player_cards[i]
                        current_colour = player_colours[i]
                        player_cards.pop(i)
                        player_colours.pop(i)
                        lp = "player"
                        break

                    else:
                        print("Try again")

            print("-------------------------------")
            print("Your cards are now", len(player_cards))

            for i in range(len(player_cards)):
                print(player_cards[i], player_colours[i])

            print("-------------------------------")




        elif lp == "player":
            possible_choices = []
            
            for i in range(len(bot_cards)):
                check(bot_cards[i], bot_colours[i])

                if allowed == True:
                    possible_choices.append(bot_cards[i])
    
            choice = random.choice(possible_choices)

            for i in range(len(bot_cards)):
                if bot_cards[i] == choice:
                    if bot_colours[i] == "special":
                        current_colour = rando.choice(colours)
                        current_card = bot_cards[i]
                        bot_cards.pop(i)
                        bot_colours.pop(i)
                        lp = "bot"
                        break
                            
                    print("-------------------------------")
                    print("The bot puts down", bot_cards[i], bot_colours[i])
                    current_card = bot_cards[i]
                    current_colour = bot_colours[i]
                    bot_cards.pop(i)
                    bot_colours.pop(i)
                    lp = "bot"
                    break

                else:
                    print("-------------------------------")
                    print("The bot passes")
                    lp = "bot"
                    break 


typeout("Hello, this is UNO made by dario!")
print("-------------------------------")
typeout("Here are your cards!")























# assign cards to player

player_cards = []

for loop in range(7):
    r = random.choice(normal_cards)
    player_cards.append(r)

for i in range(len(player_cards)):
    if player_cards[i] in ("10", "11", "12"):
        player_cards[i] = random.choice(rare_cards)

player_colours = []

for loop in range(7):
    r = random.choice(colours)
    player_colours.append(r)

for i in range(len(player_cards)):
    if player_cards[i] in rare_cards:
        player_colours[i] = "special!"

    print(player_cards[i], player_colours[i])

# assign cards to bot

bot_cards = []

for loop in range(7):
    r = random.choice(normal_cards)
    bot_cards.append(r)

for i in range(len(bot_cards)):
    if bot_cards[i] in ("10", "11", "12"):
        bot_cards[i] = random.choice(rare_cards)

bot_colours = []

for loop in range(7):
    r = random.choice(colours)
    bot_colours.append(r)

for i in range(len(bot_cards)):
    if bot_cards[i] in rare_cards:
        bot_colours[i] = "special!"

# gameplay


starting = ["player", "bot"]
starts = random.choice(starting)
print("-------------------------------")
typeout(f"the {starts} is starting!")

if starts == "bot":
    bot_starts()
    lp = "bot"

else:
    player_starts()
    lp = "player"

play(lp)


