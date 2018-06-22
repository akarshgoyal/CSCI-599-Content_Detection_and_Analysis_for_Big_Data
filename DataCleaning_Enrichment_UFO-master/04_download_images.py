import os
import time
import http
import urllib.request

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

cur = 0
driver = None
chrome_options = None


def setup_driver():
    global chrome_options
    chrome_options = Options()
    chrome_options.add_extension('extension_1_5_13_0.crx')  # touchvpn
    chrome_options.add_extension('extension_1_15_24_0.crx')  # ublock


def start_driver():
    global driver
    driver = webdriver.Chrome(
        executable_path="./chromedriver", chrome_options=chrome_options)

def activate_vpn():
    ext_url = 'chrome-extension://bihmplhobchoageeokmgbdihknkjbknd/panel/panel.html'
    driver.get(ext_url)
    time.sleep(2)
    start_vpn_btn = e = driver.find_element_by_xpath(
        '//*[@id="panel"]/div/div/div[2]/div[3]/div')
    start_vpn_btn.click()
    time.sleep(2)

start = 373

def main():
    global start, cur, driver
    setup_driver()
    start_driver()
    activate_vpn()
    retries = 0
    with open('image_urls.txt', 'r') as f:
        urls = f.readlines()
    for url in urls[start:]:
        url = url.rstrip('\n')
        print("Current url", start + cur, url)
        try:
            driver.get(url)
            time.sleep(1)
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/img')))
            #check_404(url)
            #get_image(url)
            image_name = url.split('/')[-1]
            urllib.request.urlretrieve(url, 'data/images/' + image_name)
            cur += 1
        # add more exceptions if you run into them
        except TimeoutException as e:
            print('timedout: ', str(e))
            continue
    driver.close()


if __name__ == "__main__":
    main()
