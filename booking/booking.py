import booking.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from booking.filteration import Filteration
from booking.booking_report import BookingReport

# service = Service(executable_path=const.DRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=opts)

class Booking(
    webdriver.Chrome):  # inheritance, every object of this class is itself  a driver...............         THIS TOO WITHOUT THE () seems like u just inherit here dont fk with the args

    def __init__(self, driver_path=const.DRIVER_PATH, service=Service(executable_path=const.DRIVER_PATH),
                 tear_down=False):
        self.tear_down = tear_down
        self.driver_path = driver_path
        self.service = service
        super().__init__(
            service=service)  # this shit is for the Daddy class Chrome # THIS TOOK ME FKING LONG TOME TO ACKNOWLEDGE GET BACK TO SEC 3 TO UNDERSTAND
        self.maximize_window()
        self.implicitly_wait(30)

        # the idea is that we pass the service thing to the parent class(chrome) for each object

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency="EUR"):
        self.implicitly_wait(30)

        currency_button = self.find_element(By.XPATH, '//button[@data-tooltip-text="Choose your currency"]')
        currency_button.click()
        select_currency_btn = self.find_element(By.CSS_SELECTOR,
                                                f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        # this * added cuz the atrb we chose has substring and we chose this part notice the ;& stuff

        select_currency_btn.click()

    def select_place(self, place='Ramallah'):
        self.implicitly_wait(30)

        place_field = self.find_element(By.ID, 'ss')
        place_field.clear()
        place_field.send_keys(f'{place}')
        first_in_list = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_in_list.click()

    def select_date(self, check_in="2022-09-22", check_out="2022-10-11"):
        self.implicitly_wait(30)
        in_date = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in}"]')
        in_date.click()
        out_date = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out}"]')
        out_date.click()

    def select_members(self, target_num=7):
        self.implicitly_wait(30)

        members_button = self.find_element(By.ID, 'xp__guests__toggle')
        members_button.click()
        current_num = self.find_element(By.ID, 'group_adults')

        dec_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
        inc_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')

        while True:
            current_num2 = current_num.get_attribute('value')  # will return current num

            if int(current_num2) == 1:
                break

            dec_button.click()

        for i in range(target_num - 1):
            inc_button.click()

    def click_search(self):

        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def exit_shit(self):
        self.implicitly_wait(3)
        try:
            x_btn = self.find_element(By.XPATH, '//button[@aria-label="Dismiss sign in information."]')
            x_btn.click()
        except:
            print('X not found')

    def do_filteration(self):
        filter_obj = Filteration(driver=self)
        filter_obj.set_star_rating(4)
        filter_obj.sort_by_lowest()

    def report(self):
        hotels_cards = self.find_elements(By.XPATH,'//div[@data-testid="property-card"]')
        rep = BookingReport(hotels_cards)
        rep.get_titles()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tear_down:
            self.quit()
