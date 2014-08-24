#!/usr/bin/env python
from new_db import QBO
import cgi

def printApp():
    qbo=QBO();
    
    print "Content-type: text/html"
    print
    getvars = cgi.FieldStorage()
    query_name=''
    try:
        query_name=getvars["queryname"].value
    except:
        pass
    if(query_name==''):
        pass
    print('''<!Doctype html> <html><head><title>abcd</title></head><body>It works
           '''+str(qbo.execOperation(query_name))+'''
           </body></html>''');
    

if __name__=='__main__':
    printApp()
