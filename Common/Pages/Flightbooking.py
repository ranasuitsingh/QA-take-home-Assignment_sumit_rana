import sys
import traceback
from Common.TestUtility.seleniumCommon import SeleniumCommon
import os, time


class SearchFlight:
    """
    -------- Locator of flight pages ---------""""""
    """
    FLIGHT_LOGO = "//span[contains(text(), 'Flights') and @class ='uitk-tab-text' ]"
    SEARCH_LEAVING_BOX = "//label[contains(text(), 'Leaving from') and @for='location-field-leg1-origin']"
    SEARCH_GOING_BOX = "//label[contains(text(), 'Going to') and @for='location-field-leg1-destination-input']"
    DEPARTING_DATE = "d1-btn"
    RETURNING_DATE = "d2-btn"
    SEARCH_BUTTON = "//button[@type='submit' and @data-testid='submit-button']"
    PRICE_OPTION = "//option[contains(text(), 'Price (Highest)')]"
    STOP_OPTION = "//span[contains(text(), 'Nonstop (')]"
    CLICK_SELECT = "//button//span[ text()='Select result 1 when sorted by price']"
    CLICK_POPUP = "No Thanks"
    FINAL_VALUE = "//article[@id='outboundFlightModule']/div/div[4]/div[2]"
    REVIEW= "odPair"


#---------Initialize the class----------------
    
    def __init__(self, driver, logger):

        self.driver = driver
        self.logger = logger
        self.selCommon = SeleniumCommon(self.driver, self.logger)

#-------Operation to search flight -------------

    def click_on_flight_logo(self):
        try:
            return self.selCommon.elementClick(self.HOME_LOGO, "xpath")
        except Exception:
            self.logger.error("Failed to click on Logo to redirect to home page!!!!")
            self.logger.error(traceback.format_exc())
            return 1

    def enter_departure(self, src):
        try:
            if self.selCommon.clearText(self.SEARCH_LEAVING_BOX, "xpath") == 0:
                return self.selCommon.sendKeys(src, self.SEARCH_LEAVING_BOX, "xpath")
            return 1
        except Exception:
            self.logger.error("Failed to fill departure !!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def enter_destination(self, dst):
        try:
            if self.selCommon.clearText(self.SEARCH_GOING_BOX, "xpath") == 0:
                return self.selCommon.sendKeys(dst, self.SEARCH_GOING_BOX, "xpath")
            return 1
        except Exception:
            self.logger.error("Failed to fill destination!!!!")
            self.logger.error(traceback.format_exc())
            return 1

    def departure_date(self, date):
        try:
            departing_date = self.selCommon.getElement(self.DEPARTING_DATE, "id")
            return self.selCommon.executescript(date, departing_date)
        except Exception:
            self.logger.error("Failed to select Departure Time !!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def returning_date(self, date):
        try:
            returning_date = self.selCommon.getElement(self.RETURNING_DATE, "id")
            return self.selCommon.executescript(date, returning_date)
        except Exception:
            self.logger.error("Failed to select Returning Time !!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def click_search_button(self):
        try:
            return self.selCommon.elementClick(self.SEARCH_BUTTON)
        except Exception:
            self.logger.error("Failed to click on Search button!!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def select_price_type(self, priceoption):
        try:
            return self.selCommon.selectDropDownVisibleText(self.PRICE_OPTION, priceoption)
        except Exception:
            self.logger.error("oops ! ,  Failed to select price type !!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def click_flight_type(self):
        try:
            return self.selCommon.elementClick(self.STOP_OPTION)
        except Exception:
            self.logger.error("Failed to select non stop flight option !!!!")
            self.logger.error(traceback.format_exc())
            return 1

    def click_select(self):
        try:
            return self.selCommon.elementClick(self.CLICK_SELECT)
        except Exception:
            self.logger.error("Failed to select the flight  !!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def click_return_select(self):
        try:
            return self.selCommon.elementClick(self.CLICK_SELECT)
        except Exception:
            self.logger.error("Failed to select the option of return  flight  !!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def handle_popup(self):
        try:
            return self.selCommon.sendKeysAlert(CLICK_POPUP)
        except Exception:
            self.logger.error("Failed to remove pop up  !!!!")
            self.logger.error(traceback.format_exc())
            return 1
        
    def switch_windows_tab(self, key):
        try:
            tab_url = self.selCommon.tablist(key)
            return self.selCommon.windowstabswitch(tab_url)

        except Exception:
            self.logger.error("Failed to switch the tab  !!!!")
            self.logger.error(traceback.format_exc())
            return 1

    def get_final_data(self):
        try:
            info_data = []
            total_info = self.selCommon.getElementslist("REVIEW", "class")
            for data in total_info:
                val = data.getText()
                info_data.append(val)
                return info_data
        except Exception:
            self.logger.error("validation failed for src and dst")
            self.logger.error(traceback.format_exc())
            return 1







