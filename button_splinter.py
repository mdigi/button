# This script pushes the attack button every 20 seconds on
# Kriegersathome page and uses splinter for web automation

from splinter import Browser
import time

def attack(page):
    """
    Helper function to try and push the attack button. If the page has not
    refreshed, then wait and keep trying.
    """
    while 1:
        try:
            button = page.find_by_id('worker_action')
            button.click()
            break
        except:
            page.reload()
            time.sleep(3)
            print 'waiting for page to refresh'

def push_button():
    """
    Navigate to kriegerathome and push the attack button every 30 seconds
    """
    with Browser() as page:
        url = 'http://algersoft.net/kriegerathome/'
        page.visit(url)

        while 1:
            # wait 30 sec, refresh page, wait 2 more seconds
            time.sleep(30)
            page.reload()
            time.sleep(2)

            # click the attack button
            attack(page)
            print 'click!'

push_button()