from twython import Twython
import unittest
from selenium import webdriver
from time import sleep
import datetime 
import csv
import os
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class QuotesScraper():

    def __init__(self, URL):
        PATH = "C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver.exe"
        # self.driver = webdriver.Chrome(executable_path = PATH) 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get(URL)
        driver.implicitly_wait(30) 
        driver.maximize_window()

    def quotes_scrape(self):
        driver = self.driver 
        quotes, authors = [], []
        for i in range(1,11):
            try:
                quotes.append(driver.find_element_by_xpath(f'/html/body/div/div[2]/div[1]/div[{i}]/span[1]').text)
                authors.append(driver.find_element_by_xpath(f'/html/body/div/div[2]/div[1]/div[{i}]/span[2]/small').text)
            except:
                pass
        return quotes, authors 


    def change_page(self):
        quotes, authors = [], []
        while True:
            try:
                self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/nav/ul/li[2]/a').click()        
                temp_1, temp_2 = self.quotes_scrape()
                quotes.extend(temp_1)
                authors.extend(temp_2)
                sleep(3)
            except:
                return quotes, authors
                break
        return quotes, authors

    def finish_bot(self):
        self.driver.quit()

def main():

    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    URL = "https://quotes.toscrape.com/page/3/"
    scraper = QuotesScraper(URL)
    # quotes, authors = scraper.quotes_scrape()
    quotes, authors = scraper.change_page()
    validacion = True

    for i, j in zip(quotes, authors): 
        message = str(i) + " " + str(j)
        try:
            twitter.update_status(status=message)
            print('Tweeted: {0}'.format(message))
            sleep(5)
        except:
            pass

    scraper.finish_bot()

if __name__ == '__main__':
    main()


