#!/usr/bin/env python
#print("Location:http://newurl.com/foobar")


import cgi
import QBO
import backend

getvars = cgi.FieldStorage()
tablename=''
newname=''
try:
    tablename=getvars["oldname"].value
    newname=getvars["newname"].value
except:
    pass

if(tablename):
    backend.renameBag(tablename, newname)

from test5 import printApp
printApp()
