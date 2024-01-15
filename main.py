from tkinter import *
from PIL import ImageTk
from ech_a_sketch import SketchGame


class Sketch:

    def __init__(self):
        self.root = Tk()
        self.root.title("Etch-A-Sketch")
        self.root.geometry("720x405")
        self.root.resizable(False, False)

        # Background Image
        self.bg_image = ImageTk.PhotoImage(file="image/bg.jpg")
        self.bg_label = Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0)

        self.start_game = Button(self.root, text="Let's Draw", padx=20, bg="orange", command=self.start_drawing)
        self.start_game.place(x=310, y=247)
        self.root.mainloop()

    def start_drawing(self):
        SketchGame()


sketching = Sketch()
