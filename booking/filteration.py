from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class Filteration:
    def __init__(self, driver: WebDriver):  # type casting, we pass the driver and call it, then call its methods
        self.driver = driver

    def set_star_rating(self, stars):  # args
        self.driver.implicitly_wait(15)

        filteration_bar = self.driver.find_element(By.XPATH, '//div[@data-testid="filters-sidebar"]')
        children = filteration_bar.find_elements(By.CSS_SELECTOR, "*")  # takes everychild tag of the filteration bar

        for element in children:
            # inner html is like <h1> faris </h1>, faris is the innerHTML
            if str(element.get_attribute('innerHTML')).strip() == f'{stars} stars' or str(
                    element.get_attribute('innerHTML')).strip() == f'{stars} star':
                element.click()
                time.sleep(5)
                break


    def sort_by_lowest(self):
        self.driver.implicitly_wait(15)

        sorting_button = self.driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')
        sorting_button.click()
        lowest_button = self.driver.find_element(By.XPATH, '//button[@data-id="price"]')
        lowest_button.click()
