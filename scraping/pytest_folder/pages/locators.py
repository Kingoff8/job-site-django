from selenium.webdriver.common.by import By


class HhRuLocators:
    START_LINK = 'https://hh.ru/search/vacancy?search_period=1&schedule=remote&clusters=true&specialization=1&no_magic=true&items_on_page=5&order_by=publication_time&enable_snippets=true'
    LIST_LINKS = (By.CSS_SELECTOR, 'a[data-qa=vacancy-serp__vacancy-title]')
    TITLE = (By.TAG_NAME, 'h2')
