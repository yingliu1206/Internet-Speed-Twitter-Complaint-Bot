from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

speed_url = 'https://x.com/'
username = 'YingLiu1028074'
pwd = 'LY19971214'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


#get into the website
driver = webdriver.Chrome(options=chrome_options)
driver.get(speed_url)

time.sleep(3)
link = driver.find_element(By.CSS_SELECTOR, '[data-testid="loginButton"]')
link.click()

time.sleep(3)
driver.find_element(By.NAME, value = 'text').send_keys(username)

time.sleep(3)
button = driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
button.click()

time.sleep(3)
driver.find_element(By.NAME, value = 'password').send_keys(pwd)
span = driver.find_element(By.XPATH, "//span[text()='Log in']")
span.click()

# draft the tweet
time.sleep(5)
div_element = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')
div_element.send_keys(f'Hey Verizon, why is my home internet speed?')



#
#
# time.sleep(60)
# down = driver.find_element(By.XPATH,
#                                      value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
# up = driver.find_element(By.XPATH,
#                                    value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
#
# print(down)
# print(up)
# # time.sleep(3)
# # print(driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))
# # # print(driver.find_element(By.XPATH, value= '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))
