import os
import time
import http

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

count404 = 0
cur, end = 76225, 81000
driver = None
chrome_options = None
imageFile = 'imageurls.txt'


def get_elements(pageNo):
    global driver
    elements = driver.find_elements_by_css_selector('td.ng-scope')
    i = 1
    for anchorTag in elements:
        href = anchorTag.find_elements_by_css_selector('a')
        with open(imageFile, 'a+') as f:
            f.write(str(href[0].get_attribute("href")) + '\n')


def setup_driver():
    global chrome_options
    chrome_options = Options()
    # chrome_options.add_extension('extension_1_2_6.crx') #anonymox
    chrome_options.add_extension('extension_1_5_13_0.crx')  # touchvpn
    chrome_options.add_extension('extension_1_15_24_0.crx')  # ublock


def start_driver():
    global driver
    driver = webdriver.Chrome(
        executable_path="chromedriver.exe", chrome_options=chrome_options)
    driver.wait = WebDriverWait(driver, 60)


def check_404(url):
    # if 10 consecutive 404s, restart
    global driver, count404, cur
    target_url = url + str(cur)
    old_cur = cur
    while True:
        if driver.current_url == 'http://www.ufostalker.com/error':
            count404 += 1
            cur += 1
            target_url = url + str(cur)
            driver.get(target_url)
            time.sleep(2)
            if count404 == 10:
                count404 = 0
                cur = old_cur
                driver.quit()
                main()
                return
        elif driver.current_url == target_url:
            return


def activate_vpn():
    ext_url = 'chrome-extension://bihmplhobchoageeokmgbdihknkjbknd/panel/panel.html'
    driver.get(ext_url)
    time.sleep(2)
    start_vpn_btn = e = driver.find_element_by_xpath(
        '//*[@id="panel"]/div/div/div[2]/div[3]/div')
    start_vpn_btn.click()
    time.sleep(2)


def main():
    global cur, end, driver
    setup_driver()
    start_driver()
    activate_vpn()
    retries = 0
    while cur <= end:
        print("Current Page", cur)
        try:
            url = 'http://www.ufostalker.com/event/'
            eventOccurence = url + str(cur)
            driver.get(eventOccurence)
            time.sleep(1)
            check_404(url)
            get_elements(cur)
            cur += 1
        # add more exceptions if you run into them
        except (http.client.RemoteDisconnected, IndexError, ConnectionResetError):
            print('Error!')
            retries += 1
            if retries >= 3:
                cur, retries = cur + 1, 0
    driver.close()


if __name__ == "__main__":
    main()
