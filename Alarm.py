import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time, winsound

#Create Widgets
def createWidgets(): #directly called function

    label1 = Label(root, text="Enter the time in hh:mm - ")#label
    label1.grid(row=0, column=0, padx=5, pady=5)#grid

    global entry1 #global since we have to use in other functions
    entry1 = Entry(root, width=15)
    entry1.grid(row=0, column=1)

    label2 = Label(root, text="Enter the message of Alarm: ")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2
    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1)

    but = Button(root, text="Submit", width=10, command=submit) #command is like onclick function
    but.grid(row=2, column=1)

    global label3
    label3 = Label(root, text="")
    label3.grid(row=3, column=0)

def message1(): #message to be displayed

    global entry1, label3
    Alarmtimelabel = entry1.get() #entry value got
    label3.config(text="The Alarm is Counting...") #config to change values

    #messagebox is like Alert with whatever message!
    messagebox.showinfo("Alarm Clock", f"The Alarm time is: {Alarmtimelabel}")

def submit():
    global entry1, entry2, label3
    Alarmtime = entry1.get()
    message1()
    currenttime = time.strftime("%H:%M") #current time to check if time we entered is equal to the system time
    alarmmessage = entry2.get()
    print(f"The Alarm time is: {Alarmtime}") #printed in console or terminal
    while Alarmtime != currenttime:
        currenttime = time.strftime("%H:%M") #if not equal, get new instant time
        time.sleep(1) #everysecond get currenttime
    if Alarmtime == currenttime:
        print("Playing Alarm Sound..")
        winsound.PlaySound("*", winsound.SND_ASYNC)
        label3.config(text="Alarm Sound Playing!")
        messagebox.showinfo("Alarm Message", f"The Message is: {alarmmessage}")


root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x150")

createWidgets()

root.mainloop()