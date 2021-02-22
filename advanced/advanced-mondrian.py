
# Created 2021-02-21 by Nick Cheatwood
# Using functional programming, creates Mondrian art

# MARK: Things to try
'''
[x] Use lines of variable width
[x] Use a broad color pallet for filled regions
[] Change the distribution of random numbers used when selecting size of regions
    [x] add two random numbers together and divide by two to favor numbers in middle of random space
[x] Occasionally split a region into 3 smaller regions instead of 2 or 4
[x] Split functionality into separate files
'''

# Import Packages
from View import *
from Mondrian import Mondrian
from Common import canvasWidth, canvasHeight

# Define our 'main' function
def main():

    # Initialize a new View object
    view = View(x=0, y=0, width=canvasWidth, height=canvasHeight)

    # Initialize new Mondrian object
    md = Mondrian(view)
    md.draw(view)

    # Render the view
    view.render()


# Code to Execute
main()

