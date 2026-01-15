import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

#Define the main window
root=tk.Tk()
root.title("Your AI Assisstant")

#Adding background colour
root.configure(bg='steelblue')

#Define the Function automate youtube
def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

#Define the Function automate google
def search_google():
    query=entry.get()
    url=f"https://www.google.com/results?search_query={query}"
    webbrowser.open(url)

#Define the Function automate youtube
def search_instagram():
    Username=entry.get().replace('@',"")#ensure username is clean of '@'
    url=f"www.instagram.com/{Username}/"
    webbrowser.open(url)

#create input feild,labels and buttons
Label(root, text="Enter your command: ").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)
Button(root, text="Search on YouTube",command=search_youtube).pack(pady=5)
Button(root, text="Search on Google",command=search_google).pack(pady=5)
Button(root, text="Search on Instagram",command=search_instagram).pack(pady=5)

#Run the GUI event loop
root.mainloop()