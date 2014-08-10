#!/usr/bin/python
import MySQLdb,sys
class QBO:
	# intermediate name -> [intermediate sql, bit, parent1,parent2]
	intermediateObjCount=0
	#BagDict = {}
	BagDict2=[]
	OperationsList = []
	Selected = [None,None]
	#TODO make TableDescription persistent
	TableDescription = {}
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
	def __init__(self,persistent_data):
                if(persistent_data!=None):
			self.OperationsList = persistent_data["OperationsList"]
			self.Selected = persistent_data["Selected"]
                        self.BagDict2=persistent_data["BagDict2"]
                        self.intermediateObjCount=persistent_data["intermediateObjCount"]
		try:
			self.dbh = MySQLdb.connect(host=self._databaseInfo['host'],user=self._databaseInfo['user'],passwd=self._databaseInfo['passwd'],db=self._databaseInfo['db'])
			self.resultData=None
			self.getDescription();
		#	print self.TableDescription;
		       	self.outputResult();
		except MySQLdb.Error,e:
			print "Error %d: %s" %(e.args[0],e.args[1])
			sys.exit(1);
	def selectTable(self,x):
		if(self.Selected[0]==x or self.Selected[1]==x):
			return
		old = self.Selected[0]
		self.Selected[0] = self.Selected[1]
		for obj in self.BagDict2:
			if(obj["name"]==old):
				obj["selected"]=False
			elif(obj["name"]==x):
				obj["selected"]=True
				self.Selected[1]=x
	def unselectTable(self,x):
		if(self.Selected[0]!=x and self.Selected[1]!=x):
			return
		if(self.Selected[0]==x):
			self.Selected[0]=self.Selected[1]
			self.Selected[1]=None
		else:
			self.Selected[1]=None;
		for obj in self.BagDict2:
			if(obj["name"]==x):
				obj["selected"]=False
	def selectOperation(self,x):
		sys.stderr.write("yoyoy"+x);
		for op in self.OperationsList:
			if(op["name"]==x):
				op["selected"]=True
			else:
				op["selected"]=False
	def unselectOperation(self,x):
		for op in self.OperationsList:
				op["selected"]=False
       	def getDescription(self):
		for o in self.ObjectsList:
			self.TableDescription[o] = []
			self.runQueries('describe '+o);
			for row in self.resultData:
				sys.stderr.write(row['Type'])
				self.TableDescription[o].append([row['Field'],row['Key'],str(row['Type'])])
	def runQueries(self, st):
		try:
			dataCursor = self.dbh.cursor( cursorclass=MySQLdb.cursors.DictCursor )
			dataCursor.execute(st)
			self.resultData = dataCursor.fetchall()
			return True
		except MySQLdb.Error,e:
			return "Error %d : %s"%(e.args[0],e.args[1])
	def outputResult(self):
		outputList = []
	def viewData(self,x):
		for obj in self.BagDict2:
			if(obj["name"]==x):
				x=self.runQueries(obj["sql"]+" as "+x)
				if(x!=True):
					sys.stderr.write(x)
					sys.stderr.write(obj["sql"])
                                return self.resultData
	def printForm(self,x):
		for bag in self.BagDict2:
			if(bag["name"] == x):
				return bag["description"]
	def getColumns(self):
		r = self.resultData[0]
#	Inserts default object(tables) into bag
#	objname -> objname_in_bag 
	def insertObjectInBag(self, objname,newobjname):
		sys.stderr.write(objname)
		if objname in self.ObjectsList:
#	sys.stderr.write(objname=='Book_Copy')
			if objname == 'Book_Type':
				self.BagDict2.append({"name":newobjname,"selected":False,"sql":"select * from Book_Type","description":self.TableDescription[objname]})
			if objname == 'Book_Copy':
				sys.stderr.write("Iminner");
				self.BagDict2.append({"name":newobjname,"selected":False,"sql":"select * from Book_Copy","description":self.TableDescription[objname]})
			if objname == 'Customer':
				self.BagDict2.append({"name":newobjname,"selected":False,"sql":"select * from Customer","description":self.TableDescription[objname]})
			if objname == 'Issue':
				self.BagDict2.append({"name":newobjname,"selected":False,"sql":"select * from Issue","description":self.TableDescription[objname]})
			if objname == 'Returns':
				self.BagDict2.append({"name":newobjname,"selected":False,"sql":"select * from Returns","description":self.TableDescription[objname]})
			if objname == 'Staff':
				self.BagDict2.append({"name":newobjname,"selected":False,"sql":"select * from Staff","description":self.TableDescription[objname]})
			return newobjname
		else:
			return None
	def intersectDescription(self,t1,t2):
		commonDescription = []
		for i in t1:
			for j in t2:
				if(i[0]==j[0]):
					commonDescription.append([i[0],i[1],j[1]])
		return commonDescription
	def getPriMul(self,schema):
		l = []
		for i in schema:
		#	print i[1]=='PRI',i[2]=='MUL'
			if((i[1]=='PRI' and i[2] == 'MUL') or (i[1]=='MUL' and i[2]=='PRI')):
				l.append(i[0])
				sys.stdout.write(i[0])
		return l
	def getSame(commonDescription):
		l = []
		for i in CommonDescription:
			if(i[1]==i[2]):
				l.append((i[0],i[1]))
		return l
	def operate(self,result):
		obj1 = None
		obj2 = None
		for obj in self.BagDict2:
			if(self.Selected[0] == obj["name"]):
				obj1 = obj
			elif(self.Selected[1] == obj["name"]):
				obj2 = obj
		operation = None
		for op in self.OperationsList:
			if(op["selected"]==True):
				operation = op["name"]
		if(operation == 'except'):
			obj1schema = obj1["description"]
			obj2schema = obj2["description"]
			commonDescription = self.intersectDescription(obj1schema,obj2schema)
			subtractColumn = self.getPriMul(commonDescription)
		#	print subtractColumn
		#	sys.stderr.write(subtractColumn)
			if(len(subtractColumn)!=1):
				return False
       			st=' select * from ( ' +obj1['sql']+ ' as ' + obj1['name'] + ' where ' + obj1['name']+'.'+subtractColumn[0] + ' not in ( select '+subtractColumn[0]+' from ( '+obj2['sql']+' ) as ' +obj2['name'] + '))'
			st1 = st + ' as ' + result
			x=self.runQueries(st1);
			if(x==True):
				self.BagDict2.append({"name":result,"selected":False,"sql":st,"description":obj1schema})	
			else:
				sys.stderr.write(x)
				sys.stderr.write(st1)
		if(operation == 'intersect'):
			obj1schema = obj1["description"]
			obj2schema = obj2["description"]
			commonDescription = self.intersectDescription(obj1schema,obj2schema)
			subtractColumn = self.getPriMul(commonDescription)
		#	print subtractColumn
		#	sys.stderr.write(subtractColumn)
			if(len(subtractColumn)!=1):
				return False
       			st=' select * from ( ' +obj1['sql']+ ' as ' + obj1['name'] + ' where ' + obj1['name']+'.'+subtractColumn[0] + ' in ( select '+subtractColumn[0]+' from ( '+obj2['sql']+' ) as ' +obj2['name'] + '))'
			st1 = st + ' as ' + result
			x=self.runQueries(st1);
			if(x==True):
				self.BagDict2.append({"name":result,"selected":False,"sql":st,"description":obj1schema})	
			else:
				sys.stderr.write(x)
				sys.stderr.write(st1)
	#		self.outputResult();

		# if(operation == 'intersect'):
		# 	obj1schema = self.TableDescription[obj1]
		# 	obj2schema = self.TableDescription[obj2]
		# 	commonDescription = self.intersectDescription(obj1schema,obj2schema)
		# 	subtractColumn = self.getPriMul(commonDescription)
		# #	print subtractColumn
		# 	if(len(subtractColumn)!=1):
		# 		return False
		# 	#TODO replace obj1 and obj2 below with there sql query in bagdict
		# 	self.runQueries('select * from ' + obj1 + ' as ' + obj1 + ' where ' + obj1+'.'+subtractColumn[0] + ' in (select ' +subtractColumn[0] + ' from ' + obj2 + ')')
		# 	self.outputResult();
		# if(operation == 'union' ):
		# 	self.runQueries('select * from ' + obj1 + ' as ' + obj1 + ' union select * from ' +obj2)
		
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
# 	obj1.operate('Customer','Issue','Result','intersect')
