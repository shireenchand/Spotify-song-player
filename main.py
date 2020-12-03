from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

song = input("Enter the name of the song: ")
artist = input("Enter the name of the artist(Enter skip if don't know): ")
PATH = "/Users/niharjagruti/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://accounts.spotify.com/en/login")

username = driver.find_element_by_id("login-username")
username.send_keys(YOUR_EMAIL)
password = driver.find_element_by_id("login-password")
password.send_keys(YOUR_PASSWORD)
login = driver.find_element_by_id("login-button")
login.click()

time.sleep(3)
if artist == 'skip':
    driver.get(url='https://open.spotify.com/search' + '/' + song)
else:
    driver.get(url='https://open.spotify.com/search'+'/'+song+'%20'+artist)


driver.maximize_window()

time.sleep(2)

pyautogui.click(670,465, clicks=2, interval=1)




time.sleep(60)