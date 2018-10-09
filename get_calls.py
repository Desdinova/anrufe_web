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
print()		# doesn't work without this

# Variables
today = datetime.datetime.now()		# time right now
dif = datetime.timedelta(days=5)
daysago = today - dif

# Connection to MySQL
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="",     # password
                     db="asterisk")   # name of the database

# Cursor to execute queries
cur = db.cursor()

# Query cdr
cur.execute("SELECT calldate, clid, src, dst from cdr WHERE calldate >=" + "'" + str(daysago) + "'")

for a in cur.fetchall():
	print (a[0], " ", a[1], " ", a[2], "->", a[3], "<br>")