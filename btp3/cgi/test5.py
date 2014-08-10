#!/usr/bin/env python

from PrintFunctions import *;
def printApp(error_message='',message=''):
    print "Content-type: text/html"
    print
    printHeader()
    printNavbar()
    try:
        getvars = cgi.FieldStorage()
        error_message=getvars["error"].value    
    except:
        pass
    if error_message:
        printError(error_message)
    if message:
        printMessage(message)
    printTables()
    printBags()
    printOperations()
    printFooter()
if __name__=='__main__':

    printApp()
