#!/usr/bin/env python
#print("Location:http://newurl.com/foobar")


import cgi
import QBO
import backend

getvars = cgi.FieldStorage()
tablename=''
try:
    tablename=getvars["tablename"].value    
except:
    pass

if(tablename):
    backend.addBag(tablename)

from test5 import printApp
printApp()
