#!/usr/bin/python
import MySQLdb
class QBO:
	# intermediate name -> [intermediate sql, bit, parent1,parent2]
	intermediateObjCount=0
	BagDict = {}
	TableSchema = {}
	ObjectsList = ['Book_Type','Book_Copy','Customer','Issue','Returns','Staff']
	OperationsDict = {'Book_Type' : {'Book_Type':['union','except','intersect'],'Book_Copy':['getCopies'],'Customer':[],'Issue':[],'Returns':[],'Staff':[]},
			  'Book_Copy' : {'Book_Type':['getDetails'],'Book_Copy':['union','except','intersect'],'Customer':[],'Issue':['getIssuedBooks'],'Returns':['getReturnedBooks'],'Staff':[]},
			  'Customer' : {'Book_Type':[],'Book_Copy':[],'Customer':['union','except','intersect'],'Issue':['getBooksIssuedByCustomer', 'getCustomersforIssuedBook'],'Returns':['getBooksReturnedByCustomer','getCustomersforReturnedBook'],'Staff':[]},
			  'Issue' : {'Book_Type':[],'Book_Copy':[],'Customer':['getBooksIssuedByCustomer', 'getCustomersforIssuedBook'],'Issue':['union','except','intersect'],'Returns':['getIssuesReturned','getIssuesNotReturned'],'Staff':['handled_by']},
			  'Returns' : {'Book_Type':[],'Book_Copy':[],'Customer':[],'Issue':['of'],'Returns':['union','except','intersect'],'Staff':['handled_by']},
			  'Staff' : {'Book_Type':[],'Book_Copy':[],'Customer':[],'Issue':['handles'],'Returns':['handles'],'Staff':['union','except','intersect']}}
# create table Book_Type(ISBN varchar(13) not null, BookAuthor varchar(255),BookName varchar(255),BookEdition varchar(5), primary key (ISBN));
# create table Customer(Customer_ID varchar(13) not null, name varchar(100), email varchar(100), roll_no varchar(13),primary key(Customer_ID));
# create table Staff(Staff_ID varchar(13) not null, name varchar(100), phone_number varchar(14), email varchar(100),primary key(Staff_ID));
# create table Book_Copy(Book_ID varchar(13) not null, ISBN varchar(13), isReference boolean,primary key (Book_ID),foreign key (ISBN) references Book_Type(ISBN));
#  create table Issue(Issue_ID varchar(13) not null, Book_ID varchar(13) references Book_Copy(Book_ID), Issue_date date, Customer_ID varchar(13) references Customer(Customer_ID),expiry_date date, Staff_ID varchar(13) references Staff(Staff_ID),primary key(Issue_ID),foreign key (Book_ID) references Book_Copy(Book_ID),foreign key(Customer_ID) references Customer(Customer_ID),foreign key(Staff_ID) references Staff(Staff_ID));
# create table Returns(Book_ID varchar(13) references Book_Copy(Book_ID), Issue_ID varchar(13) references Issue(Issue_ID), Returns_Date date, Staff_ID varchar(13), foreign key(Staff_ID) references Staff(Staff_ID),foreign key(Book_ID) references Book_Copy(Book_ID),foreign key (Issue_ID) references Issue(Issue_ID));
	
	_databaseInfo = dict(
			host = "localhost",
			user = "root",
			passwd = "password",
			db = "library")
	def __init__(self):
		try:
			self.dbh = MySQLdb.connect(host=self._databaseInfo['host'],user=self._databaseInfo['user'],passwd=self._databaseInfo['passwd'],db=self._databaseInfo['db'])
			self.resultData=None
			self.getSchema();
			print self.TableSchema;
		       	self.outputResult();
		except MySQLdb.Error,e:
			print "Error %d: %s" %(e.args[0],e.args[1])
			sys.exit(1);
	def getSchema(self):
		for o in self.ObjectsList:
			self.TableSchema[o] = []
			self.runQueries('describe '+o);
			for row in self.resultData:
				self.TableSchema[o].append((row['Field'],row['Key']))
	def runQueries(self, st):
		print st
		try:
			dataCursor = self.dbh.cursor( cursorclass=MySQLdb.cursors.DictCursor )
			dataCursor.execute(st)
			self.resultData = dataCursor.fetchall()
			return True
		except MySQLdb.Error,e:
			return "Error %d : %s"%(e.args[0],e.args[1])
	def outputResult(self):
		outputList = []
		for row in self.resultData:
			print row
	def getColumns(self):
		r = self.resultData[0]
		for s in r:
			print s;
       	# Inserts default object(tables) into bag
	# objname -> objname_in_bag 
	# def insertObjectInBag(self, objname):
	# 	if objname in self.ObjectsList:
	# 		newobjname = objname
	# 		count = 1
	# 		while newobjname in self.BagDict:
	# 			newobjname = newobjname + count
	# 			count = count +1
	# 		if objname is 'Book_Type':
	# 			self.BagDict[newobjname] = ["select * from Book_Type",[1,1,0,0,0,0],None,None]
	# 		if objname is 'Book_Copy':
	# 			self.BagDict[newobjname] = ["select * from Book_Copy",[1,1,0,1,1,0],None,None]
	# 		if objname is 'Customer':
	# 			self.BagDict[newobjname] = ["select * from Customer",[0,0,1,1,1,0],None,None]
	# 		if objname is 'Issue':
	# 			self.BagDict[newobjname] = ["select * from Issue",[0,0,0,1,1,1],None,None]
	# 		if objname is 'Returns':
	# 			self.BagDict[newobjname] = ["select * from Returns",[0,0,0,1,1,1],None,None]
	# 		if objname is 'Staff':
	# 			self.BagDict[newobjname] = ["select * from Staff",[0,0,0,1,1,1],None,None]
	# 		return newobjname
	# 	else:
	# 		return None
	# # objname -> bool
	# def deleteFromBag(self,objname):
	# 	if objname in self.BagDict:
	# 		del self.BagDict[objname]
	# 		return True
	# 	else:
	# 		return False
	def intersectSchema(self,t1,t2):
		commonSchema = []
		for i in t1:
			for j in t2:
				if(i[0]==j[0]):
					commonSchema.append([i[0],i[1],j[1]])
		return commonSchema
	def getPriMul(self,schema):
		print schema
		l = []
		for i in schema:
			print i[1]=='PRI',i[2]=='MUL'
			if((i[1]=='PRI' and i[2] == 'MUL') or (i[1]=='MUL' and i[2]=='PRI')):
				l.append(i[0])
		return l
	def operate(self,obj1,obj2,result,operation):
		# if((obj1 not in self.BagDict) or (obj2 not in self.BagDict)):
		# 	return False
		if(operation == 'except'):
			obj1schema = self.TableSchema[obj1]
			obj2schema = self.TableSchema[obj2]
			commonSchema = self.intersectSchema(obj1schema,obj2schema)
			subtractColumn = self.getPriMul(commonSchema)
			print subtractColumn
			if(len(subtractColumn)!=1):
				return False
			#TODO replace obj1 and obj2 below with there sql query in bagdict
			self.runQueries('select * from ' + obj1 + ' as ' + obj1 + ' where ' + obj1+'.'+subtractColumn[0] + ' not in (select ' +subtractColumn[0] + ' from ' + obj2 + ')')
			self.outputResult();
		if(operation == 'intersect'):
			obj1schema = self.TableSchema[obj1]
			obj2schema = self.TableSchema[obj2]
			commonSchema = self.intersectSchema(obj1schema,obj2schema)
			subtractColumn = self.getPriMul(commonSchema)
			print subtractColumn
			if(len(subtractColumn)!=1):
				return False
			#TODO replace obj1 and obj2 below with there sql query in bagdict
			self.runQueries('select * from ' + obj1 + ' as ' + obj1 + ' where ' + obj1+'.'+subtractColumn[0] + ' in (select ' +subtractColumn[0] + ' from ' + obj2 + ')')
			self.outputResult();

	# 	if(operation == 'union'):
	# 		st = '(select * from ' + self.BagDict[obj1][0] + ' as ' +  obj1 + ' ) union ( select * from '+ self.BagDict[obj2][0] + ' as '+obj2 +')';
	# 		x = self.runQueries(st);
	# 		if(x==True):
	# 			self.BagDict[result] = [st,map(lambda x,y:x|y,list1,list2),obj1,obj2] 
	# 		return x;
	# 	# if(operation == 'intersect'):		
	# 	# 	st = '(select * from ' + BagDict[obj1][0] + ' as ' +  obj1 + ') intersect ( select * from '+BagDict[obj2][0] + 'as '+obj2 +')';
	# 	# 	x = runQueries(st);
	# 	# 	return x;
	# 	# if(operation == 'except'):
	# 	# 	st = '(select * from ' + BagDict[obj1][0] + ' as ' +  obj1 + ') except ( select * from '+BagDict[obj2][0] + 'as '+obj2 +')';
	# 	# 	x = runQueries(st);
	# 	# 	return x;
	# 	if(operation == 'relate'):
	# 		st = '(select * from '+ self.BagDict[obj1][0] + ' as ' + obj1 + ' ) natural join ( select * from ' + self.BagDict[obj2][0] +' as ' + obj2 + ')';
	# 		x = self.runQueries(st);
	# 		if(x==True):
	# 			self.BagDict[result] = [st,map(lambda x,y : x|y,list1,list2),obj1,obj2]
	# 		return x;
	# 	if(operation == 'getCopies'):
	# 		return self.operate(obj1,obj2,result,'relate')
	# 	if(operation == 'getDetails'):
	# 		return self.operate(obj1,obj2,result,'relate')
	# 	if(operation == 'getIssuedBooks'):
	# 		return self.operate(obj1,obj2,result,'relate')
	# 	if(operation == 'getBooksIssued'):
	# 		return self.operate(obj1,obj2,result,'relate')
	# 	if(operation == 'getBooksNotIssued'):

	# 	if(operation == 'getReturnedIssues'):
	# 		return self.operate(obj1,obj2,result,'relate')
	# 	if(operation == 'getNotReturnedIssues'):
	# 		return self.operate(obj1,obj2,result,'relate')
	# 	if(operation == 'getIssuesTakenbyStaff'):
	# 		return 
	# 	if(operation == 'getStaffthattookIssue'):
	# 		return
	# 	if(operation == 'getReturnsTakenbyStaff'):
	# 		return
	# 	if(operation == 'getStaffthattookReturn'):
			
if __name__ == "__main__":
	obj1 = QBO();
	obj1.operate('Customer','Issue','Result','intersect')
