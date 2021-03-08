import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import pytest
#from pages.locators import HhRuLocators as Locators

class HhRuScrap(BasePage): 


    def open(self, Locators):
        print('2: ', Locators)
        link = Locators.START_LINK
        print(link)
        self.driver.get(link)

    def pars_vacancy(self, Locators):
        self.get_list(Locators)
        self.extract_vacancy()

    def get_list(self, Locators):
        self.list_links = self.driver.find_elements(*Locators.LIST_LINKS)
        #return list_links
        assert self.list_links != None

    
    def extract_vacancy(self):
        n = 0
        #извлекаем ссылки из списка
        for self.link in self.list_links: 
            self.link.click()
            time.sleep(5)

            # список окон
            print(self.driver.window_handles)

            n += 1
            print('id_w:', n)

            new_tab = self.driver.window_handles[n]

            print(new_tab)
            self.driver.switch_to.window(new_tab)
            
            # get field vacancy
            try:
                title = self.driver.find_element_by_css_selector('h1[data-qa=vacancy-title]')
                print(title.text)
                experience = self.driver.find_element_by_css_selector('span[data-qa=vacancy-experience')
                print(experience.text)
                description = self.driver.find_element_by_css_selector('div[data-qa=vacancy-description')
                print(description.text)
                #print(driver.page_source)

                try:
                    city = self.driver.find_element_by_css_selector('p[data-qa=vacancy-view-location]')
                except:
                    city = self.driver.find_element_by_css_selector('span[data-qa=vacancy-view-raw-address]')

                print(city.text)
                money = self.driver.find_element_by_css_selector('span[data-qa=bloko-header-2]')
                print(money.text)
            except:
                f = open('source_page_hh_ru.html', 'w')
                f.write(self.driver.page_source)
                f.close()


            # sitch to main window
            main_window = self.driver.window_handles[0]
            self.driver.switch_to.window(main_window)
    
