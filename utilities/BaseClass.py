import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import inspect

@pytest.mark.usefixtures('setup')
class BaseClass:
    
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver,7)
        element = wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))
        return element

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
        return sel

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile1.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler) #filehandler object
        logger.setLevel(logging.INFO)

        return logger