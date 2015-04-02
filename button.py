# script to push the button every 10 min

from selenium import webdriver
import time

url = 'http://algersoft.net/kriegerathome/'

page = webdriver.Firefox()
page.get(url)

while 1:
    # wait 30 seconds
    time.sleep(30)

    # refresh page, wait 2 seconds, then click button
    page.refresh()
    time.sleep(2)
    print 'clicking'
    page.find_element_by_class_name('button').click()
