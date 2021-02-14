import time
from pages.locators import HhRuLocators
from pages.hh_ru import HhRuScrap


def test_hh_ru(driver):

    link = HhRuLocators.START_LINK
    page = HhRuScrap(driver, link)
    page.open()
    page.pars_vacancy()
    # list_links = page.get_list()
    # page.extract_vacancy(driver, list_links)

    #driver.get(HhRuLocators.START_LINK)
    time.sleep(1)
    #print(driver.page_source)
    
    #print(title)