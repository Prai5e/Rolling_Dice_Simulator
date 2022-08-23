import tkinter as tk
from PIL import Image
from random import choice
from PIL.ImageTk import PhotoImage


dice = [r'dice_1.png', r'dice_2.png', r'dice_3.png', r'dice_4.png', r'dice_5.png', r'dice_6.png']

def roll_dice():
    _img = PhotoImage(Image.open(choice(dice)))
    # update image
    _label.configure(image = _img)
    # keep a reference
    _label.image = _img
    


root = tk.Tk()
root.geometry('400x400')
root.title("Basic-Roll the Dice")

_img = PhotoImage(Image.open(choice(dice)))
_label = tk.Label(root, image=_img)

_label.image = _img
_label.pack(expand=True)


# Adding a button to the main window
button = tk.Button(root, text="_Do Magic_", fg="indigo", command=roll_dice)

button.pack(expand=True)

# Show window
root.mainloop()
