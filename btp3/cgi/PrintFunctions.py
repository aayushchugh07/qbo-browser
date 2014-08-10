#!/usr/bin/env python
import urllib,cgi,sys
def pp(x):
    print x;
# def getObjects():
#     return ['a','b','c','d','e']
# def getBags():
#     return [{"name":'a',"selected":True},
#             {"name":'a',"selected":False},
#             {"name":'a',"selected":False},
#             {"name":'a',"selected":False}
#         ]
# def getOperations():
#     return ['op1', 'op2','op3','op4']
from backend import getObjects,getBags,getOperations
def getURLinHTML(x):
    return str(x)
    return cgi.escape(urllib.quote_plus(x),quote=True)
def esc(x):
    return str(x)
    return cgi.escape(x,quote=True)
def unesc(x):
    return str(x)
    return cgi.unescape(x,quote=True)
def getImageLink(tablename):
    image_links={"Book_Type":"book.png", "Book_Copy":"book_copy.jpg",\
                 "Issue":"issue.jpg","Customer":"People.png",\
                 "Returns":"return.jpg","Staff":"staff.jpeg"\

    }
    if(tablename in image_links.keys()):
        return "/images/"+image_links[tablename]
    else: return "/images/bag.jpg"
def printHeader():
    pp( '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Library-QBO</title>

    <!-- Bootstrap -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">
    <!-- Extra theme that will screw up everything -->
    <!-- link href="/css/bootstrap-theme.min.css" rel="stylesheet" -->
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div style="padding-left:0px;">
''')
def printError(error_message):
    pp('''      <div class="alert alert-danger">
        '''+esc(error_message)+'''
      </div>''')
def printMessage(message):
    pp('''      <div class="alert alert-info"">
        '''+esc(message)+'''
      </div>''')
def printNavbar():
    pp( '''
<!-- h2>Library-QBO</h2 -->
    <div class="navbar navbar-default">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Library-QBO</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="/cgi/test5.py">Home</a></li>
            <li><a href="#about">Data Viewer</a></li>
            <li><a href="#contact">Feedback</a></li>
            <!-- li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li -->
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>
''')

def printTables():
    pp('''
    <hr />
    <h3>Tables</h3>
    <p>Click on a table to add a new bag</p>
    <div class="row">
    ''')
    tables=getObjects()
    for table in tables:
        pp('''
            <div class="col-md-1">
              <div align="center">
		<a href="/cgi/addbag.py?tablename='''+getURLinHTML(table)+'''">
		  <img src="'''+getImageLink(table)+'''" width="60px" height="60px" />
		</a>
	      </div>
	      <p align="center">'''+table+'''</p>
	    </div>
''')
    pp('''
    </div> <!-- /row -->''')
 
def printRecords(x,table):
    pp('''
    <hr />
    <h3>Records</h3>
    <p>Records for table '''+table+''''</p>
    <div class="row">
    ''')
    for row in x:
#    pp('''
#           <div class="col-md-1">
#             <div align="center">
#		<a href="/cgi/addbag.py?tablename='''+getURLinHTML(table)+'''">
#		   <img src="/images/People.png" width="60px" height="60px" />
#		</a>
#	      </div>
#	      <p align="center">'''+table+'''</p>
#	    </div>
#''')
	    for col in row:
	    	pp('''<div align="center">'''+str(col)+''' : '''+str(row[col]) + '''<br/></div>''')
	    pp('''<br/>''')
    pp('''
    </div> <!-- /row -->''')
    
def printForm(x,table):
    pp('''
    <hr />
    <h3>Select Granularity</h3>
    <p>Select Granularity for table '''+table+'''</p>
    <div class="row"><form action='changeGranularity.py' method='GET'>
    ''')
    pp('''<input type="hidden" name="bagname" value="'''+table+'''">)''')
    for row in x:
	    colName = str(row[0])
	    colKey = str(row[1])
	    colType = str(row[2])
#    pp('''
#           <div class="col-md-1">
#             <div align="center">
#		<a href="/cgi/addbag.py?tablename='''+getURLinHTML(table)+'''">
#		   <img src="/images/People.png" width="60px" height="60px" />
#		</a>
#	      </div>
#	      <p align="center">'''+table+'''</p>
#	    </div>
#''')
	    pp('''<div align="center">'''+colName+''' : '''+'''<input type='text' name="''' +colName+ '''"/>''')
	    if(colKey=='PRI'):
		    pp('''Compulsory to be selected''')
	    else:
		    pp('''<input type="checkbox" name="selected'''+colName+'''" value="yes" >select ''')
	    pp('''<br/>''')
	    pp('''<br/>''')
    pp('''<input type="submit" value="Finalize >>"></div></form>
    </div> <!-- /row -->''')

def printFooter():
    pp('''    
    <script src="/js/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/js/bootstrap.min.js"></script>
    </div>
  </body>
</html>
''')

def printBags():
    bags=getBags()
    help_statement=''
    selected_count=0
    selected_name=''
    for bag in bags:
        if(bag["selected"]==True):
            selected_count+=1
            selected_name=bag["name"]
    buttons_html=''
    if(selected_count==0):
        help_statement="Select one or two bags to perform operations."
    elif selected_count==1:
        help_statement="Select a bag or an operation"
    else: help_statement="Two bags are selected. Please Select an operation below."
    pp('''
    <hr />
    <h3>Bags</h3>
    <p>'''+help_statement+'''</p>
    <div class="row">
    ''')
    for bag in bags:
        if(bag["selected"]==True):
            selected_name=bag["name"]
            buttons_html='''    	<div style="padding-left:10px;">
        <a href="/cgi/delete.py?bagname='''+selected_name+'''">
	      <button class="btn btn-primary">Delete</button>
            </a>
	    <a href="/cgi/rename.py?oldname='''+selected_name+'''&amp;newname=renamed1">
	      <button class="btn btn-primary">Rename</button>
            </a>
	    <a href="/cgi/viewdata.py?bagname='''+selected_name+'''">
	    <button class="btn btn-primary">View data</button>
	    </a>
	   
	<a href="/cgi/selectGranularity.py?bagname='''+selected_name+'''">
              <button class="btn btn-primary">Select<br/>Granularity</button>
            </a>
	  </ul>
	</div>'''
            
            pp('''
      	<div class="col-md-3">
	  <div class="panel panel-default">
            <div class="panel-heading">
	      <div align="center">
            <table>
              <tr><td>
		  <a href="/cgi/unselected.py?bagname='''+esc(bag["name"])+'''">
		   <img src="'''+getImageLink(bag["name"])+'''" width="60px" height="60px" align="center"/>
		  </a>
		  <p align="center">'''+esc(bag["name"])+'''</p>
	      
		</td><td>
                '''+buttons_html+'''
                </td></tr></table>
	      </div>
	      </div>
	  </div>
	</div>
''')
        else:
            pp('''
      	<div class="col-md-1">
            
	  <div class="panel panel-default">
            <div class="panel-body">
	      <div align="center" style="padding-top: 12px;">
		<a href="/cgi/selected.py?bagname='''+esc(bag["name"])+'''" >
		   <img src="'''+getImageLink(bag["name"])+'''" width="60px" height="60px" />
		</a>
	      </div>
	  </div></div>
	  <p align="center">'''+esc(bag["name"])+'''</p>
	</div>
     
''')

    pp('</div> <!-- row -->')
    if(len(bags)>0):
        pp('''
        <a href="/cgi/clearbags.py">
          <button class="btn btn-danger" >Clear all </button>
        </a>
	''')
    
    #pp(buttons_html)
def printOperations():
    operations=getOperations()
    help_statement=''
    if(len(operations))==0:
        help_statement="No operations available"
    else:
        help_statement="Click on an operation for selected table(s)."
    pp('''    
    <hr />
    <h3>Operations</h3>
    <p>'''+help_statement+'''</p>
    <div class="row">
''')
    for op in operations:
#         if(op["selected"]==True):
#             pp('''
#       	<div class="col-md-2">
# 	  <div class="panel panel-default">
#             <div class="panel-heading">
# 	      <div align="center">
#             <table>
#               <tr><td>
# 		  <a href="/cgi/unselected_operation.py?operationname='''+esc(op["name"])+'''">
# 		    <img src="/images/People.png" width="60px" height="60px" align="center"/>
# 		  </a>
# 		  <p align="center">'''+esc(op["name"])+'''</p>
	      
# 		</td>
#                 </tr></table>
# 	      </div>
# 	      </div>
# 	  </div>
# 	</div>
# ''')
#         else:
            pp('''
      	<div class="col-md-1">
	  <div align="center" style="padding-top: 12px;">
	    <a href="/cgi/execute.py?operationname='''+esc(op["name"])+'''" >
	      <img src="'''+getImageLink(op["name"])+'''" width="60px" height="60px" />
	      </a>
	  </div>
	  <p align="center">'''+esc(op["name"])+'''</p>
	</div>
     
''')

    pp('''
    </div><!-- row -->
''')    
    # pp('''
    #     <a href="/cgi/execute.py">
    #       <button class="btn btn-danger" >Execute </button>
    #     </a>
    #     ''')
