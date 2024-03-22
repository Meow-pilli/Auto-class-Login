from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from discord_webhook.webhook import DiscordEmbed
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook
from selenium import webdriver
from datetime import datetime
from os import environ
import schedule
import time


now = datetime.now()
x = now.strftime("%H:%M")
y = environ['discord_webhook']
chrome_options = Options()
#chrome_options.binary_location = environ['GOOGLE_CHROME_BIN']
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })
#driver = webdriver.Chrome(executable_path=environ['CHROMEDRIVER_PATH'], chrome_options=chrome_options)

def login_domain():
    driver = webdriver.Chrome()
    url = environ['domain_link']
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/input').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/input').send_keys(environ['time_username'])
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[5]/input').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[5]/input').send_keys(environ['time_password'])
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/input[2]').click()
    driver.find_element_by_xpath('/html/body/div[4]/div/section/div/div[2]/div/a/div').click()

def testing():
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='Up and running', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()

def login_ccc():
    driver = webdriver.Chrome()
    url = environ['ccc_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='CCC class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()
def login_aptitude():
    driver = webdriver.Chrome()
    url = environ['aptitude_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='Aptitude class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()
def login_verbal():
    driver = webdriver.Chrome()
    url = environ['verbal_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='Verbal class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()
def login_resume():
    driver = webdriver.Chrome()
    url = environ['resume_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='resume class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()

def start_browser():

	global driver
	driver = webdriver.Chrome(chrome_options=chrome_options,service_log_path='NUL')

	WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

schedule.every().monday.at("12:30").do(login_ccc)
schedule.every().monday.at("14:30").do(login_verbal)
schedule.every().monday.at("16:00").do(login_domain)

schedule.every().tuesday.at("12:30").do(login_ccc)
schedule.every().tuesday.at("14:30").do(login_verbal)
schedule.every().tuesday.at("16:00").do(login_domain)

schedule.every().wednesday.at("12:30").do(login_ccc)
schedule.every().wednesday.at("14:30").do(login_verbal)
schedule.every().wednesday.at("16:00").do(login_domain)

schedule.every().thursday.at("12:30").do(login_ccc)
schedule.every().thursday.at("14:30").do(login_resume)
schedule.every().thursday.at("16:00").do(login_domain)

schedule.every().friday.at("12:30").do(login_ccc)
schedule.every().friday.at("14:30").do(login_resume)
schedule.every().friday.at("16:00").do(login_domain)

schedule.every().saturday.at("12:30").do(login_verbal)

testing()
start_browser()
while True:
    schedule.run_pending()
    time.sleep(1)