from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 100
TWITTER_EMAIL = "lallupallu78@gmail.com"
TWITTER_PASSWORD = "lalluisequalto"
chrome_driver_path = "C:\Development\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        print(self.down)
        print(self.up)
    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get("https://twitter.com/")
            self.driver.maximize_window()
            time.sleep(2)
            login = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
            login.click()
            time.sleep(2)
            email = self.driver.find_element(By.NAME, "text")
            email.send_keys(TWITTER_EMAIL)
            email.send_keys(Keys.ENTER)
            time.sleep(2)
            username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys("stephen_marbury")
            username.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(3)
            tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            message = f"Hello Internet Provider, why is my Internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
            tweet.send_keys(message)
            button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            button.click()


TwitterBot = InternetSpeedTwitterBot()
TwitterBot.get_internet_speed()
TwitterBot.tweet_at_provider()