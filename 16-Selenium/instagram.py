from InstagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        time.sleep(2)
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        
        print(f"First Count: {followerCount}")
        
        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                time.sleep(1)
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break
        
        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")            
            followerList.append(link)            

        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == 'Follow':
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
            time.sleep(2)
        else:
            print("Zaten Takip Ediyorsun")
    
    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == "Message":
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span").click()
            time.sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
        else:
            print("Zaten Takip Etmiyorsun")


instagram = Instagram(username, password)
instagram.signIn()
# instagram.getFollowers()
# instagram.followUser("python.hub")
instagram.unFollowUser("python.hub")

