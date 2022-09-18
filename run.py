from booking.booking import Booking
from booking.constants import *


def main():

    with Booking(tear_down=False) as bot:

        bot.land_first_page()
        bot.change_currency(currency="ILS")
        bot.select_place() #by default Ramallah
        bot.select_date()
        bot.select_members(target_num=1)
        bot.click_search()




if __name__ == '__main__':
    main()
