
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

username = ""
password = ""
class instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username= username
        self.password = password
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)


    def getfollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")   

        followerslink = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").click()
        followerslink.send_keys(self.username)
        followerslink.send_keys(Keys.ENTER)
    def followuser(self,username):
        self.username = username
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followbutton = self.browser.find_element_by_tag_name("button")
        followbutton.click()
             

instgrm = instagram(username,password)
instgrm.signIn()  
#instgrm.getfollowers()
instgrm.followuser("username")