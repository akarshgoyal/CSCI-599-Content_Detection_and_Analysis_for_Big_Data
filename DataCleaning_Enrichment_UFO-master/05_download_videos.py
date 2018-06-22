import os
import time
import http
import urllib.request
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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


def download_video(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    # ignore large videos
    if int(r.headers['Content-length']) > 15 * 1024 * 1024:
        print('Too large, skipped.')
        return
    with open('data/videos/' + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:f.write(chunk)

start = 15

def main():
    global start, cur, driver
    #setup_driver()
    #start_driver()
    #activate_vpn()
    retries = 0
    with open('video_urls.txt', 'r') as f:
        urls = f.readlines()
    for url in urls[start:]:
        url = url.rstrip('\n')
        print("Current url", start + cur, url)
        try:
            #print('doing driver.get')
            #driver.get(url)
            #print('done driver.get')
            #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/video')))
            #print('found video xpath')
            download_video(url)
            # video_name = url.split('/')[-1]
            # urllib.request.urlretrieve(url, 'data/videos/' + video_name)
            cur += 1
        except TimeoutException as e:
            print('timedout: ', str(e))
            continue
    #driver.close()


if __name__ == "__main__":
    main()
