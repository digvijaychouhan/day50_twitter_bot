import time
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_PATH_DRIVER = "C:/Softwares/chromedriver_win32/chromedriver.exe"
TWITTER_EMAIL =
TWITTER_PASSWORD =


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH_DRIVER)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(60)
        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(down.text)
        print(up.text)

    def tweet_at_provider(self):
        print("Hi")


bot = InternetSpeedTwitterBot()
# bot.driver.get("https://twitter.com/i/flow/login")
# time.sleep(3)
#
# bot.driver.find_element(By.CSS_SELECTOR, ".css-901oao").send_keys(TWITTER_EMAIL)
# bot.driver.find_element(By.CSS_SELECTOR, ".css-18t94o9").click()


bot.get_internet_speed()
bot.tweet_at_provider()