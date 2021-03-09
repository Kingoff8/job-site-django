from selenium.webdriver.common.by import By


class HhRuLocators:
    START_LINK = 'https://hh.ru/search/vacancy?search_period=1&schedule=remote&clusters=true&specialization=1&no_magic=true&items_on_page=2&order_by=publication_time&enable_snippets=true'
    LIST_LINKS = (By.CSS_SELECTOR, 'a[data-qa=vacancy-serp__vacancy-title]')
    TITLE = (By.CSS_SELECTOR, 'h1[data-qa=vacancy-title]')
    EXPERIENCE = (By.CSS_SELECTOR, 'span[data-qa=vacancy-experience')
    DESCRIPTION =(By.CSS_SELECTOR, 'div[data-qa=vacancy-description')
    CITY_LOC = (By.CSS_SELECTOR, 'p[data-qa=vacancy-view-location]')
    CITY_ADDR = (By.CSS_SELECTOR, 'span[data-qa=vacancy-view-raw-address]')
    MONEY = (By.CSS_SELECTOR, 'span[data-qa=bloko-header-2]')