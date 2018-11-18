import random
import re

PlayerName = input("Please Enter Your Name")
PlayerName2 = input("Please Confirm Your Name")

if PlayerName == PlayerName2:
    print("Welcome To The Guessing Game", PlayerName2)
else:
    print("Please Re-Enter Your Name")
    PlayerName = input("Please Enter Your Name")
    PlayerName2 = input("Please Confirm Your Name")

score = 0

remove_lower = lambda text: re.sub('[a-z]', '_', text)

filename = "songs.txt"
line_number = random.randint(1, 10)
with open(filename, 'r') as filehandle:
    current_line = 1
    for line in filehandle:
        if current_line == line_number:
            fields = line.split(",")
            songtitle1 = fields[0]
            songtitle = remove_lower(songtitle1)
            artist = fields[1]
            upper = songtitle
            question = upper + " by" + artist
            print(question), (question).__len__()

            answer = input("Please Guess the Song Title")
            if answer == songtitle1:
                score = score + 3
                print(PlayerName2, "Your Score is", score)
            else:
                print("Please Guess Again")
                print(question)
                answer1 = input("Please Guess the Song Title")
                if answer1 == upper:
                    score = score + 1
                else:
                    print("Wrong Answer")
                    print(PlayerName2, "Your Score is", score)
        current_line += 1
