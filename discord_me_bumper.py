from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# config vars
email = "name@domain.com"
pw = "yourPasswordABC123"
PATH = "path_to_chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://discord.me/login')
login_btn = driver.find_element_by_css_selector("[type=submit]")
fill_email = driver.find_element_by_css_selector("[type=email]")
fill_pw = driver.find_element_by_css_selector("[type=password]")
bump_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[1]/div[4]/div/div[1]/div/div/div[2]/div/div[2]/div/div[4]/a[1]')


def discordme_login():
    time.sleep(10)
    fill_email.send_keys(email)
    fill_pw.send_keys(pw)
    login_btn.click()
    time.sleep(5)


def discordme_bump():
    while True:
        bump_btn.click()
        time.sleep(7201)


discordme_login()
discordme_bump()