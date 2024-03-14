import sys
import subprocess
try:
    from selenium import webdriver
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
    from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
import os
import tkinter as Tk
from tkinter import ttk
from tkinter.messagebox import askyesno
from webbrowser import open_new_tab as open_url
try:
    from requests import get
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    from requests import get
import json
try:
    import pyperclip as pc
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyperclip'])
    import pyperclip as pc
from datetime import datetime

def isnull(l,ind):
    try :
        return l[ind].text.strip()
    except: 
        return ''

class Loopnet:

    url = "https://www.loopnet.com/"

    def __init__(self,chromium,userdata,viewable = True):
        self.options = Options()
        if not viewable:
            self.options.add_argument('--headless')
        self.options.add_argument('user-data-dir='+userdata)
        self.chromium = chromium
        self.userdata = userdata
        self.openbrowser()
    
    @classmethod
    def openbrowserasuser(mth,chrome,userdata):
        # os.system(r'"{1}"  --user-data-dir="{0}" "https://www.loopnet.com/"'.format(userdata,chrome))
        return r'"{1}"  --user-data-dir="{0}" "https://www.loopnet.com/"'.format(userdata,chrome)

    def openbrowser(self):
        self.browser = webdriver.Chrome(executable_path=self.chromium,options=self.options)
        self.browser.get(self.url)

    def __getloginbutton(self):
        return self.browser.find_element(By.CLASS_NAME,"login").find_element(By.TAG_NAME,'a')

    def login(self):
        while True:
            try:
                self.__getloginbutton().click()
                sleep(1)
                self.browser.find_element(By.CLASS_NAME,"identify-account").click()
            except:
                break
        sleep(5)
        self.loggedin = True
    def advancedsearch(self):
        self.browser.find_element(By.CLASS_NAME,"advanced").click()

    def passlogin(self):
        while  True:
            try:
                self.browser.find_element(By.CLASS_NAME,"save-search-reg-overlay-show")
                break
            except:
                sleep(1)
        self.browser.find_elements(By.CLASS_NAME,"csgp-modal-close")[-1].click()
    
    def forsale(self):
        self.browser.find_element(By.ID,"forSale").click()

    def chooseType(self):
        hospitality = -4
        [ele for ele in self.browser.find_element(By.CLASS_NAME,"input-select-multiple").find_elements(By.TAG_NAME,"input") if ele.location['x']!=0 and ele.location['y']!=0][hospitality].click()
    
    def visitarticle(self,url):
        self.browser.get(url)

    def contact(self,message):
        sleep(3)
        self.browser.find_element(By.CLASS_NAME,"watch-property-trigger").click()
        for time in range(10):
            try:
                self.browser.find_element(By.CLASS_NAME,"ln-icon-close-hollow").click()
                break
            except:
                sleep(0.5)
        self.browser.execute_script("window.scroll(0,500)")
        sleep(1)
        self.browser.find_element(By.CLASS_NAME,"contact-card-action").click()
        self.browser.find_element(By.NAME,"message").clear()
        self.browser.find_element(By.NAME,"message").send_keys(message)
        self.browser.find_element(By.CLASS_NAME,"contact-button").click()

    def filters(self):
        for ele in self.browser.find_elements(By.CLASS_NAME,"column-12")[1].find_elements(By.TAG_NAME,"input"):
            ele.click()
        self.browser.find_elements(By.CLASS_NAME,"column-12")[2].find_element(By.TAG_NAME,"input").click()
        self.browser.find_elements(By.CLASS_NAME,"range-from")[13].find_element(By.TAG_NAME,"input").send_keys("40")
        #save filters
        # input()
        self.browser.find_elements(By.CLASS_NAME,"column-12")[-1].find_elements(By.TAG_NAME,"button")[-1].click()

    def sorting(self,sorttype):
        self.browser.find_element(By.CLASS_NAME,"sort-wrapper").click()
        sort = {"newest":1,"oldest" : 2,"AtoZ":-4}
        self.browser.find_element(By.CLASS_NAME,"sort-wrapper").find_elements(By.CLASS_NAME,"drop-down-menu")[1].find_elements(By.TAG_NAME,"li")[sort[sorttype]].click()
        sleep(5)
        self.generatedurl = self.browser.current_url

    def getTotalPages(self):
        return int(self.browser.find_elements(By.CLASS_NAME,"afterellipsisli")[1].text.strip())
    
    def get_articles(self):
        articles = list()
        for article in self.browser.find_elements(By.TAG_NAME,"article"):
            articles.append(article)
        return articles

    def getpage_articles(self,page):
        self.browser.get(self.generatedurl.replace("for-sale/","for-sale/"+str(page)+"/"))
        articles = self.get_articles()
        return articles

    def getarticle_href(self,art):
        return art.find_element(By.TAG_NAME,"a").get_attribute('href')

    def is_article_fav(self,art):
        try:
            art.find_element(By.CLASS_NAME,"ln-icon-heart-filled").get_attribute("innerHTML")
            return True
        except:
            return False


    def getthisarticle(self):
        infos= self.browser.find_elements(By.CLASS_NAME,"profile-hero__segment")
        contacts= self.browser.find_element(By.CLASS_NAME,"contacts").find_elements(By.TAG_NAME,"li")
        info =dict()
        info["url"]=self.browser.current_url
        info["name"]=isnull(infos,0)
        info["groupname"]=isnull(contacts,1)
        info["owner"]=isnull(contacts,0)
        info["address"]=isnull(infos,1)
        info["city"]=isnull(infos,3)
        info["sent"]=int(self.is_article_fav(self.browser.find_element(By.CLASS_NAME,"watch-property-trigger")))
        return info
    def getarticleinfos(self,url):
        self.browser.execute_script(f"window.open('{url}')")
        self.browser.switch_to.window(self.browser.window_handles[-1])
        info= self.getthisarticle()
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
        return info
    @classmethod
    def sent_article(meth,url):
        # print("https://loopnet.salimalaoui.repl.co/?sent="+re.findall("/(\d+)/$",url)[0])
        get("https://loopnet.salimalaoui.repl.co/?sent="+re.findall("/(\d+)/$",url)[0])





with open("data.json",'r') as f:
    jss = json.loads(f.read())

lmessage = jss["lastmessage"]

screen = Tk.Tk()
screen.geometry("600x400")
screen.title("Loopnet Automation")

logopic = Tk.PhotoImage(file = 'logo.png')

screen.iconphoto(False, logopic)


def clear():
    for c in screen.slaves():
        c.destroy()

# screen.configure(background='black')

def cont1(chrome,chromeuser):
    jss["chrome"]=chrome
    jss["chromeuser"]=chromeuser
    with open("data.json",'w') as f:
        f.write(str(jss).replace("'",'"'))
    clear()
    screen.quit()
    

def cont2():
    # for c in screen.children:
    clear()
    sync = Loopnet("chromedriver.exe",jss["chromeuser"])#,False)
    sync.login()
    sync.advancedsearch()
    sync.forsale()
    sync.chooseType()
    sync.filters()
    sync.sorting("AtoZ")
    total_pages = sync.getTotalPages()
    for article in sync.get_articles():
        if sync.is_article_fav(article):
            Loopnet.sent_article(sync.getarticle_href(article))
    for page in range(2,total_pages+1):
        for article in sync.getpage_articles(page):
            if sync.is_article_fav(article):
                Loopnet.sent_article(sync.getarticle_href(article))
    jss["state"]="log-in"
    with open("data.json",'w') as f:
        f.write(str(jss).replace("'",'"'))
    screen.quit()
    

while jss["state"]=="logged-out":
    ttk.Label(screen,text="Open Chrome://Version").pack(pady=(20,20))
    version = Tk.StringVar()
    chromeexe = Tk.StringVar()
    chromeuser = Tk.StringVar()
    ttk.Label(screen, text="Chrome Version:").pack()
    ttk.Entry(screen,textvariable=version).pack(pady=(20,20))
    ttk.Label(screen, text="Executable Path:").pack()
    ttk.Entry(screen,textvariable=chromeexe,width=60).pack(pady=(20,20))
    ttk.Label(screen, text="Profile Path:").pack()
    ttk.Entry(screen,textvariable=chromeuser,width=60).pack(pady=(20,20))
    ttk.Button(screen,text="Continue",command=lambda:cont1(chromeexe.get(),chromeuser.get())).pack()
    screen.mainloop()
    comm = Tk.Frame(screen)
    commandstyle = ttk.Style()
    commandstyle.configure("C.TLabel", foreground="black", background="white", borderwidth=1,relief="solid", width=60)
    commandstyle = ttk.Style()
    commandstyle.configure("C.TButton", foreground="white", background="black", borderwidth=1,relief="solid", width=20)
    log = Loopnet.openbrowserasuser(jss["chrome"],jss["chromeuser"])
    label = ttk.Label(comm, text=log.replace('--user-','--us...') ,style="C.TLabel")
    c = lambda : pc.copy(log) 
    button = ttk.Button(comm,text="COPY",command=c)
    title = ttk.Label(screen, text="Set Up",font=("Arial", 35))
    title.pack(pady=(80,0))
    ttk.Button(screen,text="Download Chrome Driver",command=lambda:open_url("https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/")).pack()
    ttk.Label(screen, text="copy this command on your terminal to log in",font=("Arial", 15)).pack(pady=(80,0))
    label.grid(column=1, row=10,padx=(50,0),pady=(80,0))
    button.grid(column=2, row=10,pady=(80,0))
    commandstyle = ttk.Style()
    commandstyle.configure("CON.TButton", foreground="blue", background="blue", borderwidth=1,relief="solid", width=40)
    contin = ttk.Button(screen,text="Continue",style="CON.TButton",command=cont2)
    comm.pack()
    contin.pack()
    screen.mainloop()


def add(url):
    global i
    i+=1
    if url!=None:
        req.append(url)
    clear()
    screen.quit()


def send(message):
    headless = askyesno(title="Browser Visible?", message="Do you Want to track Bot?")
    mybot = Loopnet("chromedriver.exe",jss["chromeuser"],headless)
    mybot.login()
    global lmessage
    lmessage = message
    jss["lastmessage"] = message
    with open("data.json",'w') as f:
        f.write(str(jss).replace("'",'"'))
    date = datetime.today()
    today = date.strftime("%A")
    date = str(date.day)+"/"+str(date.month)+"/"+str(date.year)
    for i in req:
        article = js[i]
        owner = article["owner"].split(' ')[0]
        groupname = article["groupname"]
        name = article["name"]
        city = article["city"]
        mybot.visitarticle(article["url"])
        exec(f'mybot.contact(f"""{message}"""+jss["priceless"] if article["price"] in [None,""] else "")')
        Loopnet.sent_article(article["url"])

    mybot.browser.close()
    clear()
    screen.quit()

def stop():
    global run
    run = False
    clear()
    screen.quit()

req = list()
get("https://loopnet.salimalaoui.repl.co/available?json=on")
rep = get("https://loopnet.salimalaoui.repl.co/available.json").content.decode()

js = json.loads(rep)

while True:
    req=[]
    i=0
    run=True
    while run:
        art = js[i]
        num = 0 
        article = Tk.Frame(screen)
        infomations = ttk.Frame(article)
        title = ttk.Label(infomations,text=art["name"]+" "+art["city"])
        subtitle = ttk.Label(infomations,text=art["groupname"]+"-"+art["owner"])
        price = ttk.Label(infomations,text="Price:"+(f"${art['price']:,}" if art["price"] not in [None,''] else "not set")+("  No* Rooms:"+str(art["rooms"]) if art["rooms"] is not None  else " not set"))
        title.grid(row=0,column=0)
        subtitle.grid(row=1,column=0)
        price.grid(row=2,column=0)
        ttk.Button(infomations,text="open on Loopnet",command=lambda:open_url(art["url"])).grid(row=0,column=2)
        if art["sentforowner"]>0:
            requestfor = ttk.Label(infomations,text=str(art["sentforowner"])+" sent for this before",foreground="red")
            requestfor.grid(row=1,column=1) 

        ttk.Button(infomations,text="Request",command=lambda:add(art["id"]) ).grid(row=5,column=1)
        ttk.Button(infomations,text="SKIP",command=lambda:add(None) ).grid(row=5,column=0)
        infomations.pack( side='left',pady=(50,0))
        article.pack()
        ttk.Button(screen,text="Save and Quit",command=stop).pack(pady=(40,0))
        screen.mainloop()

    ttk.Label(screen,text="MESSAGE",font=("Arial 18")).pack(pady=(30,0))
    option = ttk.Frame(screen)

    ttk.Label(option,text="{owner} for proprety owner",foreground="blue").grid(row=0,column=0,padx=(10,10))
    ttk.Label(option,text="{groupname} for group name",foreground="blue").grid(row=0,column=1,padx=(10,10))
    ttk.Label(option,text="{name} for proprety name",foreground="blue").grid(row=0,column=2,padx=(10,10))
    ttk.Label(option,text="{city} for proprety city",foreground="blue").grid(row=1,column=0)
    ttk.Label(option,text="{date} for date",foreground="blue").grid(row=1,column=1)
    ttk.Label(option,text="{today} for today name",foreground="blue").grid(row=1,column=2)
    option.pack()

    message = Tk.Text(screen,height = 8, width = 52,font=("Arial 10"))
    message.pack(pady=(30,20))
    message.insert(Tk.END, lmessage)

    fr = ttk.Frame(screen)
    
    ttk.Button(fr,text="cancel",command=stop).grid(row=0,column=0)
    ttk.Button(fr,text="Send Requests",command=lambda:send(message.get(1.0,Tk.END))).grid(row=0,column=1)
    fr.pack()
    screen.mainloop()





