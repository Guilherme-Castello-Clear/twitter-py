from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

TWITTER_EMAIL = "guiauguisto.castello@gmail.com"
TWITTER_PASSWORD = "nop"
