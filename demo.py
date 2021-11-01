from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import locators

browser = webdriver.Chrome()
browser.get("https://desktop.any.do/")

# Login_With_Email, worked but now making problems
login_link = browser.find_element_by_class_name("AppLoginButton--email")
login_link.click()

browser.implicitly_wait(1)
# username_box = browser.find_element_by_xpath('/html/body/div/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/input')
username_box = browser.find_element(*locators.LoginPageLocator.EMAIL)
username_box.send_keys("info.oytizzo@gmail.com")
username_arrow = browser.find_element_by_xpath('/html/body/div/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/button')
username_arrow.click()
browser.implicitly_wait(3)
password_box = browser.find_element_by_xpath('/html/body/div/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input')
password_box.send_keys('helloworld')
password_box.submit()
# worked
