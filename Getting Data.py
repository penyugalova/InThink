# encoding^ utf-8
__author__ = 'аналитик'


import urllib.request
import urllib

dates = []


#----------здесь хранятся ссылки на все последующие балансы, отсюда надо вытащить даты и ссылки на страницу с балансами и сводными данными объединений
url         = 'http://lks.fcsm.ru/publication/index.html'

with urllib.request.urlopen(url) as response:
    html = response.read()                                                                                  #bytes

page   = html.decode('windows-1251')                                                                        #string
start  = page.find("/publication/index.html?'+this.value")+59                                               #начало раздела "select", в котором выбираются даты отчетов
finish = page.find('</select>')                                                                             #конец раздела "select", в котором выбираются даты отчетов
number_of_reports = page.count('value', start, finish)                                                      #определяем, сколько отчетов выложено

for i in range(1, number_of_reports):                                                                       #выбираем даты отчетов
    start  = page.find('value', start) +7
    dates.append(page[start:(start+10)])

for i in dates:
    for ii in range(1, 10000):
        try:
            url = 'http://lks.fcsm.ru/publication/' + i + '/s1/' + str(ii) + '.zip'                         #ВАЖНО!!! url надо находить в самом html, потому что он у них меняется
            file_name   = i + '_' + str(ii) + '.zip'
            urllib.request.urlretrieve(url, file_name)
        except:
            continue












