
# Created 02/21/2021 by Nick Cheatwood
#  Creates a view class with x,y coordinates, width, height, and a canvas

import tkinter as tk

class View:

    def __init__(self, x, y, width, height):
        # Initialize a new View with appropriate attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Create window with a canvas
        self.master = tk.Tk()
        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack()

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getCanvas(self):
        return self._canvas

    def createRectangle(self, width, height, borderWidth, borderColor, fillColor):
        self.canvas.create_rectangle(self.x, self.y, width, height, fill=fillColor,
                                     outline=borderColor, width=borderWidth)

    def render(self):
        # Render Tkinter
        self.master.mainloop()
