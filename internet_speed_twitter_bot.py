from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:/Users/robertp/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
url = "https://twitter.com/home"
email = "robertp@papint.school.nz"
password = "#rrRRPWP5916"
username = "@pether_robert"


class InternetSpeedTwitterBot:
    def __init__(self):
        # load twitter
        driver.get(url)
        time.sleep(3)
        # Give email
        self.email_input = driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]').send_keys(email)
        time.sleep(0.5)
        self.next_button = driver.find_element(By.CSS_SELECTOR, 'div[class="css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]').click()
        time.sleep(1)
        try:
            # Twitter usually identifies actions as suspicious - so requires username
            driver.find_element(By.CSS_SELECTOR,
                                                 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]').send_keys(username)
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR,
                                                  'div[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr"]').click()
            # sometimes username not required
        except NoSuchElementException:
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR,
                                                 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]').send_keys(password)
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR,
                                                  'div[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]').click()
        else:
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]').send_keys(password)
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR, 'div[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]').click()

    def send_tweet(self, tweet_text):
        time.sleep(5)
        print(tweet_text)
        driver.find_element(By.CSS_SELECTOR,
                                              'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys(tweet_text)
        driver.find_element(By.CSS_SELECTOR, 'div[class="css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"]').click()
