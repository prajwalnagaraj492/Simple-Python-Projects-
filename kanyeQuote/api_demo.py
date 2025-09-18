"""this simple project demonstrates hot we use APIs in python along with a simple Tkinter UI
    basically we display so random quotes from our API(which is refreshed every time we click on button)
"""


import tkinter as tk
import requests

kanye_URL = "https://api.kanye.rest/"
quotetext = ""

def getQuote():
    response = requests.get(kanye_URL)
    global quotetext
    global quote
    data = response.json()
    quote.config(text=data["quote"])




window = tk.Tk()
window.title("kanye quotes")
window.minsize(width=500,height=500)

titlelabel = tk.Label(text="Kanye Quotes",width=30,pady=1,fg="green",font=("times new roman",20,"bold"))
titlelabel.grid(row=0,column=1)

canvas = tk.Canvas(highlightthickness=0,bg="#76852a",width=400,height=400)
canvas.grid(row=1,column=1)
quote = tk.Label(text=quotetext,fg="white",bg="#76852a",font=("calibiri",20,"bold"),width=20,wraplength=300)
quote.place(x=50,y=200)

button = tk.Button(text="Get New Quote",bg="green",fg="white",command=getQuote)
button.grid(row=2,column=1)




window.mainloop()