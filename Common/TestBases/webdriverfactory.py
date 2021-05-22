
"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
import sys
sys.path.append('..')
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class WebDriverFactory():
    ''' Class containing Selenium methods to setup the browser drivers.
    '''
    def __init__(self, browser, host, logger):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.logger = logger
        self.host = host
        
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the self.browser configuration

        Returns:
            'WebDriver Instance'
        """
        try:
            self.logger.debug("Inside the webdriver factory.........")
            baseURL = self.host
            self.logger.debug("opening zrs reporting console (8443 page) ")
    
            if self.browser == "iexplorer":
                # Set ie driver
                driver = webdriver.Ie('C:\Users\Administrator\Downloads\IEDriverServer_Win32_3.4.0\IEDriverServer.exe')
                self.logger.debug("opening Internet Exploral self.browser####### ")
            elif self.browser == "chrome":
                # Set chrome driver
                driver = webdriver.Chrome('C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe')
                self.logger.debug("opening Google Chrome self.browser####### ")
            else:
                browser_profile = webdriver.FirefoxProfile()
                browser_profile.set_preference("browser.download.folderList", 2)
                browser_profile.set_preference("browser.download.manager.showWhenStarting", False)
                browser_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-compressed;application/x-zip-compressed;application/zip;multipart/x-zip")
                driver = webdriver.Firefox(browser_profile)
                self.logger.debug("opening firefox self.browser")
            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(40)
            # Maximize the window
            driver.maximize_window()
            # Loading self.browser with App URL
            driver.get(baseURL)
            return driver
        except Exception, ex:
            self.logger.exception("exception" + ex.message)
            self.logger.error(traceback.format_exc())
            return 1

    