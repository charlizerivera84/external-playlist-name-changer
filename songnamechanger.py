import random
import re

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
            uppercase = songtitle
            new_song_title = uppercase + " by" + artist
            print(new_song_title)
        current_line += 1
