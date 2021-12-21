from tkinter import *
from PIL import Image, ImageTk

root = Tk()
user_image = ImageTk.PhotoImage(Image.open('images/team.jpg'))
login_image = ImageTk.PhotoImage(Image.open('images/login.jpg'))
label1 = Label(root, text="Doctor Image", image=user_image, compound=RIGHT, font=('Comic Sans ms', 15, 'bold'))
label1.grid(row=1, column=0, columnspan=2)
login = Button(root, image=login_image)
login.grid(row=2, column=0, columnspan=2)
# root.geometry("800x500+100+100")
root.mainloop()
