import time
from pages.hh_ru import HhRuScrap


def test_hh_ru(driver,request):
    site =  request.config.getoption('site')
    print('\n', site)
    if site == 'hh':
        from pages.locators import HhRuLocators as Locators
    else:
        from pages.locators import other_site_Locators as Locators
        return Locators


    #link = 'https://юзерагент.рф'
    # driver.get(Locators.START_LINK)
    # time.sleep(1)
    # print(driver.page_source)
    # title = driver.find_element(*Locators.TITLE).text
    # print(title)
    page = HhRuScrap(driver)
    #page.import_class(site)
    page.open(Locators)
    page.pars_vacancy(Locators)
    # list_links = page.get_list()
    # page.extract_vacancy(driver, list_links)

    #driver.get(HhRuLocators.START_LINK)
    time.sleep(1)
    #print(driver.page_source)
    
    #print(title)
