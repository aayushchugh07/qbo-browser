#!/usr/bin/python
import cgi 
import MySQLdb
import sys
print "Content-Type: text/plain\n\n"

_databaseInfo = dict(
  host   = "localhost",
  user   = "root",
  passwd = "password",
  db     = "library"
)
class DataBase:
	def __init__(self):
		try:
 			self.con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

    			self.cur = con.cursor()
    			self.cur.execute("SELECT VERSION()")

   			self.ver = cur.fetchone()
    
   			print "Database version : %s " % ver
    
		except mdb.Error, e:
  
 			print "Error %d: %s" % (e.args[0],e.args[1])
    			sys.exit(1)
	
	def executeQuery(self,query):
		cur.execute(query)
