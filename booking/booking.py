import booking.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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
        # self.maximize_window()
        self.implicitly_wait(15)

        # the idea is that we pass the service thing to the parent class(chrome) for each object

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_button = self.find_element(By.XPATH, '//button[@data-tooltip-text="Choose your currency"]')

        currency_button.click()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tear_down:
            self.quit()
