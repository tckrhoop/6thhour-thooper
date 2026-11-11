#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
players = int(input("# of players: "))
ratings = []
for number in range(players):
    rating = int(input("Enter a rating 1-5"))
    while rating >5 or rating < 1:
        print("Your rating has to be 1-5 ")
        break
    else: ratings.append(rating)
avrg = sum(ratings)/len(ratings)
print("The average rating is: ", avrg)