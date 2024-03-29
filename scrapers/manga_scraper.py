import requests
from parsel import Selector


class MangaScraper:

    URL = "https://mangalib.me/"
    HEADERS = {
        "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    LINK_XPATH = '//h4[@class="updates__name"]/text()'

    def scrape_data(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        # print(response.text)
        tree = Selector(text=response.text)
        link = tree.xpath(self.LINK_XPATH).getall()
        for title in link:
            print(title.strip())


if __name__ == "__main__":
    scraper = MangaScraper()
    scraper.scrape_data()

