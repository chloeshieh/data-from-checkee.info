#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Yix
@description: data from checkee.info, get html table and write into .csv table file  --> for data visualization
1st version: Jul 2019
2nd version: Jul 30 2019 --> revise to table2csv (an easier way)
"""

import requests
from pyquery import PyQuery as pq


def get_page(url):
    """发起请求 获得源码"""
    r = requests.get(url)
    r.encoding = 'utf8'
    html = r.text
    return html


def parse(text):
    """解析数据 写入文件"""
    doc = pq(text)
    # 获得每一行的tr标签
    tds = doc('table[6]').items()
    for td in tds:
        rank = td.xpath('//tr[@align="center"]/td').text()
        print(rank)
        name = td.find('div').text()
        city = td.find('td:nth-child(3)').text()
        score = td.find('td:nth-child(4)').text()
    #     with open('E:\check.csv', 'a+', encoding='utf8') as f:
    #         f.write(rank + '\t\t')
    #         f.write(name + '\t\t')
    #         f.write(city + '\t\t')
    #         f.write(score + '\t\t\n')
    # print("check.csv created!")


if __name__ == "__main__":
    url = "https://www.checkee.info/main.php?dispdate=2019-06"
    text = get_page(url)
    # parse(text)
