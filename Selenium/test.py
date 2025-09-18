from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ytopt = webdriver.ChromeOptions()
ytopt.add_experimental_option("detach",True)

yt = webdriver.Chrome(options=ytopt)
yt.get("https://www.youtube.com/")

searchbar = yt.find_element(By.NAME,value="search_query")
searchbar.send_keys("coolie powerhouse")

searchbutton = yt.find_element(By.XPATH,value='//*[@id="center"]/yt-searchbox/button')
searchbutton.click()

time.sleep(4)
first_vdo = yt.find_element(By.PARTIAL_LINK_TEXT,value="Official Lyric Video")
first_vdo.click()

time.sleep(6)

skipButton = yt.find_element(By.XPATH,value='//*[@id="skip-button:2"]')
skipButton.click()
vdoplay = yt.find_element(By.TAG_NAME,value="html")
vdoplay.send_keys('F')