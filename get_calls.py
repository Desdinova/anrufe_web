#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging

import cgitb, MySQLdb, datetime
# cgitb for Apache cgi connector
# MySQLdb for MySQL connection
# datetime for dates

# Enable Apache cgi connector
cgitb.enable()

# Header for Webpage
print("Content-Type: text/html;charset=utf-8")
print()         # doesn't work without this

# Variables
daysBackwards = 5
today = datetime.datetime.now()         # time right now
dif = datetime.timedelta(days=daysBackwards)
daysAgo = today - dif

htmlHeader = """
<!DOCTYPE html>
<html>
<head>
<title>Anrufe</title>
<link rel='stylesheet' href='styles.css'>
</head>
<body>
"""

htmlFooter = """
</body>
</html>
"""

# Connection to MySQL
db = MySQLdb.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="",     # password
                     db="asterisk")   # name of the database

# Cursor to execute queries
cur = db.cursor()

# Query cdr
cur.execute("SELECT calldate, clid, src, dst from cdr WHERE calldate >=" + "'" + str(daysAgo) + "'"  + " ORDER BY calldate DESC")


print(htmlHeader)

print("<div id='topbar'>")
print("<ul>")
print("<li><h1>Anrufe der letzten " + str(daysBackwards) + " Tage</h1></li>")
print("<li><a href='http://10.0.0.20/python/get_calls.py' class='button'>Refresh</a></li>")
print("</ul>")
print("</div>")

#Empty space. Otherwise fixed topbar overwrites calls.
print("<div style='height:80px;'></div>")

for a in cur.fetchall():
        print("<div id='call'>")
        print("<b>Datum: </b>", a[0], "<br>")
        print("<b>Von: </b>", a[1], " ", a[2], "<br>")
        print("<b>An: </b>", a[3], "<br>")
        print("</div>")

print("</div>")
print(htmlFooter)
