from booking.booking import Booking
from booking.constants import *


with Booking(tear_down=False) as bot:
    bot.land_first_page()
    bot.change_currency()


