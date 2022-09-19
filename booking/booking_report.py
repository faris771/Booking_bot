from selenium.webdriver.remote.webdriver import WebElement #ELEMENT NO T DRIVER
from selenium.webdriver.common.by import By
import time


class BookingReport:
    def __init__(self, boxes_container: WebElement):
        self.boxes_container = boxes_container  # ll boxes

    def get_titles(self):
        for box in self.boxes_container:
            name = box.find_element(By.CLASS_NAME,'sr_hotel__name')#//div[@data-testid="property-card"]
            print(name.get_attribute('innerHTML'))


    def print_report(self):
        pass