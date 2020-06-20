#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

CityCode = {'가평군':'41820', '고양시':'41280', '과천시':'41290', '광명시':'41210', '광주시':'41610',
            '구리시':'41310', '군포시':'41410', '김포시':'41570', '남양주시':'41360', '동두천시':'41250',
            '부천시':'41190', '성남시':'41130', '수원시':'41110', '시흥시':'41390', '안산시':'41270',
            '안성시':'41550', '안양시':'41170', '양주시':'41630', '양평군':'41830', '여주시':'41670',
            '연천군':'41800', '오산시':'41370', '용인시':'41460', '의왕시':'41430', '의정부시':'41150',
            '이천시':'41500', '파주시':'41480', '평택시':'41220', '포천시':'41650', '하남시':'41450', '화성시':'41590'}

KEY = "KEY=de547a5cf35444bb9e49043ce00f4115"
TOKEN = '1169278266:AAFVc9DInhRyYXZ8z-qJeGk7SpG9ugYb5BE'
MAX_MSG_LENGTH = 100
baseurl = "https://openapi.gg.go.kr/PlaceThatDoATasteyFoodSt?KEY=de547a5cf35444bb9e49043ce00f4115&SIGUN_CD="
bot = telepot.Bot(TOKEN)

def getData(cityCode):
    res_list = []
    #print('-------------------')
    #print(cityCode)
    if CityCode.get(cityCode) is None:
        return
    else:
        url = baseurl + CityCode.get(cityCode)
        #print(CityCode.get(cityCode))
        #print(url)
        #print('-------------------')

        res_body = urlopen(url).read()
        #print(res_body)
        soup = BeautifulSoup(res_body, 'html.parser')
        items = soup.findAll('row')
        for item in items:
            item = re.sub('<.*?>', '|', str(item))#item.text)
            parsed = item.split('|')
            #print(parsed)
            try:
                info = parsed[6] + \
                      '\n대표메뉴 : ' + parsed[8]+ '\n전화번호 : ' +parsed[10] + \
                      '\n주소 : ' + parsed[14] # + '\n도로명주소 : ' + parsed[16]
            except IndexError:
                info = item.replace('|', ',')

            if info:
                res_list.append(info.strip())
        return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData(param)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg) + 1> MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')
    print( '[',today,']received token :', TOKEN )
    pprint( bot.getMe() )
    run(current_month)