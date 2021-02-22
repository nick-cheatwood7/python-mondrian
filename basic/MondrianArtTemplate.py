#Created by Ben Stephenson (ben.stephenson@ucalgary.ca)
#
#  Draw random "art" in a Mondrian style
#
import tkinter as tk
import random

WIDTH = 1024
HEIGHT = 768

SPLIT_LOW = 120
SPLIT_PENALTY = 1.5

#
# TODO: 
# Select a color randomly
#
def randomColor():


#
# TODO:
# Split the region both vertically and horizontally
# Invoke mondrian on all four quadrants
#
def split_both(x, y, w, h, canvas):

#
# TODO:
# Split so that the regions are side by side
# Invoke mondrian on both halves
#
def split_horizontal(x, y, w, h, canvas):

#
# TODO:
# Split so that one region is above the other
# Invoke mondrian on both halves
#
def split_vertical(x, y, w, h, canvas):

#
# TODO: 
# Use recursion to draw "art" in a Mondrian style
# This is the algorithm in the project description
#
def mondrian(x, y, w, h, canvas):

#
# Main method - driver of the program
#
def main():
  # Create a window with a canvas
  master = tk.Tk()
  canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
  canvas.pack()

  # Draw the art
  mondrian(0, 0, WIDTH, HEIGHT, canvas)
  tk.mainloop()

main()
