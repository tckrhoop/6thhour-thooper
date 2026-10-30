#Name: Tucker Hooper
#Hour: 6th

import random

Wallet=500
print(Wallet)
Playing = int(input("How much would you like to play?: "))
new_wallet=Wallet-Playing
print(new_wallet,"dollars left")
first_card=random.randint(2,11)
second_card=random.randint(2,11)
if first_card > 10:
    print("Ace")
else:
    print(first_card)
if second_card > 10:
    print("ace")
else:
    print(second_card)
h_s=(input("hit or stand:"))
if h_s == "hit":
    third_card=(random.randint(2,11))
    if third_card > 10:
        print("Ace")
    else:
        print(third_card)
    dealer_hand = (random.randint(4, 27))
    print(dealer_hand,"Dealer hand")
elif h_s == "stand":
   dealer_hand=(random.randint(4,27))
   print(dealer_hand,"Dealer hand")
if h_s == "hit":
    hand=first_card + second_card + third_card
else:
    hand=first_card + second_card
print(hand, "player hand")
if hand > dealer_hand:
    if hand <= 21:
        print("You win")
        winnings=Playing*2
        winnings+Wallet
        print(Wallet)
    if hand > 21:
        print("Bust")
elif hand < dealer_hand:
    if dealer_hand > 21:
        print("Dealer Bust")
        print("You win")
        winnings = Playing * 2
        winnings + Wallet
        print(Wallet)


