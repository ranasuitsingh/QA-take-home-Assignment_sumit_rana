from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import traceback
import time
import sys
sys.path.append('..')
from screenShot import ScreenShot

class SeleniumCommon():
    
    ''' Class containing Selenium methods to setup the browser drivers.
    '''
    def __init__(self, driver, logger):
        
        self.driver = driver
        self.logger = logger
        self.scrShot = ScreenShot(self.driver, self.logger)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tagname":
            return By.TAG_NAME
        else:
            self.logger.error("Locator type " + locatorType +" not correct/supported")
        return False

    def getElement(self, locator, locatorType="xpath"):
        """
        This method will find the element of given locator.
        Arguments: Locator and locator type of the element.
        Returns: returns element if element found otherwise return None
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.logger.info("Element Found with locator: " + locator +" and  locatorType: " + locatorType)
        except Exception, ex:
            self.logger.exception("Element not found with locator: " + locator +" and  locatorType: " + locatorType)
            self.scrShot.screen_shot(locator)
            self.logger.error(traceback.format_exc())
        return element
        

    def elementRightClick(self, locator, locatorType="XPATH"):
        """
        This method will right click operation on an element.
        Arguments: Locator and locator type of the element.
        Returns: returns 0 if right clicked otherwise return 1
        """
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            if element == None:
                return 1
            self.logger.info("Element is {}".format(element))
            self.logger.debug("Element Found with locator: " + locator +" and  locatorType: " + locatorType)
            self.logger.info("prforming right click operation on locator: "+ locator)
            time.sleep(1)
            ActionChains(self.driver).context_click(element).perform()
            return 0
        except Exception, ex:
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1

    def elementClick(self, locator, locatorType="xpath"):
        """
        This method will click on the element of locator.
        Arguments: Locator and locator type of the element.
        Returns: returns 0 if element clicked otherwise return 1
        """
        try:
            element = self.getElement(locator, locatorType)
            if element == None:
                return 1
            self.logger.info("Element is {}".format(element))
            time.sleep(1)
            element.click()
            self.logger.info("Clicked on element with locator: " + locator +" locatorType: " + locatorType)
            return 0
        except Exception, ex:
            self.logger.exception("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            self.logger.error(traceback.format_exc())
            return 1
    def executescript(self,value , element):
        try:
            self.driver.execute_script("arguments[0].setAttribute('value', "+value+")", element)
            return 0
        except Exception, ex:
            self.logger.exception("Failed to excute the script ")
            self.scrShot.screen_shot(locator)
            self.logger.error(traceback.format_exc())
        return element

    def clearText(self, locator, locatorType="xpath"):
        """
        This method will clear the textbox of the locator.
        Arguments: Locator and locator type of the element.
        Returns: returns 0 if text box cleared otherwise return 1
        """
        try:
            element = self.getElement(locator, locatorType)
            if element == None:
                return 1
            time.sleep(1)
            element.clear()
            self.logger.info("Cleared data on element with locator: " + locator +" locatorType: " + locatorType)
            return 0
        except Exception, ex:
            self.logger.info("Cannot clear data on the element with locator: " + locator + " locatorType: " + locatorType)
            self.logger.error(traceback.format_exc())
            return 1
        
    def sendKeys(self, data, locator, locatorType="xpath"):
        """
        This method will send keyword in the text box location.
        Arguments: Locator and locator type of the element.
        Returns: returns 0 if key entered successfully otherwise return 1
        """
        try:
            element = self.getElement(locator, locatorType)
            if element == None:
                return 1
            time.sleep(1)
            element.send_keys(data)
            self.logger.info("Sent data on element with locator: " + locator +" locatorType: " + locatorType)
            return 0
        except:
            self.logger.exception("Cannot send data on the element with locator: """ + locator + " locatorType: " + locatorType)
            self.logger.error(traceback.format_exc())
            return 1

    def mouseover(self, locator, locatorType="xpath"):
        """
        This method move mouse pointer over on the view menu.
        Arguments: Locator and locator type of the element.
        Returns: returns the hover to perform action
        """
        try:
            self.logger.debug("Inside the seleniumCommon page........")
            element_to_hover_over = self.getElement(locator, locatorType)
            if element_to_hover_over == None:
                return 1
            time.sleep(1)
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            self.logger.debug("mouse over on element: "+str(element_to_hover_over))
            hover.perform()
            time.sleep(2)
            self.driver.implicitly_wait(20)
            return 0
        except Exception, ex:
            self.logger.error("mouseover not performed!!!!!!!!")
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1
        

    def tearDown(self):
        """
        This method can be use for close browser.
        """
        try:
            self.logger.debug("closing browser################################")
            self.driver.quit()
        except Exception, ex:
            self.logger.error("Not able to close the window!!!!!!!")
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1

    def isElementPresent(self, locator, locatorType="xpath"):
        """
        This method will check whether element is present on the browser page or not.
        Arguments: Locator and locator type of the element.
        Returns: returns 0 if element is present otherwise return 1
        """
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.logger.info("Element Found")
                return 0
            else:
                self.logger.info("Element not found")
                return 1
        except Exception, ex:
            self.logger.error("exception found in finding element!!!!!!!!")
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1

    def getElementslist(self, locator, locatorType="xpath"):
        """
        This method will get the list of the elements.
        Arguments: Locator and locator type of the element.
        Returns: returns the element list otherwise 1
        """
        elementsList = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementsList = self.driver.find_elements(byType, locator)
            self.logger.info("Elements Found with locator: " + locator +" and  locatorType: " + locatorType)
        except Exception, ex:
            self.logger.error("Element not found with locator: " + locator +" and  locatorType: " + locatorType)
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1
        
        return elementsList

    def getText(self, locator, locatorType="xpath"):
        """
        This method will find out the text of the element for given location.
        Arguments: locator of the element and locator type.
        Returns: text of the element if found otherwise returns 1.
        """
        try:
            element = self.getElement(locator, locatorType)
            if element == None:
                return None
            if element.text == '':
                return None
            return element.text
            
        except Exception, ex:
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1

    def tablist(self, key):

        """
        This method will return specific windows tab.
        Arguments: windows tab keyword.
        Returns: returns tab object if element is present otherwise return 1
        """
        try:
            all_tabs = self.driver.window_handles
            for tab in all_tabs:
                if key in tab:
                    return tab
        except Exception, ex:
            self.logger.error("Failed to get the list of tabs")
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1

    def windowstabswitch(self, tab):

        """
        This method will switch to specific windows tab.
        Arguments: windows tab obj.
        Returns: returns 0 object if element is present otherwise return 1
        """
        try:
            self.driver.switch_to.window(tab)
            return 0
        except Exception, ex:
            self.logger.error("frame switch not performed!!!!!!!!")
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1

    def sendKeysAlert(self, inputVal):

        """
        This method will send key to alert pop up.
        Arguments: windows tab obj.
        Returns: returns 0 object if element is present otherwise return 1
        """
        try:
            alert = self.driver.switch_to_alert()
            alert.send_keys(inputVal)
            return 0
        except Exception:
            self.logger.error("Failed to send Data to Alert!!!!")
            self.logger.error(traceback.format_exc())
            return 1
