
# Created 2021-02-09 by Nick Cheatwood
# Using functional programming, creates Mondrian art

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
    # Convert integer to decimal form
    randVal = (random.randint(0, 100) / 100)
    if (randVal < 0.0833):
        return 'red'
    elif (randVal < 0.1667):
        return 'skyblue'
    elif (randVal < 0.25):
        return 'yellow'
    else:
        return 'white'

# Split horizontal: top and bottom
def splitRegionHorizontal(x, y, width, height, canvas):
    print('Splitting horizontal...')
    # Choose split point randomly (range end stops before end value) need as decimal, so divide by 100
    horizSplitPoint = (random.randrange(33, 68) / 100)
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
    vertSplitPoint = (random.randrange(33, 68) / 100)
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
    horizSplitPoint = (random.randrange(33, 68) / 100)
    vertSplitPoint = (random.randrange(33, 68) / 100)

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
            canvas.create_rectangle(x, y, (width + x), (height + y), fill=randomColor, outline='black', width=2)

# Define our 'main' function
def main():
    # Create window with a canvas
    master = tk.Tk()
    canvas = tk.Canvas(master, width=canvasWidth, height=canvasHeight)
    canvas.pack()

    # Draw the art
    drawMondrianArt(0, 0, canvasWidth, canvasHeight, canvas)
    tk.mainloop()


# Code to Execute
main()

