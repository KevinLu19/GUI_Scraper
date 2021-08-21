from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import News_Scraper
import time

def selenium_main():
    options = Options()
    options.set_headless = True
    anime_news_obj = News_Scraper.AnimeNews()
    page_url = anime_news_obj.url

    driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")
    driver.get(page_url)

    selenium_page_refresher(driver)
    
    return driver

def selenium_page_refresher(driver):
    if driver:
        time.sleep(5)
        driver.refresh()
        print("URL Refreshed.")
    
    driver.quit()

if __name__ == "__main__":
    selenium_main()