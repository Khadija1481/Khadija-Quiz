print("Welcome to my quiz!")

print("Who knows me the best....")

playing = input("Would you like to play? ").strip().lower()

if playing == "no":
    print("You're boring!")
    quit()

print("Perfect! Let's Play")
score = 0 
total_questions = 5 

answer = input("What is my favoruite colour? ").lower()
if answer == "blue":
    print("Correct!")
    score += 1 
else:
    print("Not off to a good start ey..")

correct_answers = ["japan","malaysia","spain","italy","turkey"]
answer = input("Name 1 country I want to travel to... ").lower()

if answer in correct_answers:
    print("Correct!")
    score += 1 
else:
    print("You'll get the next one!")

while True:
    answer = input("Who is my favourite pet? ").lower()

    if answer == "link":
        print("He's cute but not my favourite. Try again!")
    elif answer == "minnie":
        print("Close, but not close enough :( Try again!")
    elif answer == "ray":
        print("Correct!!!")
        score += 1
        break # Exit loop once the correct answer is given
    else:
        print("You had 3 options and you chose none??? Wrong.")
        break # Exit the loop for any answer not in the options

answer = input("What am I allergic to? ").lower()
if answer == "fish":
    print("Correct!")
    score += 1 
else:
    print("Dissapointing, wrong!")

answer = input("What month was I born? ").lower()
if answer == "November":
    print("Correct!")
    score += 1 
else:
    print("Incorrect.")

print(" You scored " + str(score) + " questions correct!")
print(" You scored " + str((score / total_questions) * 100) + "%.")
