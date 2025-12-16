from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#start selenium browser session
driver = webdriver.Chrome()

#load desired page in chrome browser
driver.get("https://duckduckgo.com/")
print("Initial Page Title: ", driver.title)
driver.implicitly_wait(10)

#access the controls on the page 
search_box = driver.find_element(By.NAME,"q")

# interact with the control
# for ch in "dkte college ichalkaranji":
#     search_box.send_keys(ch)
#     time.sleep(0.2)
search_box.send_keys("dkte college ichalkaranji")
search_box.send_keys(Keys.RETURN)

# wait for the result
print("Later Page Title:", driver.title)

# stop the session
time.sleep(10)
driver.quit()


