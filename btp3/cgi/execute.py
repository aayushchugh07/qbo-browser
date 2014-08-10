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

from test5 import printApp

if(operationname):
    try:
        backend.selectOperation(operationname)
        operation_result=backend.operate()
        if(operation_result==True):
            printApp()
        elif operation_result==None :
            printApp(message="No records found for the specified operation")
        else: 
            printApp(operation_result)
        import sys
        sys.stderr.write("Return val of operation is:"+str(operation_result))
    except:
        printApp("Could not execute operation")
else:
    printApp("No operation specified")
