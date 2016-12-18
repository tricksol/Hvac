#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  temp.py
#  
#  Copyright 2016 Matthew Midgett <matthew@midgettfamily.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import time
import datetime
import glob
import MySQLdb
from time import strftime


# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="swriter",passwd="password", db="hvac")
cur = db.cursor()
 
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor = '/sys/bus/w1/devices/28-041673dc6dff/w1_slave'
sensor_id = '28-041673dc6dff'
host = os.uname()[1]
host_id = 1
 
def tempRead():
        t = open(temp_sensor, 'r')
        lines = t.readlines()
        t.close()
 
        temp_output = lines[1].find('t=')
        if temp_output != -1:
                temp_string = lines[1].strip()[temp_output+2:]
                temp_c = float(temp_string)/1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
        return round (temp_f,1)    
         
while True:
    temp = tempRead()
    print temp
    datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    print datetime
    sql = ("""INSERT INTO temp (host_id,host,sensor_id,datetime,temp) VALUES (%s,%s,%s,%s,%s)""",(host_id,host,sensor_id,datetime,temp))
    try:
        print "Writing to database..."
        # Execute the SQL command
        cur.execute(*sql)
        # Commit your changes in the database
        db.commit()
        print "Write Complete"
 
    except:
        # Rollback in case there is any error
        db.rollback()
        print "Failed writing to database"
 
    cur.close()
    db.close()
    break
