
# Created 02/22/2021 by Nick Cheatwood
#  Contains any numbers or functions generic enough to warrant being outside of main file

import random

# Specify canvas width/height
canvasWidth = 1024
canvasHeight = 768

# Specify splits
# 'Generate a random integer between 120 and the width of the region * 1.5'
# If the random integer is less than the width of the region then split the region
splitLow = 120 # Ensures that we never split a region less than 120px wide
splitPenalty = 1.5 # Provides a random chance that a larger region will not be split into smaller regions

# Generate a random color
def getRandomColor():

    # Available color choices
    colorChoices = [ 'white',
                     '#6E5AE0',
                     '#E09287',
                     '#8170E0',
                     '#E0CF5A',
                     '#65E0A7'
                     ]

    # Pick a random value between 0 and the length of the color choices array
    randColorVal = random.randint(0, len(colorChoices) + 1)

    if(randColorVal >= len(colorChoices)):
        # randColorVal depends on a range, so end range is length of array + 1 to get proper range
        randIndex = randColorVal - 2 # out of index, bring down 2 to get to proper end array index
    else:
        randIndex = randColorVal

    return colorChoices[randIndex] # return a random color

def getRandomBorderColor():
    # Avaliable color options
    colors = [
        'black',
        'white',
        'hot pink',
        'grey',
        'blue'
    ]
    # range, so add 1 to length of colors array
    randVal = random.randint(0, len(colors) + 1)
    # make sure randomized index is in range
    randIndex = randVal - 2 if randVal >= len(colors) else randVal
    return colors[randIndex]