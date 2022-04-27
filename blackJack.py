import random
points = 100
playing = True
# initialize card names and values
cardNames = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
cardValues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("Welcome to the Black Jack table! You have {points} points.".format(points = points))
while points > 0 and playing == True:
    bet = int(input("How much would you like to bet: "))
    print("")
    # make sure the user is only inputing y or n
    while isinstance(bet, int) == False or bet > points:
        if isinstance(bet, int) == False:
            bet = int(input("Please type an integer for your bet: "))
            print("")
        if bet > points:
            bet = int(input("Sorry, you only have {points} points, you can not bet more than that. Please insert bet: ".format(points = points)))
            print("")
    # create the list of available cards, then quadruple it to account for all 4 suits
    # the numbers 1 through 13 in these represent ace through king, and are used to reference back to the cardName and cardValue lists created in the beginning
    availCards = list(range(1,14))
    availCards = availCards + availCards + availCards + availCards
    playerCards = []
    houseCards = []
    # give the player and the house two cards, and tell the player what their cards are and what 1 of the houses cards are
    playerCards.append(availCards.pop(random.randint(1,len(availCards))-1))
    houseCards.append(availCards.pop(random.randint(1,len(availCards))-1))
    playerCards.append(availCards.pop(random.randint(1,len(availCards))-1))
    houseCards.append(availCards.pop(random.randint(1,len(availCards))-1))
    print("You have a {card1} and a {card2}.".format(card1 = cardNames[playerCards[0]-1], card2 = cardNames[playerCards[1]-1]))
    print("The house has a {card3} showing.".format(card3 = cardNames[houseCards[1]-1]))
    playerTotal = cardValues[playerCards[0]-1] + cardValues[playerCards[1]-1]
    houseTotal = cardValues[houseCards[0]-1] + cardValues[houseCards[1]-1]
    hitting = True
    # loop will run until player stops hitting or busts
    while playerTotal <= 21 and hitting == True:
        hit = input("Hit? Y or N: ").lower()
        print("")
        while hit not in ["y", "n"]:
            hit = input("Sorry, could not understand. Hit? Y or N: ").lower()
            print("")
        if hit == "y":
            # give the player another cards, add it to their total, and tell them what they got
            playerCards.append(availCards.pop(random.randint(1,len(availCards))-1))
            playerTotal += cardValues[playerCards[-1]-1]
            if playerTotal > 21 and 1 in playerCards:
                # aces are counted as 11 by default. if the player busts but has an ace, 10 is taken from their total, essentially making the ace worth 1 instead
                # the ace is then changed to a "50" in their hand, so this subtraction of 10 can't happen again for the same card
                playerTotal = playerTotal - 10
                playerCards[playerCards.index(1)] = 50
            print("You got a {newCard}. You now have a total of {total}.".format(newCard = cardNames[playerCards[-1]-1], total = playerTotal))
        if hit == "n":
            hitting = False
    # reveal the house's other card, then hit till it goes over 16
    print("The house's flipped card is a {card}, for a total of {total}.".format(card = cardNames[houseCards[0]-1], total = houseTotal))
    while houseTotal < 16:
        houseCards.append(availCards.pop(random.randint(1,len(availCards))-1))
        houseTotal += cardValues[houseCards[-1]-1]
        if houseTotal > 21 and 1 in houseCards:
            # similar to the player, if the house busts but has an ace, its value is changed from 11 to 1
            houseTotal = houseTotal - 10
            houseCards[houseCards.index(1)] = 50
        print("The house hit and got a {card}, for a total of {total}.".format(card = cardNames[houseCards[-1]-1], total = houseTotal))
    # busts are changed to 0s so for ease of score comparison
    if houseTotal > 21:
        houseTotal = 0
    if playerTotal > 21:
        playerTotal = 0
    if playerTotal > houseTotal:
        points = points + bet
        print("Congratulations, you won this hand! You now have {points} points.\n".format(points = points))
    if houseTotal >= playerTotal:
        points = points - bet
        print('Sorry, you lost this hand. You now have {points} points.\n'.format(points = points))
    if points <= 0:
        print('Sorry, you are out of points. Thanks for playing!')
    # player will get the opportunity to leave with their points, or keep playing
    else:
        play = input("Would you like to keep playing? Y or N: ").lower()
        print("")
        while play not in ["y", "n"]:
            play = input("Sorry, could not understand. Would you like to keep playing? Y or N: ").lower()
            print("")
        if play == "n":
            playing = False
if points > 0:
    print("Thanks for playing! You left the table with {points} points!".format(points = points))