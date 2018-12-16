#!/usr/bin/python
import MySQLdb

#
 #       'NAME': 'hundy_LifeManagement',
 #       'USER': 'hundy_LMAdmin',
 #       'PASSWORD': 'Scr3am!ngM!M!',
 #       'HOST': 'gator3212.hostgator.com',
 #       'PORT': '3306',
 #       'OPTIONS': {
 #           'read_default_file': '/path/to/my.cnf'



db = MySQLdb.connect(host='gator3212.hostgator.com',    # your host, usually localhost
                     user='hundy_LMAdmin',         # your username
                     passwd='Scr3am!ngM!M!',  # your password
                     db='hundy_LifeManagement')        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Get data from database
try:
    cur.execute("SELECT * FROM Contacts")
    rows = cur.fetchall()
except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
# Print results in comma delimited format
for row in rows:
    for col in row:
        print ("%s," % col)
    print ("\n")

db.close()