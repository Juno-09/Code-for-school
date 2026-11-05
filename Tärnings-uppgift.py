import random

score = 0
x = "y"

print("     Get to 21!")

while score < 21 and x == "y":
    x = str(input("Roll the dice! (n/y)     "))
    if x == "y":
        roll = random.randint(1,6)
        score = roll + score
        print("You rolled", roll, "and your score is", score)
    elif x == "n":
        print("damn ok. you were", 21 - score, "off.")

if score == 21:
    wm = random.randint(1,4)
    if wm == 1:
        print("Yay!! Yippie!!!")
    elif wm == 2:
        print("Took some skill!")
    elif wm == 3:
        print("A new winning streak??")
    else:
        print("You should go to a real casino!")

if score > 21:
    lm = random.randint(1,4)
    if lm == 1:
        print("Oops you fucky wuckied.")
    elif lm == 2:
        print("You can definetly do better.")
    elif lm == 3:
        print("Balatro more your style?")
    else:
        print("Unlucky, go again.")

