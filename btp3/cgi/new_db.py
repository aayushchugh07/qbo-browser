#!/usr/bin/python
import MySQLdb,sys
class QBO:
    _databaseInfo = dict(
			host = "localhost",
			user = "root",
			passwd = "iiit123",
			db = "library")
    
    ObjectsList = ['Book_Type','Book_Copy','Customer','Issue','Returns','Staff']
    ObjectsListWithNames = [{'name':'Book_Type', 'descr' : 'the ultimate table'},{'name':'Book_Copy', 'descr' : 'the ultimate table'},{'name':'Customer', 'descr' : 'the ultimate table'},{'name':'Issue', 'descr' : 'the ultimate table'},{'name':'Returns', 'descr' : 'the ultimate table'},{'name':'Staff', 'descr' : 'the ultimate table'}]
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

    def viewData(self,x):
        for obj in self.BagDict2:
            if(obj["name"]==x):
                sys.stderr.write("$$$"+obj["sql"]+"$$$")
                x=self.runQueries(obj["sql"]+" as "+x)
                if(x!=True):
                    sys.stderr.write(x)
                    sys.stderr.write(obj["sql"])
                return self.resultData
    def try_stuff(self):
        #This is the ultra useless function, (usually not) used to test if QBO is working
        self.runQueries('select * from Book_Copy;');
        return self.resultData

    def __init__(self):
        try:
            self.TableDescription={};
            self.dbh = MySQLdb.connect(host=self._databaseInfo['host'],user=self._databaseInfo['user'],passwd=self._databaseInfo['passwd'],db=self._databaseInfo['db'])
            self.resultData=None
            self.getDescription();
            
        except MySQLdb.Error,e:
            print "Error %d: %s" %(e.args[0],e.args[1])
            sys.exit(1);
