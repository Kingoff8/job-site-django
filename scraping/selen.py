import time
import random
import csv

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# отключаем голову браузера
opt = Options()
opt.add_argument('-headless')

# random user agent
r_user_agent = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36", 
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36", 
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36", 
                "Mozilla/5.0 (Windows NT 6.1; rv:83.0) Gecko/20100101 Firefox/83.0",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320"]
r_user_agent = random.choice(r_user_agent)


# передача user agent
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", r_user_agent)

driver = webdriver.Firefox(profile, options=opt)

# настройки для Chrome

# from selenium.webdriver.chrome.options import Options

# opts = Options()
# opts.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 YaBrowser/20.11.3.268 (beta) Yowser/2.5 Safari/537.36')

# browser = webdriver.Chrome(chrome_options=opts)

# функция сохранения данных в csv

def write_csv(table_0):
    with open("table_vacancy.csv", mode="w", encoding='utf-8') as w_file:
        names = ["Заголовок", "Описание"]
        file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                    lineterminator="\r", fieldnames=names)
        file_writer.writeheader(table_0)

link = 'https://hh.ru/search/vacancy?st=searchVacancy&text=&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=2&no_magic=true&L_save_area=true'

#link = 'https://юзерагент.рф'
try:
    r = driver.get(link)
    list_links = driver.find_elements_by_css_selector('a[data-qa=vacancy-serp__vacancy-title]')
    list_for_save = []
    print(len(list_links))

    n = 0
    # извлекаем ссылки из списка
    for link in list_links: 
        link.click()
        time.sleep(5)

        # список окон
        print(driver.window_handles)

        n += 1
        print('id_w:', n)

        new_tab = driver.window_handles[n]

        print(new_tab)
        driver.switch_to.window(new_tab)
        
        # get field vacancy
        try:
            title = driver.find_element_by_css_selector('h1[data-qa=vacancy-title]')
            print(title.text)
            experience = driver.find_element_by_css_selector('span[data-qa=vacancy-experience')
            print(experience.text)
            description = driver.find_element_by_css_selector('div[data-qa=vacancy-description')
            print(description.text)
            #print(driver.page_source)

            try:
                city = driver.find_element_by_css_selector('p[data-qa=vacancy-view-location]')
            except:
                city = driver.find_element_by_css_selector('span[data-qa=vacancy-view-raw-address]')

            table_0 = {
                'title': title.text,
                'experience': experience.text,
                'description': description.text
            }
            
                
            print(city.text)
            money = driver.find_element_by_css_selector('span[data-qa=bloko-header-2]')
            print(money.text)
        except:
            f = open('source_page_hh_ru.html', 'w')
            f.write(driver.page_source)
            f.close()


        # sitch to main window
        main_window = driver.window_handles[0]
        driver.switch_to.window(main_window)        

# ниже не раскомент

    # page = driver.page_source
    with open("table_vacancy.csv", mode="w", encoding='utf-8') as w_file:
        names = ["Заголовок", "Описание"]
        file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                    lineterminator="\r", fieldnames=names)
        file_writer.writeheader(table_0)
    

finally:
    time.sleep(1)
    driver.quit()