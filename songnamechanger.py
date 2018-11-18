import random
import re

PlayerName = input("Please Enter Your Name")
PlayerName2 = input("Please Confirm Your Name")

if PlayerName == PlayerName2:
    print("Welcome To The Song Name Changer", PlayerName2)
else:
    print("Please Re-Enter Your Name")
    PlayerName = input("Please Enter Your Name")
    PlayerName2 = input("Please Confirm Your Name")

score = 0

remove_lower = lambda text: re.sub('[a-z]', '_', text)

filename = "songs.txt"
## change the randint value to however amount of songs you have in the playlist 
## e.g. if you have 20 song change it to random.randint(1, 20)
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
            answer = upper + " by" + artist
            print(answer)
        current_line += 1
