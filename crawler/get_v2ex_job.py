#!/usr/bin/python3.4
import bs4
from urllib import request
import jieba
import re

meanless_str = [' ', '|', '[', ']', '/', ',', '!', '&', '）', '（']
v2ex_url = "https://www.v2ex.com"


def rm_meanless(text_list):
    for j in meanless_str:
        if j in text_list:
            text_list.remove(j)
            print("remove {0}".format(j))
    return text_list


jd_url_list = []
for page in range(10):
    page_content = request.urlopen("https://www.v2ex.com/go/jobs?p={0}".format(page))
    page_bs4 = bs4.BeautifulSoup(page_content, "html.parser")
    for job_title in page_bs4.findAll(class_='item_title'):
        job_title_list = list(jieba.cut(re.sub('[！，,&…\[\]\-\~\!\,\/（）|]+', '', job_title.get_text())))
        jd_url_raw = job_title.find('a').get('href')
        jd_url = v2ex_url + jd_url_raw
        jd_url_list.append(jd_url)
print(jd_url_list)
for url in jd_url_list:
    import time
    time.sleep(2)
    jd_content = request.urlopen(url)
    jd_bs4 = bs4.BeautifulSoup(jd_content, "html.parser")
    jd_str = jd_bs4.find(class_='topic_content')
    jd_str_filted = re.sub('<.*?>', '', str(jd_str))
    if '运维' in jd_str_filted:
        print(jd_str_filted)
