from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from django.test import TestCase
from time import sleep
# driver = Chrome()

browser = webdriver.Firefox(executable_path='./geckodriver')
# browser.set_window_size(900,900)
# browser.set_window_position(0,0)
browser.get("https://otrc.stephensoncancercenter.org/Mobile-Health-Technology/Contact-Us")
# print(browser.title)
# assert "Oklahoma" in browser.title
print(browser.current_url)
firstname=browser.find_elements_by_id('QR~QID1~1~label')
print(firstname)
# sleep(10)
browser.close()



