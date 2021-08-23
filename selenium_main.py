from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import News_Scraper
import time
import requests

class SeleniumMain:
    def selenium_main(self):
        options = Options()
        options.set_headless = True
        
        driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")
        driver.get("https://myanimelist.net/news")

        get_raw_html_content = driver.page_source

        # soup = BeautifulSoup(get_raw_html_content, "html5lib")
        soup = BeautifulSoup(get_raw_html_content, "html.parser")

        # self.individual_anime_news_block = self.soup.find("div", attrs = {"class": "news-list mt16 mr8"})
        # self.individual_anime_news_image_src = self.soup.find("a", attrs= {"class": "image-link"})

        anime_news_block = soup.find("div", attrs={"class": "news-list mt16 mr8"})
        anime_news_image_src = soup.find("a", attrs= {"class": "image-link"})

        # self.news_scrape_obj = News_Scraper.AnimeNews(anime_news_block, anime_news_image_src, soup)
        self.news_scrape_obj = News_Scraper.AnimeNews()
        self.news_scrape_obj.selenium_data(anime_news_block, anime_news_image_src, soup)

        if driver:
            driver.quit()

        # self.selenium_page_refresher(self.driver)
        
    # Copy the breakdown of individual news cell code onto here. That way, removes the headache of trying to pass data from one file to another while file c gives constant errors. 
    # First make a git commit.

    def selenium_page_refresher(self, driver):
        if driver:
            time.sleep(5)
            driver.refresh()
            print("URL Refreshed.")
        
        driver.quit()

if __name__ == "__main__":
    sel_obj = SeleniumMain()
    sel_obj.selenium_main()