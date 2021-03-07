from selenium.webdriver.common.by import By

class HhRuLocators:
    START_LINK = 'https://hh.ru/search/vacancy?search_period=1&schedule=remote&clusters=true&specialization=1&no_magic=true&items_on_page=5&order_by=publication_time&enable_snippets=true'
    TITLE = (By.TAG_NAME, 'h2')
#    TITLE = ".find_elements_by_tag_name('h2')"
