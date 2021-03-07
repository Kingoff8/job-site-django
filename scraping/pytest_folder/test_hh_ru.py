import time


def test_hh_ru(driver, request):

    site =  request.config.getoption('site')
    
    if site == 'hh':
        from pages.locators import HhRuLocators as Locators
    else:
        from pages.locators import other_site_Locators as Locators

    #link = 'https://юзерагент.рф'
    driver.get(Locators.START_LINK)
    time.sleep(1)
    print(driver.page_source)
    title = driver.find_element(*Locators.TITLE).text
    print(title)