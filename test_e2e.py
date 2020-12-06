import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage

#@pytest.mark.usefixtures('setup')
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info('getting all the card titles')

        products = checkOutPage.getCardTitles()
        for _ in products:
            product_Name = checkOutPage.productName
            log.info(product_Name)
            if product_Name == 'Blackberry':
                checkOutPage.getCardFooter().click()

        checkOutPage.getCheckOutbutton().click()

        confirmPage = checkOutPage.getConfirmButton()
        log.info('Entering country name as ind')
        confirmPage.getCountry().send_keys('ind')

        self.verifyLinkPresence('India')

        confirmPage.getselectCountry().click()
        confirmPage.getclickCountry().click()

        confirmPage.getsubmitbutton().click()
        success_text = confirmPage.getassertmsg().text
        log.info('Text received from application is '+success_text)
        assert 'Success' in success_text