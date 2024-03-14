import tkinter as Tk
from tkinter import ttk
from requests import get
from json import loads
from webbrowser import open_new_tab as open_url

screen = Tk.Tk()
canvas = Tk.Canvas(screen)
scroll_y = Tk.Scrollbar(screen, orient="vertical", command=canvas.yview)
screen.geometry("600x400")

frame = Tk.Frame(canvas)
req = list()
get("https://loopnet.salimalaoui.repl.co/available?json=on")
rep = get("https://loopnet.salimalaoui.repl.co/available.json").content.decode()

json = loads(rep)
# print(json)
req=[]

for i,art in enumerate(json):
    req.append(0)
    article = Tk.Frame(frame)
    infomations = ttk.Frame(article)
    title = ttk.Label(infomations,text=art["name"]+" "+art["city"])
    subtitle = ttk.Label(infomations,text=art["groupname"]+"-"+art["owner"])
    # print(req[i])
    title.grid(row=0,column=0)
    subtitle.grid(row=1,column=0)
    ttk.Button(infomations,text="open",command=lambda:open_url(art["url"])).grid(row=0,column=1)
    if art["sentforowner"]>0:
        requestfor = ttk.Label(infomations,text="0 sent for this before",foreground="red")
        requestfor.grid(row=1,column=1)
    
    c1 = ttk.Checkbutton(article, text='Request',variable=req[i], onvalue=1, offvalue=0)
    infomations.pack( side='left')
    c1.pack(side="right")
    article.pack()



canvas.create_window(0, 0, anchor='nw', window=frame)

canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand=scroll_y.set)
                 
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

screen.mainloop()