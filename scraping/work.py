import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'}

url = 'https://www.work.ua/ru/jobs-kyiv-python'
resp = requests.get(url, headers=headers)

if resp == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', id='pjax-job-list')
    div_list = main_div.find_all('div', attrs={'class': 'job-link'})

h = codecs.open('work.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()