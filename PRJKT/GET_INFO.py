import sqlite3
import sys
import datetime
import vk
import json
import os

login = ''
password = ''
vk_id = ''
 
session = vk.AuthSession(app_id=vk_id, user_login=login, user_password=password) 
vk_api = vk.API(session, v='5.78', lang='ru', timeout=10)
online_dist = vk_api.users.search(count=0, university=128, online=1)
online = online_dist['count']


today = datetime.datetime.today()
date = today.strftime("%Y.%m.%d")
time = today.strftime("%H.%M")

dirs = os.path.dirname(os.path.abspath(__file__))
connect = None
connect = sqlite3.connect(dirs+'/online'+date+'.db')
cursor = connect.cursor()

cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Online'")
one = cursor.fetchall()
print(one[0])

if one[0] == (0,):
    cursor.execute("CREATE TABLE Online (id integer, online integer, time text)")
    newid = 1
else:
    cursor.execute("SELECT max(id) FROM Online;")
    rows= cursor.fetchall()
    for row in rows:
        maxid = row[0]
    newid = maxid + 1

cursor.execute("INSERT INTO Online VALUES (?,?,?)", (newid, online, time))

connect.commit()

max_online = 0
min_online = 0

cursor.execute("SELECT max(online) FROM Online;")
rows = cursor.fetchall()
for row in rows:
     max_online = row[0]

cursor.execute("SELECT min(online) FROM Online;")
rows = cursor.fetchall()
for row in rows:
   min_online = row[0]

connect = None
connect = sqlite3.connect(dirs+'/History.db')
cursor = connect.cursor()

cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='History'")
one = cursor.fetchall()
print(one[0])

if one[0] == (0,):
    cursor.execute("CREATE TABLE History (id integer, max_online integer,min_online integer, date text)")
    newid = 1
    cursor.execute("INSERT INTO History VALUES (?,?,?,?)", (newid, max_online, min_online, date))
    connect.commit()
else:
    cursor.execute("SELECT max(id) FROM History;")
    rows= cursor.fetchall()
    for row in rows:
        maxid = row[0]
    newidnew = maxid + 1
    cursor.execute("SELECT date FROM History WHERE date = :date", {"date": date})
    one = cursor.fetchall()
    if not one:
        cursor.execute("INSERT INTO History VALUES (?,?,?,?)", (newidnew, max_online, min_online, date))
    else:
        cursor.execute("UPDATE History SET max_online = :max_online, min_online = :min_online WHERE date = :date", {"max_online": max_online, "min_online": min_online, "date": date})

connect.commit()



