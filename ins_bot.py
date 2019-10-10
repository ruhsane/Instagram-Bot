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

        # go to ins main page
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        # find login button and click
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)

        # find username field and fill
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        # password field and fill
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)

        #hit enter
        password_elem.send_keys(Keys.RETURN)

myfile = open("pw.txt", "rt") # open pw.txt for reading text
pw = myfile.read()         # read the entire file into a string
myfile.close()              # close the file

ruhsane = InstagramBot("ruhsane", pw)
ruhsane.login()