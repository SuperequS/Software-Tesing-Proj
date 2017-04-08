# selenium + Python  auto test practice
# author:Superequz
#date:26/03/2017

#coding = utf-8

from selenium import webdriver	#import webdriverAPI

#driver = webdriver.Firefox()	#new obj will launch the brower
edge = webdriver.Edge()

baiduUrl = 'http://www.baidu.com'

'''
#///test 1 open a website

#get brower object,diff brower have diff function
brower1 = webdriver.Firefox()	#Firefox

# brower2 = webdriver.Ie()	#ie
# brower3 = webdriver.Chrome()	#Chrome	#blockcomments with ctrl + /

#test baidu funcion,modify user operation,the speed limited by brower access speed.

brower1.get("http://www.baidu.com")
brower1.find_element_by_id("kw").send_keys("time")
brower1.find_element_by_id("su").click()

#brower1.quit()
'''

'''
#///test2 python webdriver API

driver.maximize_window()	#maximize the window
driver.set_window_size(480, 800)	#set width 480,high 800

# need import time package
import time

firtst_url = 'http://www.baidu.com'
print("now access %s"  %(firtst_url))	#format output
driver.get(firtst_url)

secend_url = 'http://news.baidu.com'
driver.get(secend_url)

#modify forward & back fucntion
#back to first_url
driver.back()

#forward to secend_url
driver.forward()
'''

'''
#///test3 obj position

#1 html location
#webdriver has offered many elements & obj
#such as id name class_name tag_name link_text partial_link_text xpath css selector
# mapping for find_element_by_id(),find_element_by_name(),find_element_by_class_name()...
#each item may have id name class tag

#2 html location
#Xpath use for layered element
find_element_by_xpath("/html/body/diiv[2]/form/span/input")	#abs position
find_element_by_xpath("//input[@id='input']")	#relative position
find_element_by_xpath("//span[@id='input-container']/input")	#other way to relative...to

#3 css location

'''

#///test4 operation obj
#interreactive with page through WebElementAPI

'''
webdirver.clear()	#clear all containts if possibe
webdriver.send_keys()	#modify keyborad input
webdriver.click()	#modify mouse input
webdriver.submit()	#post table
'''
'''
#log in modify

url = 'https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fwww.mi.com%252F%26sign%3DNWU4MzRmNjBhZmU4MDRmNmZkYzVjMTZhMGVlMGFmMTllMGY0ZTNhZQ%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180'
driver.get(url)

account = 'testaccount'
password = 'testaccount'


driver.find_element_by_id("username").clear()	#clear deafult info
driver.find_element_by_id("username").send_keys(account)

driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys(password)

driver.find_element_by_id("login-button").click()

driver.quit()
'''
'''
#other API test

edge.get(baiduUrl)
boxSize = edge.find_element_by_id("kw").size    #return ele size
print ("00",boxSize) 

text = edge.find_element_by_id("kw").text    #return ele text
print ("01",text)

attribute = edge.find_element_by_id("kw").get_attribute('type')    #return ele attribute
print ("02",attribute)
'''

'''
#///test5 click event
#class: ActionChains
#funct: context_click(),double_click(),drag_and_drop(),move_to_element(),click_and_hold()

from selenium.webdriver.common.action_chains import ActionChains

edge.get(baiduUrl)
myelement = edge.find_element_by_id("kw")
ActionChains(edge).context_click(myelement).perform()
'''

#///test6 keyboard event