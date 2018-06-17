from bottle import  run, route, static_file, view, template, post, request

import sqlite3
import sys
import datetime
import vk
import os


@route('/')
def index():
    today = datetime.datetime.today()
    date = today.strftime("%Y.%m.%d")
    time = today.strftime("%H.%M")
    colsp = []
    timesp = []
    sts = []
    dirs = os.path.dirname(os.path.abspath(__file__))
    con = None
    con = sqlite3.connect(dirs+'/online'+date+'.db')

    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM Online ORDER BY id DESC LIMIT 12")
 
    while True:
        row = cur.fetchone()
        
        if row == None:
            break
            
        colsp.append(row[1])
        timesp.append(row[2])
        list(reversed(colsp))
        list(reversed(timesp))
    dirs = os.path.dirname(os.path.abspath(__file__))
    con = None
    con = sqlite3.connect(dirs+'/History.db')
    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM History ORDER BY id DESC LIMIT 30")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        sts.append(row)

    return template ('''<!DOCTYPE html>
  <html>
    <head>
       <meta charset="utf-8"/> 
        <title>Онлайн</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css">
      <script src="https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js"></script>
    </head>
    <body>    
    <div style="margin: 10px auto; text-align: center">График</div>
    
    <div class="ct-chart ct-perfect-fourth" style="max-width:700px; margin: 10px auto"></div>

    <div style="margin: 10px auto; text-align: center">Статистика</div>
     <div style="margin: 10px auto; text-align: center">{{sts}}</div>
<script>
new Chartist.Line('.ct-chart', {
  labels: {{!timesp}} ,
  series: [
    {{colsp}}
  ]
}, {
  showArea: true
}); 
</script>
</body>
  </html>''', colsp=list(reversed(colsp)), timesp=list(reversed(timesp)), sts=sts )


run(host='194.177.20.97', port=80)
