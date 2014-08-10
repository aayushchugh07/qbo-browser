#!/usr/bin/env python
import backend
import json
import cgi

OperationsDict = {'Book_Type' : [{'name':'Book_Type', 'ops':['union','except','intersect']},
                        	{'name':'Book_Copy', 'ops': ['getCopies']}],
	          'Book_Copy' : [{'name':'Book_Type', 'ops':['getDetails']},
		  		 {'name':'Book_Copy', 'ops':['union','except','intersect']},
				 {'name':'Issue', 'ops':['getIssuedBooks']},
				 {'name':'Returns', 'ops':['getReturnedBooks']}],
		  'Customer' : [{'name':'Customer', 'ops':['union','except','intersect']},
		  		{'name':'Issue', 'ops':['getBooksIssuedByCustomer', 'getCustomersforIssuedBook']},
				{'name':'Returns', 'ops': ['getBooksReturnedByCustomer','getCustomersforReturnedBook']}],
	          'Issue' : [{'name':'Customer', 'ops':['getBooksIssuedByCustomer', 'getCustomersforIssuedBook']},
			     {'name':'Issue', 'ops':['union','except','intersect']},
			     {'name':'Returns','ops':['getIssuesReturned','getIssuesNotReturned']},
			     {'name':'Staff', 'ops':['handled_by']}],
		  'Returns' : [{'name':'Issue', 'ops':['of']},
			       {'Returns':['union','except','intersect']},
			       {'Staff':['handled_by']}],
		  'Staff' : [{'name':'Issue', 'ops':['handles']},
		  	     {'name':'Returns', 'ops':['handles']},
			     {'name':'Staff', 'ops':['union','except','intersect']}]}

def getTableOperationsUtil():
	global OperationsDict
	print "Content-type: text/plain"
	print
	getvars = cgi.FieldStorage()
	tablename = ''
	try:
#tablename = getvars["tablename"].value
#	operationsList = OperationsDict[tablename]
		print json.dumps(OperationsDict)
	except:
		pass

if __name__ == '__main__':
	getTableOperationsUtil()
