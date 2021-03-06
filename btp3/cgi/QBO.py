#!/usr/bin/python
#import MySQLdb
class QBO:
	# intermediate name -> [intermediate sql, bit, parent1,parent2]
	intermediateObjCount=0
	BagDict = {}
        BagDict2=[]
	#ObjectsList = ['Book_Type','Book_Copy','Customer','Issue','Returns','Staff']
	ObjectsListWithNames = [{'name':'Book_Type'},{'name':'Book_Copy'},{'name':'Customer'},{'name':'Issue'},{'name':'Returns'},{'name':'Staff'}]
	OperationsDict = {'Book_Type' : {'Book_Type':['union','except','intersect'],'Book_Copy':['getCopies'],'Customer':[],'Issue':[],'Returns':[],'Staff':[]},
			  'Book_Copy' : {'Book_Type':['getDetails'],'Book_Copy':['union','except','intersect'],'Customer':[],'Issue':['getIssuedBooks'],'Returns':['getReturnedBooks'],'Staff':[]},
			  'Customer' : {'Book_Type':[],'Book_Copy':[],'Customer':['union','except','intersect'],'Issue':['getBooksIssuedByCustomer', 'getCustomersforIssuedBook'],'Returns':['getBooksReturnedByCustomer','getCustomersforReturnedBook'],'Staff':[]},
			  'Issue' : {'Book_Type':[],'Book_Copy':[],'Customer':['getBooksIssuedByCustomer', 'getCustomersforIssuedBook'],'Issue':['union','except','intersect'],'Returns':['getIssuesReturned','getIssuesNotReturned'],'Staff':['handled_by']},
			  'Returns' : {'Book_Type':[],'Book_Copy':[],'Customer':[],'Issue':['of'],'Returns':['union','except','intersect'],'Staff':['handled_by']},
			  'Staff' : {'Book_Type':[],'Book_Copy':[],'Customer':[],'Issue':['handles'],'Returns':['handles'],'Staff':['union','except','intersect']}}
# create table Book_Type(ISBN varchar(13) not null, BookAuthor varchar(255),BookName varchar(255),BookEdition varchar(5), primary key (ISBN));
# create table Book_Copy(ID varchar(13) not null, ISBN varchar(13) references Book_Type(ISBN), isReference boolean);
# create table Customer(ID varchar(13) not null, name varchar(100), email varchar(100), roll_no varchar(13));
# create table Staff(ID varchar(13) not null, name varchar(100), phone_number varchar(14), email varchar(100));
# create table Issue(ID varchar(13) not null, Book_ID varchar(13) references Book_Copy(ID), Issue_date date, Customer_ID varchar(13) references Customer(ID),expiry_date date, Staff_ID varchar(13) references Staff(ID));
#  create table Return(Book_ID varchar(13) references Book_Copy(ID), Issue_ID varchar(13) references Issue(ID), Returns_Date date, Staff_ID varchar(13) references Staff(ID));
	
	_databaseInfo = dict(
			host = "localhost",
			user = "root",
			passwd = "password",
			db = "library")
	def __init__(self,persistent_data):
                if(persistent_data!=None):
                        self.BagDict2=persistent_data["BagDict2"]
                        self.intermediateObjCount=persistent_data["intermediateObjCount"]

		# try:
		# 	self.dbh = MySQLdb.connect(host=self._databaseInfo['host'],user=self._databaseInfo['user'],passwd=self._databaseInfo['passwd'],db=self._databaseInfo['db'])
		# 	self.resultData=None
		# 	self.runQueries("show tables");
		# 	self.outputResult();
		# except MySQLdb.Error,e:
		# 	print "Error %d: %s" %(e.args[0],e.args[1])
		# 	sys.exit(1);
        # def runQueries(self, st):
	# 	print st
	# 	try:
	# 		dataCursor = self.dbh.cursor( cursorclass=MySQLdb.cursors.DictCursor )
	# 		dataCursor.execute(st)
	# 		self.resultData = dataCursor.fetchall()
	# 		return True
	# 	except MySQLdb.Error,e:
	# 		return "Error %d : %s"%(e.args[0],e.args[1])
	
        # def outputResult(self):
	# 	outputList = []
	# 	for row in self.resultData:
	# 		print row
       	
        # Inserts default object(tables) into bag
	# objname -> objname_in_bag 
	
        def insertObjectInBag(self, objname):
		if objname in self.ObjectsList:
			newobjname = objname
			count = 1
			while newobjname in self.BagDict:
				newobjname = newobjname + count
				count = count +1
			if objname is 'Book_Type':
				self.BagDict[newobjname] = ["select * from Book_Type",[1,1,0,0,0,0],None,None]
			if objname is 'Book_Copy':
				self.BagDict[newobjname] = ["select * from Book_Copy",[1,1,0,1,1,0],None,None]
			if objname is 'Customer':
				self.BagDict[newobjname] = ["select * from Customer",[0,0,1,1,1,0],None,None]
			if objname is 'Issue':
				self.BagDict[newobjname] = ["select * from Issue",[0,0,0,1,1,1],None,None]
			if objname is 'Returns':
				self.BagDict[newobjname] = ["select * from Returns",[0,0,0,1,1,1],None,None]
			if objname is 'Staff':
				self.BagDict[newobjname] = ["select * from Staff",[0,0,0,1,1,1],None,None]
			return newobjname
		else:
			return None
	
        # # objname -> bool
	def deleteFromBag(self,objname):
		if objname in self.BagDict:
			del self.BagDict[objname]
			return True
		else:
			return False
	
        # def operate(self,obj1,obj2,result,operation):
	# 	if((obj1 not in self.BagDict) or (obj2 not in self.BagDict)):
	# 		return False
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
			
# if __name__ == "__main__":
# 	obj1 = QBO();
