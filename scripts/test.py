from customtkinter import *
from PIL import Image

str_stat = 8

def decrement_value(str_stat):
    if str_stat > 8:
        str_stat -= 1

def increment_value(str_stat):
    if str_stat < 16:
        str_stat += 1

root = CTk()
root.title("Character Creation")
root.geometry("1280x720")

test_img = CTkImage(Image.open("images/man.jpg"), size=(32, 32))

stats_frame = CTkFrame(root)
stats_frame.pack()

CTkLabel(stats_frame, text="  Strength  ", image=test_img, compound=LEFT, font=("Arial", 32)).pack(side=LEFT, padx=15)
CTkButton(stats_frame, text=" - ", font=("Arial", 32), width=32, command=decrement_value(str_stat)).pack(side=LEFT)
CTkLabel(stats_frame, text=str(str_stat), font=("Arial", 32)).pack(side=LEFT, padx=15)
CTkButton(stats_frame, text=" + ", font=("Arial", 32), width=32, command=increment_value(str_stat)).pack(side=LEFT)

root.mainloop()