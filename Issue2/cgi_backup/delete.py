#!/usr/bin/env python
#print("Location:http://newurl.com/foobar")


import cgi
import QBO
import backend

getvars = cgi.FieldStorage()
tablename=''
try:
    tablename=getvars["bagname"].value    
except:
    pass

if(tablename):
    backend.deleteBag(tablename)

from test5 import printApp
printApp()
