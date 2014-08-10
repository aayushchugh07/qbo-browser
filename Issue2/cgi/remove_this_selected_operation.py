#!/usr/bin/env python
#print("Location:http://newurl.com/foobar")

import cgi
import QBO
import backend

getvars = cgi.FieldStorage()
operationname=''
try:
    operationname=getvars["operationname"].value    
except:
    pass

if(operationname):
    backend.selectOperation(operationname)

from test5 import printApp
printApp()
