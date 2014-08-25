#!/usr/bin/python
import MySQLdb,sys,json
class QBO:
    _databaseInfo = dict(
			host = "localhost",
			user = "root",
			passwd = "iiit123",
			db = "library")
    
    ObjectsList = ['Book_Type','Book_Copy','Customer','Issue','Returns','Staff']

# create table Book_Type(ISBN varchar(13) not null, BookAuthor varchar(255),BookName varchar(255),BookEdition varchar(5), primary key (ISBN));
# create table Customer(Customer_ID varchar(13) not null, name varchar(100), email varchar(100), roll_no varchar(13),primary key(Customer_ID));
# create table Staff(Staff_ID varchar(13) not null, name varchar(100), phone_number varchar(14), email varchar(100),primary key(Staff_ID));
# create table Book_Copy(Book_ID varchar(13) not null, ISBN varchar(13), isReference boolean,primary key (Book_ID),foreign key (ISBN) references Book_Type(ISBN));
# create table Issue(Issue_ID varchar(13) not null, Book_ID varchar(13) references Book_Copy(Book_ID), Issue_date date, Customer_ID varchar(13) references Customer(Customer_ID),expiry_date date, Staff_ID varchar(13) references Staff(Staff_ID),primary key(Issue_ID),foreign key (Book_ID) references Book_Copy(Book_ID),foreign key(Customer_ID) references Customer(Customer_ID),foreign key(Staff_ID) references Staff(Staff_ID));
# create table Returns(Book_ID varchar(13) references Book_Copy(Book_ID), Issue_ID varchar(13) references Issue(Issue_ID), Returns_Date date, Staff_ID varchar(13), foreign key(Staff_ID) references Staff(Staff_ID),foreign key(Book_ID) references Book_Copy(Book_ID),foreign key (Issue_ID) references Issue(Issue_ID));
    

    queries={
        'returns_handled_by_staff' : 'select * from Returns natural join Staff;',
        'issues_handled_by_staff' : 'select * from Issue natural join Staff;',
        'returned_books' : 'select * from Book_Type natural join Book_Copy natural join Returns;',
        "returns_by_customer" : "select * from Customer natural join (select * from  (select i.Issue_ID,i.Book_ID,i.Issue_date,i.Customer_ID,i.expiry_date,i.Staff_ID as 'Issuing Staff', r.Returns_Date, r.Staff_ID as 'Returning Staff' from Issue as i join Returns as r where i.Issue_ID = r.Issue_ID ) as t1) as t3; ",
        "returned_issues" : "select * from  (select i.Issue_ID,i.Book_ID,i.Issue_date,i.Customer_ID,i.expiry_date,i.Staff_ID as 'Issuing Staff', r.Returns_Date, r.Staff_ID as 'Returning Staff' from Issue as i join Returns as r where i.Issue_ID = r.Issue_ID ) as t1;",
        "not_returned_issues" : "select * from Issue where Issue_ID not in (select Issue_ID from Returns);",
        "returns_handled_by_staff" : "select * from Returns natural join Staff;",
        "getIssuedBooks" : "select * from  Book_Type natural join Book_Copy natural join Issue;",
        "issues_by_customer" : "select * from Customer c , Issue i where c.Customer_ID=i.Customer_ID;",
        "issues_handled_by_staff" : "select * from Issue natural join Staff;",
        "customers_of_book" : "select * from Book_Type natural join (select * from Book_Copy natural join (select * from (select * from Issue natural join Customer) as t1) as t2) as t3;",
        "returns_of_book_customer" : "select * from Book_Type natural join (select * from Book_Copy natural join (select * from  Customer natural join (select i.Issue_ID,i.Book_ID,i.Issue_date,i.Customer_ID,i.expiry_date,i.Staff_ID as 'Issuing Staff', r.Returns_Date, r.Staff_ID as 'Returning Staff' from Issue as i join Returns as r where i.Issue_ID = r.Issue_ID ) as t1) as t2) as t3;",
        "book_details" : "select * from Book_Type natural join Book_Copy;",
        "Book_Type":"select * from Book_Type;",
        "Book_Copy":"select * from Book_Copy;",
        "Customer":"select * from Customer;",
        "Issue":"select * from Issue;",
        "Returns":"select * from Returns;",
        "Staff":"select * from Staff;"
    }
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
            for result_item in self.resultData:
                result_item['_is_shown']=True
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
    
    def execOperation(self, operation_name):
        try:
            query=self.queries[operation_name]
            self.runQueries(query)
        except:
            raise Exception("Exception occured in trying to run query")
        return json.dumps(self.resultData)

    def __init__(self):
        try:
            self.TableDescription={};
            self.dbh = MySQLdb.connect(host=self._databaseInfo['host'],user=self._databaseInfo['user'],passwd=self._databaseInfo['passwd'],db=self._databaseInfo['db'])
            self.resultData=None
            self.getDescription();
            
        except MySQLdb.Error,e:
            print "Error %d: %s" %(e.args[0],e.args[1])
            sys.exit(1);
