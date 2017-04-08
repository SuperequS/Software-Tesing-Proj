#coding = utf-8
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.gaoqing.la")

print ("Brower maxmize")

driver.maximize_window()