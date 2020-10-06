import tkinter
from PIL import Image, ImageTk
import random

# toplevel widget of Tk which represents mostly the main window of an application
root = tkinter.Tk()
root.geometry('200x175')
root.title('6 Sided Die')

# image
# make sure image is in path or specify specific path
dice = ['dice_1.PNG', 'dice_2.PNG', 'dice_3.PNG', 'dice_4.PNG', 'dice_5.PNG', 'dice_6.PNG']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for the image
label1 = tkinter.Label(root, image=image1)

# keep a reference, if needed
label1.image = image1

# pack a widget in the parent widget with placement
label1.pack()
# label2.pack(side=tkinter.RIGHT)

# function activated by button
def roll_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1


# button
# command will use roll_dice function
button = tkinter.Button(root, text='roll dice', foreground='green', command=roll_dice)

# pack a widget in the parent widget
button.pack()

# call the mainloop of Tk
# keeps window open
root.mainloop()