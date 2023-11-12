from bs4 import BeautifulSoup
from urllib import request


class WebScraper:
    """
    Extract data from worldometers web page.
    """
    page = "https://www.worldometers.info/coronavirus/"

    @staticmethod
    def get_covid_cases():
        """
        Get value from the current number of cases in the specified site.
        """
        with request.urlopen(WebScraper.page) as f:
            page = f.read()

        soup = BeautifulSoup(page, 'html.parser')
        value = soup.find("div", {"class": "maincounter-number"})
        value = value.find("span").get_text().replace(",", "")
        value = int(value)
        return value
