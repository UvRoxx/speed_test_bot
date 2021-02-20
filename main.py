from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

URL = "https://www.speedtest.net/"
DRIVER_PATH = "/Users/utkarshvarma/Dropbox/My Mac (UTKARSHs-MacBook-Pro.local)/Documents/Development/chromedriver"
PROMISED_DOWN = 150
PROMISED_UP = 10
UID = os.environ['TWITTER_ID']
PASS = os.environ['TWITTER_PASS']
TWITTER_URL = "https://twitter.com/login"

def send_tweet(present_up, present_down):
    print(present_up)
    print(present_down)
    driver.get(TWITTER_URL)
    sleep(5)
    user_name = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    user_name.send_keys(UID)
    password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    password.send_keys(PASS)
    password.send_keys(Keys.ENTER)
    sleep(5)
    tweet_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/'
                                             'div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
    tweet_box.send_keys(f"I was promised {PROMISED_DOWN} Download and {PROMISED_UP} but im getting {present_down}/{present_up} why!!!!")
    send_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div')
    send_button.click()
    print("DONE")
    pass


driver = webdriver.Chrome(DRIVER_PATH)
driver.get(URL)

driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
sleep(45)
download_speed = float(driver.find_element_by_xpath(
    '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
    '/div[2]/div/div[2]/span').text)
upload_speed = float(driver.find_element_by_xpath(
    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]'
    '/div/div[2]/span').text)

if download_speed < PROMISED_DOWN or upload_speed<PROMISED_UP:
    send_tweet(download_speed,upload_speed)

