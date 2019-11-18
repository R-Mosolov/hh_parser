import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}

base_url = 'https://kazan.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=Frontend&area=1&from' \
           '=cluster_area&showClusters=false '


def hh_parse(base_url, headers):
    session = requests.session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        items = soup.find_all('div', attrs={'class': 'vacancy-serp-item'})

        for item in items:
            vacancy_title = item.find('a', attrs={'class': 'bloko-link'}).text
            vacancy_link = item.find('a', attrs={'class': 'bloko-link'})['href']
            salary = item.find('div', attrs={'class': 'vacancy-serp-item__compensation'}).text
            vacancy_responsibility = item.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            vacancy_requirement = item.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            resp_and_req = vacancy_responsibility + ' ' + vacancy_requirement
            print(resp_and_req)

    else:
        print('ERROR')


hh_parse(base_url, headers)
