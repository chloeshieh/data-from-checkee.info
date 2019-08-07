# coding=utf-8
import io
import sys
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码, 防止控制台打印乱码

url = "https://www.checkee.info/main.php?dispdate=2019-06"


def get_soup(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 若请求不成功,抛出HTTPError 异常
        # r.encoding = 'gbk'
        soup = BeautifulSoup(r.text, 'lxml')
        return soup
    except HTTPError:
        return "Request Error"


def saveTocsv(data, fileName):
    '''
    将checkee.info表格[6]的数据保存至csv文件
    '''
    result_weather = pd.DataFrame(data, columns=['date', 'tq', 'temp', 'wind'])
    result_weather.to_csv(fileName, index=False, encoding='gbk')
    print('Save all weather success!')


def saveToMysql(data):
    '''
    将天气数据保存至MySQL数据库
    '''
    # 建立连接
    conn = pymysql.connect(host="localhost", port=3306, user='root', passwd='root', database='test', charset="utf8")
    # 获取游标
    cursor = conn.cursor()
    
    sql = "INSERT INTO weather(date,tq,temp,wind) VALUES(%s,%s,%s,%s)"
    data_list = np.ndarray.tolist(data)  # 将numpy数组转化为列表
    try:
        cursor.executemany(sql, data_list)
        print(cursor.rowcount)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    
    cursor.close()
    conn.close()


def get_data():
    soup = get_soup(url)
    all_weather = soup.find('div', class_="wdetail").find('table').find_all("tr")
    data = list()
    for tr in all_weather[1:]:
        td_li = tr.find_all("td")
        for td in td_li:
            s = td.get_text()
            data.append("".join(s.split()))
    
    res = np.array(data).reshape(-1, 4)
    return res


if __name__ == '__main__':
    data = get_data()
    saveTocsv(data, "E:\weather.csv")
