from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import undetected_chromedriver as uc

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get()