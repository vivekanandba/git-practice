from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    cardFooter = (By.XPATH, "div/button")
    CheckOutbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirmbutton = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getProductName(self):
        return self.driver.find_element(*CheckoutPage.productName)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckOutbutton(self):
        return self.driver.find_element(*CheckoutPage.CheckOutbutton)

    def getConfirmButton(self):
        self.driver.find_element(*CheckoutPage.confirmbutton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
    
    