from selenium import webdriver
from speed import InternetSpeedTwitterBot

username = '********'
pwd = '********'
PROMISED_DOWN = 300
PROMISED_UP = 300
speed_url = 'https://www.speedtest.net/'
tweet_url = 'https://x.com/'

# create the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = InternetSpeedTwitterBot(chrome_options)
bot.get_internet_speed(url = speed_url)
print('down', bot.down)
print('up', bot.up)
bot.tweet_at_provider(url = tweet_url, username=username, pwd=pwd)
