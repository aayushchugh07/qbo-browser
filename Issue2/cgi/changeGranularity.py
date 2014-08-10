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
    finalSchema = []
    initialCount=0;
    finalCount=0;
    for row in x:
    	    initialCount = initialCount + 1
	    colName = str(row[0])
	    colKey = str(row[1])
	    colType = str(row[2])
	    sys.stderr.write(str(getvars))
	    if(colKey=='PRI'):
		try:
			finalSchema.append([colName,getvars[colName].value])
			finalCount = finalCount +1
		except KeyError:
			pass
	    else:
	 	st = [None,None]
	 	try:
			if(getvars["selected"+colName].value == "yes"):
				st[0]=colName
		except KeyError:
			pass
		try:
			if(getvars[colName].value):
				st[0]=colName
				st[1]=getvars[colName].value
		except KeyError:
		  	pass
		if(st[0]!=None):
			finalCount = finalCount +1
			finalSchema.append(st);
    backend.finalize(tablename,finalSchema,initialCount,finalCount)
from test5 import printApp
printApp()
