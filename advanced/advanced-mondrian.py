
# Created 2021-02-21 by Nick Cheatwood
# Using functional programming, creates Mondrian art

# MARK: Things to try
'''
[x] Use lines of variable width
[x] Use a broad color pallet for filled regions
[] Change the distribution of random numbers used when selecting size of regions
    [x] add two random numbers together and divide by two to favor numbers in middle of random space
[x] Occasionally split a region into 3 smaller regions instead of 2 or 4
'''

# Import Packages
import tkinter as tk
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

    colorChoices = [ 'white',
                     '#6E5AE0',
                     '#E09287',
                     '#8170E0',
                     '#E0CF5A',
                     '#65E0A7'
                     ]

    randColorVal = random.randint(0, len(colorChoices) + 1)  # Pick a random value between 0 and the length of the color choices array

    if(randColorVal >= len(colorChoices)):
        # randColorVal depends on a range, so end range is length of array + 1 to get proper range
        randIndex = randColorVal - 2 # out of index, bring down 2 to get to proper end array index
    else:
        randIndex = randColorVal

    return colorChoices[randIndex] # return a random color

def getRandomBorderColor():
    colors = [
        'black',
        'white',
        'hot pink',
        'grey',
        'blue'
    ]
    randVal = random.randint(0, len(colors) + 1) # range, so add 1 to length of colors array
    randIndex = randVal - 2 if randVal >= len(colors) else randVal # make sure randomized index is in range
    return colors[randIndex]

def drawRectangles(x, y, width, height, canvas, fillColor, randomizeBorderColor=0):
    borderWidth = random.randint(1, 8)
    if randomizeBorderColor:
        # If user wants to randomize, get random color
        borderColor = getRandomBorderColor()
    else:
        borderColor = 'black'
    canvas.create_rectangle(x, y, (width + x), (height + y), fill=fillColor, outline=borderColor, width=borderWidth)

def drawRandomRectangle(view):
    print('Drawing random rectangle')
    # Specify params
    x = view['x']
    y = view['y']
    canvas = view['canvas']
    width = view['width'] + x / random.randint(1, 10)
    height = view['height'] + y / random.randint(1, 10)
    canvas.create_rectangle(x, y, width, height, fill=getRandomColor(), outline='black', width=2)

def randomizeSplitPoint():
    # Randomize two split points between the range 33% and 67%
    split1 = random.randrange(33, 68) /100
    split2 = random.randrange(33, 68) /100

    finalSplit = ( split1 + split2 ) / 2 # evenly distribute split point
    return finalSplit

# Split horizontal: top and bottom
def splitRegionHorizontal(x, y, width, height, canvas):
    print('Splitting horizontal...')
    # Choose split point randomly (range end stops before end value) need as decimal, so divide by 100
    horizSplitPoint = randomizeSplitPoint()
    topRegion = round(horizSplitPoint * width)  # Randomly assigns top region using random split point
    bottomRegion = width - topRegion  # Splits into two regions– top and bottom
    # Draw mondrian at the initial point provided and then draw Mondrian using the regions
    drawMondrianArt(x, y, width, topRegion, canvas)
    # Since the create_rectangle method works inverted (top->bottom, not bottom->top),
    #   add the top region and bottom region
    drawMondrianArt(x, y + topRegion, width, bottomRegion, canvas)

# Split vertical: left and right
def splitRegionVertical(x, y, width, height, canvas):
    print('Splitting vertical...')
    # Choose split point randomly (range end stops before end value) need as decimal, so divide by 100
    vertSplitPoint = randomizeSplitPoint()
    leftRegion = round(vertSplitPoint * height) # Randomly assigns left region using random split point
    rightRegion = height - leftRegion # Splits into two regions– left and right
    # Draw mondrian at the initial point provided and then draw Mondrian using the regions
    drawMondrianArt(x, y, leftRegion, height, canvas)
    # Since the create_rectangle method works inverted (top->bottom, not bottom->top),
    #   add the left region to the initial point and use right region as the width
    drawMondrianArt(x + leftRegion, y, rightRegion, height, canvas)

# Split both regions
def splitRegionBoth(x, y, width, height, canvas):
    print('Splitting both...')
    # Combine horizontal region split and vertical region split
    # Choose split point randomly (range end stops before end value) need as decimal, so divide by 100
    horizSplitPoint = randomizeSplitPoint()
    vertSplitPoint = randomizeSplitPoint()

    leftRegion = round(vertSplitPoint * height)  # Randomly assigns top region using random split point
    rightRegion = height - leftRegion  # Splits into two regions– left and right

    topRegion = round(horizSplitPoint * width) # Randomly assigns top region using random split point
    bottomRegion = width - topRegion # Splits into two regions– top and bottom

    # Draw mondrian at the initial point provided and then draw Mondrian using the left-right regions and top-bottom
    # Split into four quadrants: ([Q1: x,y], [Q2: x+,y], [Q3: x,y+], [Q4: x+,y+])
    drawMondrianArt(x, y, leftRegion, topRegion, canvas) # At initial + left and top splits (Q1)
    drawMondrianArt(x + leftRegion, y, rightRegion, topRegion, canvas) # shift by left and set width and height to splits (Q2)
    drawMondrianArt(x, y + topRegion, leftRegion, bottomRegion, canvas) # shift by top and use left and bottom splits (Q3)
    drawMondrianArt(x + leftRegion, y + topRegion, rightRegion, bottomRegion, canvas) # use all second splits (Q4)

# Draw Mondrian art
def drawMondrianArt(x, y, width, height, canvas):
    print('Drawing mondrian...')

    # Map current view params into object
    view = {
        'x': x,
        'y': y,
        'width': width,
        'height': height,
        'canvas': canvas
    }

    if (width > canvasWidth / 2 and height > canvasHeight / 2):
        # Split region into 4 smaller regions– split both
        splitRegionBoth(x, y, width, height, canvas)
    elif (width > canvasWidth / 2):
        # Split using vertical line
        splitRegionVertical(x, y, width, height, canvas)
        # splitRegionHorizontal(x, y, width, height, canvas)
    elif (height > canvasHeight / 2):
        # Split using horizontal line
        splitRegionHorizontal(x, y, width, height, canvas)
        # splitRegionVertical(x, y, width, height, canvas)
    else:
        # Default condition (if x, y = 0,0)
        # Splits randomly selected
        # Each split must be between the minimum region split and either the minimum region split + 1 or the initial canvas dimensions * 1.5 + 1
        vertSplit = random.randrange(splitLow, max(splitLow + 1, round(splitPenalty * height) + 1))
        horizSplit = random.randrange(splitLow, max(splitLow + 1, round(splitPenalty * width) + 1))

        # Test if each split is smaller than its counterpart
        if (vertSplit < height and horizSplit < width):
            # Split into 4 smaller regions (both)
            splitRegionBoth(x, y, width, height, canvas)
        elif (horizSplit < width):
            # Split the region into 2 smaller regions with a horizontal line
            splitRegionHorizontal(x, y, width, height, canvas)
        elif (vertSplit < height):
            # Split region into 2 smaller regions with a vertical line
            splitRegionVertical(x, y, width, height, canvas)
        else:
            # Fill current region with random color
            randomColor = getRandomColor()
            # Using Tkinter, create a filled rectangle using random color
            # NOTE: (x,y) is starting coordinate, (x1,y1) is coordinate just outside the bottom-right corner
            # create_rectangle(x0, y0, x1, y1, option, ...)
            # To get to bottom right corner, determine the region (width, height) provided and add the initial coordinate
            # Determine whether to draw standard or random rectangle
            shouldDrawRandomRectangle = bool(random.randint(0,2)) # Random boolean
            if shouldDrawRandomRectangle:
                drawRandomRectangle(view)
            else:
                # Randomly determine if border colors should be random or not
                hasRandomBorderColors = random.randint(0,2)
                drawRectangles(x, y, width, height, canvas, randomColor, hasRandomBorderColors)

# Define our 'main' function
def main():
    # Create window with a canvas
    master = tk.Tk()
    canvas = tk.Canvas(master, width=canvasWidth, height=canvasHeight)
    canvas.pack()

    # Draw the art
    # Initiate a view
    view = {
        'x': 0,
        'y': 0,
        'width': canvasWidth,
        'height': canvasHeight,
        'canvas': canvas
    }

    drawMondrianArt(0, 0, canvasWidth, canvasHeight, canvas)
    tk.mainloop()


# Code to Execute
main()

