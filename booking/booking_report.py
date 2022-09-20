from selenium.webdriver.remote.webdriver import WebDriver  # ELEMENT NO T DRIVER
from selenium.webdriver.remote.webdriver import WebElement  # ELEMENT NO T DRIVER
from selenium.webdriver.common.by import By
import time
from prettytable.prettytable import PrettyTable


class BookingReport:
    def __init__(self, driver: WebDriver):
        self.driver = driver  # ll boxes
        self.collection = self.get_titles_rating()

    def get_titles_rating(self):
        collection = []
        hotels_cards = self.driver.find_elements(By.XPATH, '//div[@data-testid="property-card"]')
        triple = []
        price = self.driver.find_elements(By.XPATH,
                                          '//div[@data-testid="price-and-discounted-price"]/span[2]')

        rating = self.driver.find_elements(By.XPATH, '//div[@data-testid="review-score"]/div[1]')

        allnames = []
        allprices = []
        allratings = []

        # ik this is not the best way but i got bored to find better solution
        for card in hotels_cards:
            name = card.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute(
                'innerHTML')  # seems like it searchs after that elemenet
            allnames.append(name)
        for p in price:
            allprices.append(p.get_attribute('innerHTML'))

        for r in rating:
            allratings.append(r.get_attribute('innerHTML'))

        for _ in range(len(price)):
            collection.append([allnames[_], allprices[_].strip().split(';')[1], allratings[_]])

        return collection

    def print_report(self):
        table = PrettyTable(field_names=['name', 'price', 'rating'])
        table.add_rows(self.collection)
        print(table)

