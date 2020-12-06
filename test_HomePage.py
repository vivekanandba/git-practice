import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info('First name is'+getData['firstname'])
        homepage.getName().send_keys(getData['firstname'])
        homepage.getEmail().send_keys(getData['lastname'])
        homepage.getCheck().click()
        self.selectOptionByText(homepage.getGender(),getData['gender'])
        homepage.getSubmit().click()
        alertText = homepage.getSuccessMessage().text
        assert ('Success' in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData('Testcase2'))
    def getData(self, request):
        return request.param
