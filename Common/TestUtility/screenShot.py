
import sys
import logging
import traceback

class ScreenShot(object):

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def screen_shot(self, filename):
        try:
            self.logger.debug("Taking screenshot of current UI Page..")
            directory = "../../screenshots/"
            self.driver.get_screenshot_as_file(directory+filename+'.png')
        except Exception, ex:
            logger.exception("exception" + ex.message)
            logger.error(traceback.format_exc())
            return 1