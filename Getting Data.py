# encoding^ utf-8
__author__ = '��������'


import urllib.request
import urllib

dates = []


#----------����� �������� ������ �� ��� ����������� �������, ������ ���� �������� ���� � ������ �� �������� � ��������� � �������� ������� �����������
url         = 'http://lks.fcsm.ru/publication/index.html'

with urllib.request.urlopen(url) as response:
    html = response.read()                                                                                  #bytes

page   = html.decode('windows-1251')                                                                        #string
start  = page.find("/publication/index.html?'+this.value")+59                                               #������ ������� "select", � ������� ���������� ���� �������
finish = page.find('</select>')                                                                             #����� ������� "select", � ������� ���������� ���� �������
number_of_reports = page.count('value', start, finish)                                                      #����������, ������� ������� ��������

for i in range(1, number_of_reports):                                                                       #�������� ���� �������
    start  = page.find('value', start) +7
    dates.append(page[start:(start+10)])

for i in dates:
    for ii in range(1, 10000):
        try:
            url = 'http://lks.fcsm.ru/publication/' + i + '/s1/' + str(ii) + '.zip'                         #�����!!! url ���� �������� � ����� html, ������ ��� �� � ��� ��������
            file_name   = i + '_' + str(ii) + '.zip'
            urllib.request.urlretrieve(url, file_name)
        except:
            continue












