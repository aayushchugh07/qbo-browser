#!/usr/bin/env python
from new_db import QBO
import cgi

def printApp():
    qbo=QBO();
    
    print "Content-type: text/html"
    print
    # print('''<!Doctype html> <html><head><title>abcd</title></head><body>It works
    #        '''+str(qbo.try_stuff())+'''
    #        </body></html>''');
    getvars = cgi.FieldStorage()
    tablename=''
    try:
        tablename=getvars["bagname"].value
    except:
        pass
    if(tablename==''):
        

if __name__=='__main__':
    printApp()
