from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

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
        time.sleep(2)

        # find login button and click
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(1)

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
        time.sleep(2)
    
    def get_valid_photo_links(self, hashtags):
        driver = self.driver 
        pic_hrefs = []

        for hashtag in hashtags:
            driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
            time.sleep(2)
            
            # bot scrolls down to web page to get new pictures
            for i in range(1, 2):
                try: 
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    # get all the tags
                    hrefs_in_view = driver.find_elements_by_tag_name('a')
                    # finding relevant hrefs
                    pics_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]
                    # building list of unique photos
                    [pic_hrefs.append(href) for href in pics_in_view if href not in pic_hrefs]
                    print(hashtag + ' photos: ' + str(len(pic_hrefs)))
                except Exception:
                    continue

        return pic_hrefs

    def like_photo(self, hashtags):
        driver = self.driver
        pic_hrefs = self.get_valid_photo_links(hashtags)

        # like pics
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                print('Liked!')
                for second in range(0, random.randint(2, 3)):
                    print('# unique photos left: ' + str(unique_photos) + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

    def comment(self, hashtags):
        pic_hrefs = self.get_valid_photo_links(hashtags)
        comments = ['Keep up the good work! 👏💪', 'I love this']
        for pic in pic_hrefs:
            self.driver.get(pic)
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            comment_field = lambda: self.driver.find_element_by_tag_name('textarea')
            comment_field().click()
            comment_field().clear()

            comment = random.choice(comments)
            for letter in comment:
                comment_field().send_keys(letter)
                time.sleep(0.2)

            comment_field().send_keys(Keys.RETURN)


if __name__ == "__main__":

    username = "ruhsane"
    myfile = open("pw.txt", "rt") # open pw.txt for reading text
    pw = myfile.read()         # read the entire file into a string
    myfile.close()              # close the file

    ig = InstagramBot(username, pw)
    ig.login()

    hashtags_in_niche = [
        'coding','programming','computerscience'
    ]

    # ig.like_photo(hashtags_in_niche)
    ig.comment(hashtags_in_niche)