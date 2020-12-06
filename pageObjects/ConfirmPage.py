from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, 'country')
    selectCountry = (By.LINK_TEXT, "India")
    clickCountry = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitbutton = (By.CSS_SELECTOR, "[type='submit']")
    assertmsg = (By.CLASS_NAME, 'alert-success')

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getselectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def getclickCountry(self):
        return self.driver.find_element(*ConfirmPage.clickCountry)

    def getsubmitbutton(self):
        return self.driver.find_element(*ConfirmPage.submitbutton)

    def getassertmsg(self):
        return self.driver.find_element(*ConfirmPage.assertmsg)
    
    