import pytest
import time
import random
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

@pytest.fixture(scope="function")
def driver():
    print('\nStart browser...')        
    driver = webdriver.Firefox(profile)

    yield driver
    print("\nquit browser..")
    driver.quit()