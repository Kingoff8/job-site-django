import time
from pages.locators import HhRuLocators


def test_hh_ru(driver):

    #link = 'https://юзерагент.рф'
    driver.get(HhRuLocators.START_LINK)
    time.sleep(1)
    print(driver.page_source)
    title = driver.find_element(*HhRuLocators.TITLE).text
    print(title)