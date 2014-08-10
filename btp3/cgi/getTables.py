#!/usr/bin/env python
#print("Location:http://newurl.com/foobar")


#import cgi
import backend
import json

#getvars = cgi.FieldStorage()
def getTablesUtil():
	print "Content-type: text/plain"
	print
	ObjectList = backend.getObjectsWithNames()
	
	print json.dumps(ObjectList)
	 
 
if __name__=='__main__':
	getTablesUtil()
