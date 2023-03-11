## intro
print("Sir issac newton had brain damage after an apple fell on his head and he needs help remembering his laws")
print("His friends will help him try to remember  are you ready? (1 = 1st law 2 = 2nd law 3 = 3rd law")
##the laws/rules^^
laws = [1, 2, 3]
##questions
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
