from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import time
import collections

class SeleniumMain:
    def __init__(self):
        options = Options()
        options.headless = True

        self.driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")
        self.driver.get("https://myanimelist.net/news")

        get_raw_html_content = self.driver.page_source
        self.soup = BeautifulSoup(get_raw_html_content, "html.parser")

        self.anime_news_block = self.soup.find("div", attrs={"class": "news-list mt16 mr8"})
        self.anime_news_image_src = self.soup.find("a", attrs= {"class": "image-link"})

    def individual_anime_news_cell(self):
        # Lists to store anime url, title, and the text of scraped data.
        anime_href = []
        news_title = []
        news_body = []

        for item in self.anime_news_block.find_all("p", attrs = {"class" : "title"}):
            # Gets the URL from news
            url_of_anime_news = item.find("a")["href"]
            # Gets the title of the news
            title_of_anime_news = item.find("a").contents

            for title in title_of_anime_news:
                new_title_of_anime_news = title

            anime_href.append(url_of_anime_news)
            news_title.append(new_title_of_anime_news)

        for item in self.soup.find_all("div", attrs = {"class": "text"}):
            text_body_of_news = item.text
            news_body.append(text_body_of_news)

        return(anime_href, news_title, news_body)

    def list_mapping_into_one_list_entry(self, list1, list2, list3):
        return list(map(lambda x,y,z: [x,y,z], list1, list2, list3))
        
    def list_entry_dequeue(self, anime_list):
        convert_to_queue = collections.deque(anime_list)
         
        return convert_to_queue.popleft()

    def get_deque_data(self, deque_list):
        for item in deque_list:
            return item

    def get_anime_image(self):
        
        return self.anime_news_image_src.find("img")["src"]

    def selenium_page_refresher(self):
        while self.driver:
            time.sleep(5)
            self.driver.refresh()
            print("URL Refreshed.")

    def restart_program(self):
        pass

if __name__ == "__main__":
    sel_obj = SeleniumMain()
    print(sel_obj.get_anime_image())