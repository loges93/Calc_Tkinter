from tkinter import *
from PIL import Image
# This file is used for reference using images for window icon and in general
window = Tk()
window.configure(bg = "#282828")
window.title("A Random Window")
photo = Image.open("cool_image.jpg")
#making and exit button
quit_button = Button(window, text = "Exit", command=window.quit)
quit_button.pack()
label = Label(window, image = photo)
label.pack() 

window.mainloop()
