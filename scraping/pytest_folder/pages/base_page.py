from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        #self.url = url
        self.driver.implicitly_wait(timeout)


