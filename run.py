from booking.booking import Booking
from booking.constants import *


def main():

    with Booking() as bot:

        bot.land_first_page()
        bot.change_currency(currency="ILS")
        bot.select_place(place='New York') #by default Ramallah
        bot.select_date()
        bot.select_members(target_num=1)
        bot.click_search()
        bot.exit_shit()
        bot.do_filteration()





if __name__ == '__main__':
    main()
