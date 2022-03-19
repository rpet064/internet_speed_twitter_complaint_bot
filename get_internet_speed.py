from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(chrome_driver_path)
url = "https://www.speedtest.net/"


class GetInternetSpeed:
    def __init__(self):
        pass
        # load internet speed checker website
        driver.get(url)
        time.sleep(5)
        self.start_button = driver.find_element(By.CLASS_NAME, "start-button")
        self.start_button.click()
        time.sleep(75)
        # record results from speed test
        self.down = driver.find_element(By.CSS_SELECTOR,
                                        'span[class="result-data-large number result-data-value download-speed"]')
        self.up = driver.find_element(By.CSS_SELECTOR,
                                      'span[class="result-data-large number result-data-value upload-speed"]')
        self.down = self.down.text
        self.up = self.up.text


