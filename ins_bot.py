from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        # <a href="/accounts/login/?source=auth_switcher">Log in</a>
        # <input .... name="username" type="text" value="">
        # <input .... name="password" type="text" value="">

        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)


myfile = open("pw.txt", "rt") # open pw.txt for reading text
pw = myfile.read()         # read the entire file into a string
myfile.close()              # close the file

ruhsane = InstagramBot("ruhsane", pw)
ruhsane.login()