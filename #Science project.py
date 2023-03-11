## intro
print("Sir issac newton had brain damage after an apple fell on his head and he needs help remembering his laws")
print("His friends will help him try to remember are you ready? (1 = 1st law 2 = 2nd law 3 = 3rd law")
##the laws/rules^^
laws = [1, 2, 3]
##questions
path = input("Would you like to stay in the house or go somewhere with him (house or outside)")
##first path
if path.lower().strip() == "house":
    print("House it is..")
    y = int(input("Sir Issac newton has a bible on his desk and is wondering why it isnt moving at all. What is he starting to remember."))
    if y == 1:
        print("Nice job, He is trying to remember something over by his pendulum clock...")
    elif y != 1:
        print("Nope sorry, but he needs help the next room over")
    y = int(input("He is looking at his pendulum clock and is thinking 'why is my clock going back after going foward?'"))
    print(y)
    if y == 3:
        print("He thanks you for helping him a bit. In the next room over, He decides to play a game of darts...")
    if y != 3:
        print("He says 'I dont think thats right.' You feel as thought if you get the next law wrong its all over.")
    y = int(input("As you go over into the room, he seems to be throwing the darts at different speeds and with differnt parts of his hand, writing down the results, he seems to be trying to remember a law. Which one is he thinking about?"))
    if y == 2:
        print("He starts to remember everything. His laws his memories and goes on to write about them and discover gravity again.")
    if y != 2:
        print("You feel the earth start to shake beneath you as things start being thrown around floating and the earth starts crumbling in itself and everybody on earth eventually dies to the vacuum of space ")    
else:
##second path
    x = int(input("He had a car sitting in his yard that doesnt move. What law does he start to remember?"))
print(x)
if x == 1:  
    print("Correct, now he needs help over on the road!")
## if its incorrect
elif x != 1 :
    print("Sorry, maybe you'll get it next time.") 

##question 2
x = int(input("He is going to a basketball court via a car, (yes a car dont question it) and is starting to remember a law. what law is the car representing? (air resistance and force the car is producing)"))
print(x)
if x == 3:
    print("Good job! But he needs help over at the court...")
elif x != 3:
    ##wrong 2
    print("sorry that isnt right, I know you can help him remember.")
##question 3
x = int(input("Over in the basketball courtyard, he finds his friends shooting hoops. He goes over and asks if he can shoot a couple of shots and finds that if he puts less of 'His back into it.' the ball doesnt go as far. Likewise, if he doesnt throw it fast enough it doesnt go as far. What law is this representing?"))
print(x)
if x == 2:
    print("Good job, you helped him remember all of his laws and he got his memories back. He can now go back to the apple tree he was sitting under and have this happen all over again")
elif x != 3:
    ##wrong 3
    print("You weren't correct. Now, Sir Issac Newton cant remember his laws and gravity was never discovered")
    print("This 'Game' Was made by levi ley in python it was a science project for Dr.O")
