import tkinter as tk
import subprocess
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

def button1_clicked():
    subprocess.call(["python", "image_face_recognition.py"])

def button2_clicked():
    subprocess.call(["python", "realtime_face_detection.py"])

def button3_clicked():
    subprocess.call(["python", "ageGenderdetection.py"])

# Create the main window
win = Tk()
win.geometry("600x500")
bg = ImageTk.PhotoImage(file="images/ai3.jpg")
win.title('FACE RECOGNITION')
frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("images/ai3.jpg"))


label = Label(frame, image = img)
label.pack()

#adding logo to tkinter window
path = "images/logo.jpg"
load = Image.open(path)
render = ImageTk.PhotoImage(load)
win.iconphoto(False, render)

# Create the labels
label1 = tk.Label(win, text="Recognize Face through photos", fg="#ffffff", bg="#0a68ab", font=("Arial", 16))
label1.pack(pady=20)

button1 = tk.Button(win, text="Click Me", command=button1_clicked, bg="#87CEEB", fg="#ffffff", font=("Arial", 14))
button1.pack(pady=20)

label2 = tk.Label(win, text="Detect Face through Camera", fg="#ffffff", bg="#0a68ab", font=("Arial", 16))
label2.pack(pady=20)

button2 = tk.Button(win, text="Click Me", command=button2_clicked, bg="#87CEEB", fg="#ffffff", font=("Arial", 14))
button2.pack(pady=20)

label3 = tk.Label(win, text="Detect Age and Gender", fg="#ffffff", bg="#0a68ab", font=("Arial", 16))
label3.pack(pady=20)

button3 = tk.Button(win, text="Click Me", command=button3_clicked, bg="#87CEEB", fg="#ffffff", font=("Arial", 14))
button3.pack(pady=20)

win.mainloop()
