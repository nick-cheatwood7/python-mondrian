
from Common import *
import random

class Mondrian:

    def __init__(self, view):
        self.view = view
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

    # Draw Mondrian art
    def draw(self, view):
        print('Drawing mondrian...')

        if (view.width > self.canvasWidth / 2 and view.height > self.canvasHeight / 2):
            # Split region into 4 smaller regions: split both
            self.splitRegionBoth(view)
        elif (view.width > canvasWidth / 2):
            # Split using vertical line
            self.splitRegionVertical(view)
        elif (view.height > canvasHeight / 2):
            # Split using horizontal line
            self.splitRegionHorizontal(view)
        else:
            # Default condition (if x, y = 0,0)
            # Splits randomly selected
            # Per project file...Each split must be between the minimum region split and either the minimum region split + 1 or the initial canvas dimensions * 1.5 + 1
            vertSplit = random.randrange(splitLow, max(splitLow + 1, round(splitPenalty * view.height) + 1))
            horizSplit = random.randrange(splitLow, max(splitLow + 1, round(splitPenalty * view.width) + 1))

            # Test if each split is smaller than its counterpart
            if (vertSplit < view.height and horizSplit < view.width):
                # Split into 4 smaller regions (both)
                self.splitRegionBoth(view)
            elif (horizSplit < view.width):
                # Split the region into 2 smaller regions with a horizontal line
                self.splitRegionHorizontal(view)
            elif (vertSplit < view.height):
                # Split region into 2 smaller regions with a vertical line
                self.splitRegionVertical(view)
            else:
                # Fill current region with random color
                randomColor = getRandomColor()
                # Using Tkinter, create a filled rectangle using random color
                # NOTE: (x,y) is starting coordinate, (x1,y1) is coordinate just outside the bottom-right corner
                # create_rectangle(x0, y0, x1, y1, option, ...)
                # To get to bottom right corner, determine the region (width, height) provided and add the initial coordinate
                # Determine whether to draw standard or random rectangle
                shouldDrawRandomRectangle = bool(random.randint(0, 2))  # Random boolean: true or false

                if shouldDrawRandomRectangle:
                    # Draw a random rectangle
                    self.drawRandomRectangle(view)
                else:
                    # Randomly determine if border colors should be random or not
                    hasRandomBorderColors = bool(random.randint(0, 2))
                    # Append additional props to view object
                    view.randomizeBorderColor = hasRandomBorderColors
                    view.fillColor = randomColor
                    # Draw a standard rectangle with given attributes
                    self.drawRectangles(view)

    def randomizeSplitPoint(self):
        # Randomize two split points between the range 33% and 67%
        split1 = random.randrange(33, 68) / 100
        split2 = random.randrange(33, 68) / 100

        # evenly distribute split point
        finalSplit = (split1 + split2) / 2
        return finalSplit

    # Split vertical: left and right
    def splitRegionVertical(self, view):
        print('Splitting vertical...')
        # Choose split point randomly (range end stops before end value) need as decimal, so divide by 100
        vertSplitPoint = self.randomizeSplitPoint()
        leftRegion = round(vertSplitPoint * view.height)  # Randomly assigns left region using random split point
        rightRegion = view.height - leftRegion  # Splits into two regions– left and right
        # Draw mondrian at the initial point provided and then draw Mondrian using the regions
        view.width = leftRegion
        self.draw(view)
        # Since the create_rectangle method works inverted (top->bottom, not bottom->top),
        #   add the left region to the initial point and use right region as the width
        view.x = view.x + leftRegion
        view.width = rightRegion
        self.draw(view)

    # Split horizontal: top and bottom
    def splitRegionHorizontal(self, view):
        print('Splitting horizontal...')
        # Choose split point randomly (range end stops before end value) need as decimal, so divide by 100
        horizSplitPoint = self.randomizeSplitPoint()
        topRegion = round(horizSplitPoint * view.width)  # Randomly assigns top region using random split point
        bottomRegion = view.width - topRegion  # Splits into two regions– top and bottom
        # Draw mondrian at the initial point provided and then draw Mondrian using the regions
        view.height = topRegion
        self.draw(view)
        # Since the create_rectangle method works inverted (top->bottom, not bottom->top),
        #   add the top region and bottom region
        view.y = view.y + topRegion
        view.height = bottomRegion
        self.draw(view)

    # Split both regions
    def splitRegionBoth(self, view):
        print('Splitting both...')
        # Combine horizontal region split and vertical region split
        # Choose split point randomly (range end stops before end value) need as decimal, so divide by 100
        horizSplitPoint = self.randomizeSplitPoint()
        vertSplitPoint = self.randomizeSplitPoint()

        leftRegion = round(vertSplitPoint * view.height)  # Randomly assigns top region using random split point
        rightRegion = view.height - leftRegion  # Splits into two regions– left and right

        topRegion = round(horizSplitPoint * view.width)  # Randomly assigns top region using random split point
        bottomRegion = view.width - topRegion  # Splits into two regions– top and bottom

        # Draw mondrian at the initial point provided and then draw Mondrian using the left-right regions and top-bottom
        # Split into four quadrants: ([Q1: x,y], [Q2: x+,y], [Q3: x,y+], [Q4: x+,y+])
        # For each quadrant, make a copy of the view and update attributes accordingly

        # At initial + left and top splits (Q1)
        q1 = view
        q1.width = leftRegion
        q1.height = topRegion
        self.draw(q1)

        # shift by left and set width and height to splits (Q2)
        q2 = view
        q2.x = q2.x + leftRegion
        q2.width = rightRegion
        q2.height = topRegion
        self.draw(q2)

        # shift by top and use left and bottom splits (Q3)
        q3 = view
        q3.y = q3.y + topRegion
        q3.width = leftRegion
        q3.height = bottomRegion
        self.draw(q3)

        # use all second splits (Q4)
        q4 = view
        q4.x = q4.x + leftRegion
        q4.y = q4.y + topRegion
        q4.width = rightRegion
        q4.height = bottomRegion
        self.draw(q4)

    def drawRectangles(self, view):
        print('Drawing rectangle...')
        # Choose a random border size between 1 and 7
        borderWidth = random.randint(1, 8)
        if view.randomizeBorderColor:
            # If algorithm wants to randomize, get random color
            borderColor = getRandomBorderColor()
        else:
            # Default to black border
            borderColor = 'black'
        view.createRectangle(
                width=(view.width + view.x),
                height=(view.height + view.y),
                borderWidth=borderWidth,
                borderColor=borderColor,
                fillColor=view.fillColor
        )

    def drawRandomRectangle(self, view):
        print('Drawing random rectangle...')
        # Randomize width and height
        view.createRectangle(
            width=(view.width + view.x / random.randint(1, 10)),
            height=(view.height + view.y / random.randint(1, 10)),
            borderWidth=2,
            borderColor='black',
            fillColor=getRandomColor()
        )