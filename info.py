from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sqlite3
import random

conn = sqlite3.connect("db2.sqlite")
cur = conn.cursor()
# with open("urls.txt",'r') as file:
#     urls = file.read().split('\n')

def isnull(l,ind):
    try :
        return l[ind].text.strip()
    except: 
        return ''
cur.execute("select id,url from property where assessment<1000")
# curid = cur.fetchone()[0]
urls = cur.fetchall()
print(urls)
# input()
options = Options()

# options.add_argument('--headless')

browser = webdriver.Chrome(executable_path="chromedriver.exe",options=options)

# for i,url in enumerate(urls[curid:],curid):

# "feature-grid__data"
d=0
for  n,url in urls:
    if True :#r is None:
        print(url)
        print(str(((n+1)/len(urls))*100)[:5],"%")
        i = n-d
        browser.get(url)
        infos = browser.find_elements (By.CLASS_NAME, "feature-grid__data")
        price = str()
        rooms = str ()
        assessment =""
        data = browser.find_element(By.CLASS_NAME,"featured-grid").find_elements(By.TAG_NAME,"td")
        for b,ele in enumerate(data):#"taxes-zoning__nowrap"):
            if "Total Assessment" in ele.text:
                assessment = data[b+1].text
                break
        # input(str(assessment))

        # try:
        #     rooms = browser.find_element(By.CLASS_NAME,"profile-hero-sub-title").find_element(By.CLASS_NAME,"profile-hero__segment").text.split(' ')[0]
        # except:
        #     rooms=""
        
        # try:
        #     if "This listing is not currently being advertised on LoopNet.com" in browser.find_element(By.CLASS_NAME,"listing-not-visible-header").text :
        #         # input("this")
        #         cur.execute(f"delete from property where id={i}")
        #         cur.execute(f"update property set id =id-1 where id>{i}")
        #         print("?????????????????????? deleted ",i)
        #         d+=1
        #         continue
        # except:
        #     pass

        # try:
        #     if "This Hospitality Property is no longer advertised" in browser.find_element(By.CLASS_NAME,"off-market-banner").text:
        #         # input("this")
        #         cur.execute(f"delete from property where id={i}")
        #         cur.execute(f"update property set id =id-1 where id>{i}")
        #         print("?????????????????????? deleted ",i)
        #         d+=1
        #         continue
        # except:
        #     pass
        # for ele in infos:
        #     if ele.get_attribute("data-fact-type")=="Price":
        #         price = ele.text
        #         # elif ele.get_attribute("data-fact-type")=="NoRooms":
        #         #     rooms = ele. text
        #         # if price!="" and rooms!="":
                
        #         # break
        #     elif rooms=="" and ele.get_attribute("data-fact-type")=="NoRooms":
        #         rooms = ele.text
        #     # elif ele.get_attribute("data-fact-type")=="NumberOfProperties":
        #     #     cur.execute(f"delete from property where id={i}")
        #     #     cur.execute(f"update property set id =id-1 where id>{i}")
        #     #     print("?????????????????????? deleted ",i)
        #     #     d+=1
        # if rooms!="":
        #     cur.execute(f'update property set rooms={rooms} where id={i}')
        # if price!="":
        #     cur.execute(f'update property set price={price[1:].replace(",","")} where id={i}')
        if assessment!="":
            print(f'update property set assessment={assessment[1:].replace(",","")} where id={i}')
            cur.execute(f'update property set assessment={assessment[1:].replace(",","").split(" ")[0]} where id={i}')
        print(price,rooms,assessment)

        # infos= browser.find_elements(By.CLASS_NAME,"profile-hero__segment")
        # contacts= browser.find_element(By.CLASS_NAME,"contacts").find_elements(By.TAG_NAME,"li")
        # print(f"insert into property values({i},'{url}','{isnull(infos,0)}','{isnull(contacts,1)}','{isnull(contacts,0)}','{isnull(infos,1)}','{isnull(infos,3)}',0,0)")
        # cur.execute(f'insert into property values({i},"{url}","{isnull(infos,0)}","{isnull(contacts,1)}","{isnull(contacts,0)}","{isnull(infos,1)}","{isnull(infos,3)}",0,0)')
        # print(f'update property set rooms={rooms} where id={i}');input()
cur.execute("select * from property where assessment<1000")
# res = cur.fetchall()
# for i in range(6):
#     print(random.choice(res))

# print(res[-1])

# print("total del",d)


input("----------------------------------------finished----------------------------------------")
    
conn.commit()
    



# CREATE TABLE property(id int AUTO_INCREMENT ,url varchar(100),name  varchar(40),groupname varchar(100),owner varchar(40),address varchar(50),city varchar(30),sent int ,checked int);






