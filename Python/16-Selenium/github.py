from GitHubUserInfo import username, password
from selenium import webdriver
import time

class GitHub:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)


        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click()

github = GitHub(username, password)
github.signIn()