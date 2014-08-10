#!/usr/bin/env python
#print("Location:http://newurl.com/foobar")


import cgi
import QBO
import backend
import sys
from PrintFunctions import *;
getvars = cgi.FieldStorage()
tablename=''
newname=''
try:
    tablename=getvars["bagname"].value
except:
    pass
x=None
if(tablename):
    x=backend.printForm(tablename)
print "Content-type: text/html"
print
printHeader()
printNavbar()
printForm(x,tablename)
printFooter() 

