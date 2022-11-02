from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import sys

#https://www.inc.com/lolly-daskal/100-motivational-quotes-that-will-inspire-you-to-succeed.html finished quote number 26 start doing 27 (37 quotes done)
quotes = ["Act as if what you do makes a difference. It does.", "Believe you can and you're halfway there.", "Life is like riding a bicycle. To keep your balance, you must keep moving.", "You are never too old to set another goal or to dream a new dream.", "It is never too late to be what you might have been.", "Some people look for a beautiful place. Others make a place beautiful.", "We must be willing to let go of the life we planned so as to have the life that is waiting for us.", "Happiness is not by chance, but by choice.", "If I cannot do great things, I can do small things in a great way.", "To live a creative life, we must lose our fear of being wrong.", "If you are not willing to risk the usual you will have to settle for the ordinary.", "Trust because you are willing to accept the risk, not because it's safe or certain.", "All our dreams can come true if we have the courage to pursue them.", "If you do what you always did, you will get what you always got.", "Success is walking from failure to failure with no loss of enthusiasm.", "Just when the caterpillar thought the world was ending, he turned into a butterfly.", "Successful entrepreneurs are givers and not takers of positive energy.", "Opportunities don't happen, you create them.", "Great minds discuss ideas; average minds discuss events; small minds discuss people.", "I have not failed. I've just found 10,000 ways that won't work.", "If you don't value your time, neither will others. Stop giving away your time and talents--start charging for it.", "No one can make you feel inferior without your consent.", "If you're going through hell keep going.", "Don't raise your voice, improve your argument.", "What seems to us as bitter trials are often blessings in disguise.", "The meaning of life is to find your gift. The purpose of life is to give it away."]
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://login.microsoftonline.com/042a40a1-b128-4ac4-8648-016ffa121487/oauth2/authorize?client_id=05225f13-8d22-41e5-81e5-67ff5ddac166&redirect_uri=https%3A%2F%2Fpap.lausd.net%2F&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DAUOzF5aLsj99GagHgMPgesTZy9wjhgHKhar2AD7h3cBl4hFoipBlQrS-B5fyMVsM5U04PRp8wdTMnRntCPSILwX7Hr3tGtzkPhyDanZlAZoXO7JZpZPlz-KirF2kwNpBdqVLqXFQC0TcoJBfKPlrNVylcAqRc3nZnUKkYMTHOE4XcT0KAc3o9YbUNnFCPNyUoGdahKqBjjgH7YYycacvNqt3UPvCRF7KWcyOvJaUcLGXeoAk9uJPb_6Dfw-dL9ZLLYSr9ozz7dZqElJyJISX3WPKZT9MuA_6k55LyXMFO1ukFDZGEi-Qqjai28F44DkacDLImitrXF6ak47k6P6xHi8C80kPFWpSHiji5_f2R9F2IDfxCoLwzbw7F8YCG9mj&response_mode=form_post&nonce=637799904934746147.YTNlMmQ2ZWItNzA0Yy00MDQ0LWI4MzYtNzBlMDJjMGVkYzBmNmM2NzdhOTctNDhjMC00ZjlmLThkMTQtZDZmMmM3Mjc5MWEz&ui_locales=en-US&x-client-SKU=ID_NET461&x-client-ver=5.3.0.0&sso_reload=true")
email = driver.find_element_by_id("i0116")
email.send_keys("bkim0076@mymail.lausd.net")
email.send_keys(Keys.RETURN)
time.sleep(1)
pw = driver.find_element_by_id("i0118")
pw.send_keys("Lausdbaron10")
pw.send_keys(Keys.RETURN)
driver.find_element_by_xpath('//a[@href="/en-US/SignIn?returnUrl=%2F"]').click()
driver.find_element_by_id("https://login.windows.net/042a40a1-b128-4ac4-8648-016ffa121487/").click()
time.sleep(1)
driver.find_element_by_class_name("close").click()
driver.find_element_by_id("create_pass").click()
time.sleep(1)
driver.find_element_by_class_name("close").click()
driver.find_element_by_class_name("selection-card").click()
time.sleep(1)
driver.find_element_by_class_name("close").click()
driver.find_element_by_xpath('/html/body/form/div[5]/button').click()
driver.find_element_by_id('anycovid19symptoms_0').click()
driver.find_element_by_id('btnProceed').click()
time.sleep(1)
link = driver.current_url

driver.get("https://www.shorturl.at/")
driver.find_element_by_xpath('//*[@id="formurl"]/input').send_keys(link)
driver.find_element_by_xpath('//*[@id="formbutton"]/input').click()
driver.find_element_by_xpath('//*[@id="formbutton"]/input').click()
driver.find_element_by_xpath('//*[@id="formbutton"]/input').click()
time.sleep(1)

driver.get("https://voice.google.com/about")
driver.find_element_by_xpath('/html/body/div[1]/div[2]/a[2]').click()
driver.find_element_by_id('identifierId').send_keys("dailypassmaker@gmail.com")
driver.find_element_by_css_selector('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d').click()
time.sleep(1.5)
driver.find_element_by_xpath('//div/div/div/input').send_keys("Lausdbaron10")
time.sleep(0.5)
driver.find_element_by_xpath('//div/div/div/input').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/gv-side-nav/div/div/gmat-nav-list/a[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/gv-messaging-view/div/div/md-content/div/div/div').click()
driver.find_element_by_id('input_0').send_keys("2134365875")
driver.find_element_by_id('input_0').send_keys(Keys.RETURN)
driver.find_element_by_xpath('//*[@id="input_1"]').click()
driver.find_element_by_xpath('//*[@id="input_1"]').send_keys("\"")
driver.find_element_by_xpath('//*[@id="input_1"]').send_keys(random.choice(quotes))
driver.find_element_by_xpath('//*[@id="input_1"]').send_keys("\" ")
a = ActionChains(driver)
a.key_down(Keys.CONTROL).send_keys("v").perform()
driver.find_element_by_xpath('//*[@id="ib6"]').click()
driver.close()
sys.exit(0)