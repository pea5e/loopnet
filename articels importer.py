from selenium import webdriver
from time import sleep
import re
from time import time
from selenium.webdriver.chrome.options import Options
# from keep import keep
from selenium.webdriver.common.by import By

# keep()


option = Options()
# option.add_argument('--no-sandbox')
# option.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(executable_path="chromedriver.exe",options=option)

browser.get("https://www.loopnet.com/")

# browser.get("https://www.loopnet.com/search/hospitality-properties/for-sale/?sk=769afb46582c3e18b8fc0ebfc79c6f32&bb=mtp9l9tyjeo03nl33i5Q")
browser.find_element(By.CLASS_NAME,"advanced").click()
while  True:
    try:
        browser.find_element(By.CLASS_NAME,"save-search-reg-overlay-show")
        break
    except:
        sleep(1)

browser.find_elements(By.CLASS_NAME,"csgp-modal-close")[-1].click()

# print(browser.find_element(By.CLASS_NAME,"input-select-multiple").find_elements(By.TAG_NAME,"li")[-4])
# fil = "document.getElementsByClassName('advanced-filters-fs')[0]"

# for ele in browser.find_element(By.CLASS_NAME,"input-select-multiple").find_elements(By.TAG_NAME,"input")[:-4:4]:
#     ele.location_once_scrolled_into_view
# for i in range(10):
    # # browser.execute(f"{fil}.scroll(0,{fil}.scrollHeight*{(i+1)*0.1})")
    # inp = browser.find_element(By.CLASS_NAME,"input-select-multiple").find_elements(By.TAG_NAME,"input")[-4]
    # # print(browser.find_element(By.CLASS_NAME,"input-select-multiple").find_elements(By.TAG_NAME,"input")[-4].location_once_scrolled_into_view)
    # if inp.location_once_scrolled_into_view['x']!=0 and inp.location_once_scrolled_into_view['y']!=0:
    #     print(inp.location_once_scrolled_into_view)
    #     # .find_elements(By.TAG_NAME,"li")[-4]
    #     # click()
    #     # break
    # else:
    #     # browser.execute(f"{fil}.scrollTo(0,{fil}.scrollHeight*{(i+1)*0.1})")
    #     browser.execute("console.log(\"salim\"")
[ele for ele in browser.find_element(By.CLASS_NAME,"input-select-multiple").find_elements(By.TAG_NAME,"input") if ele.location['x']!=0 and ele.location['y']!=0][-4].click()
for ele in browser.find_elements(By.CLASS_NAME,"column-12")[1].find_elements(By.TAG_NAME,"input"):
    ele.click()
    # print("'",ele.text,ele.get_attribute('innerHTML'),"'")


# for ele in browser.find_elements(By.CLASS_NAME,"column-12")[2].find_elements(By.TAG_NAME,"input")[]:
#     ele.click()
#     print("'",ele.get_attribute('innerHTML'),"'")
browser.find_elements(By.CLASS_NAME,"column-12")[2].find_element(By.TAG_NAME,"input").click()

browser.find_elements(By.CLASS_NAME,"range-from")[13].find_element(By.TAG_NAME,"input").send_keys("40")

browser.find_elements(By.CLASS_NAME,"column-12")[-1].find_elements(By.TAG_NAME,"button")[-1].click()
sleep(3)
browser.find_element(By.CLASS_NAME,"sort-wrapper").click()

newest = 1
oldest = 2
AtoZ = -4
browser.find_element(By.CLASS_NAME,"sort-wrapper").find_elements(By.CLASS_NAME,"drop-down-menu")[1].find_elements(By.TAG_NAME,"li")[newest].click()
sleep(5)

total_pages = int(browser.find_elements(By.CLASS_NAME,"afterellipsisli")[1].text.strip())
print(total_pages)
generatedurl = browser.current_url
print(generatedurl)
urls = []
for article in browser.find_elements(By.TAG_NAME,"article"):
    print(article.find_element(By.TAG_NAME,"a").get_attribute('href'))
    urls.append(article.find_element(By.TAG_NAME,"a").get_attribute('href'))
    input()
for page in range(2,total_pages+1):
    print("page:",page)
    browser.get(generatedurl.replace("for-sale/","for-sale/"+str(page)+"/"))
    for article in browser.find_elements(By.TAG_NAME,"article"):
        print(article.find_element(By.TAG_NAME,"a").get_attribute('href'))
        urls.append(article.find_element(By.TAG_NAME,"a").get_attribute('href'))
    # try:
    #     print(browser.find_element(By.CLASS_NAME,"input-select-multiple").find_elements(By.TAG_NAME,"li")[-4].find_element(By.TAG_NAME,"input").location_once_scrolled_into_view)
    #     # .find_elements(By.TAG_NAME,"li")[-4]
    #     # click()
    #     # break
    # except:
    #     browser.execute(f"{fil}.scroll(0,{fil}.scrollHeight*{(i+1)*0.1})")
with open("urls1.txt",'w') as file:
    file.write("\n".join(urls))
    
# browser.execute_script("selectMainCategory(128)")
# selectMainCategory(128)
