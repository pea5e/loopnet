import tkinter as Tk
from tkinter import ttk
from requests import get
from json import loads
from webbrowser import open_new_tab as open_url


screen = Tk.Tk()
screen.geometry("600x200")

req = list()
get("https://loopnet.salimalaoui.repl.co/available?json=on")
rep = get("https://loopnet.salimalaoui.repl.co/available.json").content.decode()

json = loads(rep)
# print(json)
req=[]
i=0

def add(url):
    global i
    i+=1
    if url!=None:
        req.append(url)
    clear()
    screen.quit()
def clear():
    for c in screen.slaves():
        c.destroy()

def stop():
    global run
    run = False
    clear()
    screen.quit()

    

run=True
while run:
    art = json[i]
    num = 0 
    article = Tk.Frame(screen)
    infomations = ttk.Frame(article)
    title = ttk.Label(infomations,text=art["name"]+" "+art["city"])
    subtitle = ttk.Label(infomations,text=art["groupname"]+"-"+art["owner"])
    title.grid(row=0,column=0)
    subtitle.grid(row=1,column=0)
    ttk.Button(infomations,text="open",command=lambda:open_url(art["url"])).grid(row=0,column=2)
    if art["sentforowner"]>0:
        requestfor = ttk.Label(infomations,text="0 sent for this before",foreground="red")
        requestfor.grid(row=1,column=1)  
    oldi = i
    ttk.Button(infomations,text="Request",command=lambda:add(art["url"]) ).grid(row=2,column=1)
    ttk.Button(infomations,text="cancel",command=lambda:add(None) ).grid(row=2,column=0)
    infomations.pack( side='left',pady=(50,0))
    article.pack()
    ttk.Button(screen,text="Save and Quit",command=stop).pack(pady=(40,0))
    screen.mainloop()
