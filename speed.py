from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class InternetSpeedTwitterBot:

    def __init__(self, chrome_options):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, url):
        self.driver.get(url)

        time.sleep(3)
        link = self.driver.find_element(By.XPATH, '//*[@aria-label="start speed test - connection type multi"]')
        link.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, value= '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self, url, username, pwd):
        self.driver.get(url)

        #click login
        time.sleep(3)
        link = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="loginButton"]')
        link.click()

        #enter username
        time.sleep(3)
        self.driver.find_element(By.NAME, value='text').send_keys(username)

        #click next and enter pwd
        time.sleep(3)
        button = self.driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
        button.click()

        time.sleep(3)
        self.driver.find_element(By.NAME, value='password').send_keys(pwd)
        span = self.driver.find_element(By.XPATH, "//span[text()='Log in']")
        span.click()

        # draft the tweet
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')
        element.send_keys(f'Hey Verizon, why is my home internet speed {self.down} down/{self.up} up?')



