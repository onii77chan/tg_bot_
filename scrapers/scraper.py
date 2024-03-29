import requests
from parsel import Selector


class Scraper:

    TITLE_XPATH = '//div[@class="title d-md-none"]/text()'
    URL = "https://readmanga.live/"

    HEADERS = {
        "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    def scrape_data(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        link = tree.xpath(self.TITLE_XPATH).getall()
        filtered_list = [item for item in link if item.strip()]
        return filtered_list[0:5]


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape_data()

