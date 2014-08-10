#!/usr/bin/env python

from PrintFunctions import *;
def printApp():
    print "Content-type: text/html"
    print
    printHeader()
    printNavbar()
    printTables()
    printBags()
    printOperations()
    printFooter()
if __name__=='__main__':

    printApp()
