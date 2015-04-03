# This script pushes the attack button every 20 seconds on
# Kriegersathome page and uses splinter for web automation

from splinter import Browser
import time

with Browser() as page:
    url = 'http://algersoft.net/kriegerathome/'
    page.visit(url)

    while 1:
        # wait 30 sec, refresh page, wait 2 more seconds
        time.sleep(30)
        page.reload()
        time.sleep(2)

        # click the attack button
        button = page.find_by_id('worker_action')
        print 'click!'
        button.click()


