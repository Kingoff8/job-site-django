from selenium.webdriver.common.by import By


class HhRuLocators:

    START_LINK = 'https://hh.ru/search/vacancy?st=searchVacancy&text=&specialization=1&area=1020&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=5&no_magic=true&L_save_area=true'
    LIST_LINKS = (By.CSS_SELECTOR, 'a[data-qa=vacancy-serp__vacancy-title]')
    TITLE = (By.TAG_NAME, 'h2')
