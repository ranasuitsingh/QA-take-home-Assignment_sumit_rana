import logging
import traceback
import sys
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import os 
sys.path.append('..//..//')

from Common.TestBases.webdriverfactory import WebDriverFactory
from Common.Pages.Flightbooking import SearchFlight

class FlightSearch():

    def search_flight(self, host, logger,browser):
        date1  = str(datetime.now() + timedelta(weeks=2))
        date2 = str(datetime.now() + timedelta(weeks=3))
        priceoption = "Price (Highest)"
        src = "San Francisco"
        dst = "New York"
        self.driver = WebDriverFactory(browser, host, logger).getWebDriverInstance()
        searchflight = SearchFlight(self.driver, logger)
        searchflight.click_on_flight_logo(self.driver)
        searchflight.enter_departure(self, src)
        searchflight.enter_destination(self, dst)
        searchflight.departure_date(self, date1)
        searchflight.returning_date(self, date2)
        searchflight.click_search_button(self)
        searchflight.select_price_type(self, priceoption)
        searchflight.click_flight_type(self)
        searchflight.click_select(self)
        searchflight.click_return_select(self)
        searchflight.handle_popup(self)
        searchflight.switch_windows_tab(self)
        searchflight.get_final_data(self)


def main(argv=None):
    """
    This is main function please do not modify the below code.
    """
    logging.basicConfig(filename='..//..//Logs//test_Log.txt',level=logging.DEBUG)
    logger = logging.getLogger()
    host = "https://www.orbitz.com/"
    x_f = threading.Thread(target=search_flight, args=(host,logger,"iexplorer",))
    x_f = threading.Thread(target=search_flight, args=(host,logger,"firefox",))
    x_c = threading.Thread(target=search_flight, args=(host,logger,"chrome",))

    x_f.start()
    x_c.start()
    x_i.start()
    #obj = FlightSearch()
    #res = obj.search_flight(host, logger,browser)
    sys.exit(0)

if __name__ == "__main__":
    main()