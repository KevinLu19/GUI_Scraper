import requests
import collections
import time
# import Notifier

from bs4 import BeautifulSoup

class AnimeNews:
    def __init__(self):
        self.url = "https://myanimelist.net/news"
        self.request = requests.get(self.url)
        self.get_raw_html_content = self.request.content
        self.soup = BeautifulSoup(self.get_raw_html_content, "html5lib")
        self.html_prettify = self.soup.prettify()
        self.individual_anime_news_block = self.soup.find("div", attrs = {"class": "news-list mt16 mr8"})
        self.individual_anime_news_image_src = self.soup.find("a", attrs= {"class": "image-link"})
        # self.individual_anime_news_block = self.soup.find("p", attrs = {"class": "title"})

        # self.individual_anime_news_cell()
        
    def individual_anime_news_cell(self):
        # Lists to store anime url, title, and the text of scraped data.
        anime_href = []
        news_title = []
        news_body = []

        for item in self.individual_anime_news_block.find_all("p", attrs = {"class" : "title"}):
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

        # print(self.list_mapping_into_one_list_entry(url_of_anime_news, new_title_of_anime_news, news_body))

        one_anime_list = self.list_mapping_into_one_list_entry(anime_href, news_title, news_body)

        deque_first_entry_of_list = self.list_entry_dequeue(one_anime_list)

        # Prints latest anime news.
        for item in deque_first_entry_of_list:
            print (item)
            
        # self.get_deque_data(deque_first_entry_of_list)


        # self.print_program_asleep()
        # self.individual_anime_news_cell()

        return deque_first_entry_of_list

    def list_mapping_into_one_list_entry(self, list1, list2, list3):
        return list(map(lambda x,y,z: [x,y,z], list1, list2, list3))
        
    def list_entry_dequeue(self, anime_list):
        convert_to_queue = collections.deque(anime_list)
         
        return convert_to_queue.popleft()

    def get_deque_data(self, deque_list):
        for item in deque_list:
            return item

    def get_anime_image(self):

        return self.individual_anime_news_image_src.find("img")["src"]

    def print_program_asleep(self):
        # print("---------------------------------------------------------------")
        # time.sleep(3600)
        time.sleep(60)

if __name__ == "__main__":
    news = AnimeNews()
    news.get_anime_image()