#!/usr/bin/env python
import shelve
import sys
from QBOmy import QBO

intermediateObjCount=0;
# [{name:bag,selected:boolean,intermediate sql,schema}]
BagDict2 = [];
Selected = []
OperationsList = []
qbo=None;
d=None
def initBackend():
    global qbo,intermediateObjCount, BagDict2,d,Selected
    d = shelve.open("session_shelve_file") # open, with (g)dbm filename -- no suffix
    if(d.has_key("key")):
        # if(d.has_key("BagDict2")):
        #     del d["BagDict2"]
        #     d["BagDict2"]=[]
        Selected = d["Selected"]
        intermediateObjCount=d["intermediateObjCount"]
        BagDict2 = d["BagDict2"] 
        OperationsList = d["OperationsList"]
    else:
        intermediateObjCount=0
        BagDict2 = []
        Selected = [None,None]
       	OperationsList = [{"name":"union","selected":False},
			  {"name":"except","selected":False},
			  {"name":"intersect","selected":False}]
    qbo=QBO({"intermediateObjCount":intermediateObjCount, "BagDict2":BagDict2,"Selected":Selected,"OperationsList":OperationsList})

def addBagHelper(x,cnt):
    try_name=x+("" if cnt==0 else str(cnt))
    found=False
    for val in qbo.BagDict2:
        if(val["name"]==try_name):
            found=True
            addBagHelper(x,cnt+1)
            break;
    if not found:
     #   sys.stderr.write("hello")
        qbo.insertObjectInBag(x,try_name)
def addBag(x):
    # -- main code 
    global qbo,d
    initBackend()
    addBagHelper(x,0)
    endBackend()

def endBackend():
    global d;
    d["intermediateObjCount"]=qbo.intermediateObjCount
    d["BagDict2"]=qbo.BagDict2
    d["Selected"] = qbo.Selected
    d["OperationsList"]=qbo.OperationsList
    d["key"]=True
    d.close()

def getObjects():
    global qbo,d
    initBackend()
    retval=qbo.ObjectsList
    endBackend()
    return retval

def getObjectsWithNames():
    global qbo,d
    initBackend()
    retval=qbo.ObjectsListWithNames
    endBackend()
    return retval

def getBags():
    global qbo,d
    initBackend()
    retval=qbo.BagDict2
    endBackend()
    return retval

def deleteAllBags():
    global qbo,d
    initBackend()
    qbo.BagDict2=[]
    endBackend()

def selectTable(x):
    global qbo
    initBackend()
    qbo.selectTable(x)
    # for obj in qbo.BagDict2:
    # 	if(obj['name']==x):
    #     	obj['selected']=True
    endBackend()

def unSelectTable(x):
    global qbo
    initBackend()
    qbo.unselectTable(x)
    # for obj in qbo.BagDict2:
    # 	if(obj['name']==x):
    #     	obj['selected']=False
    endBackend()
def selectOperation(x):
    global qbo
    initBackend()
    sys.stderr.write(x)
    qbo.selectOperation(x)
    # for obj in qbo.BagDict2:
    # 	if(obj['name']==x):
    #     	obj['selected']=True
    endBackend()

def unSelectOperation(x):
    global qbo
    initBackend()
    sys.stderr.write(x)
    qbo.unselectOperation(x)
    # for obj in qbo.BagDict2:
    # 	if(obj['name']==x):
    #     	obj['selected']=False
    endBackend()

def deleteBag(x):
    global qbo
    initBackend()
    for i, obj in enumerate(qbo.BagDict2):
        if(obj["name"]==x):
            del qbo.BagDict2[i]
            break;
    endBackend()


def operateHelper(x,cnt):
    try_name=x+("" if cnt==0 else str(cnt))
    found=False
    for val in qbo.BagDict2:
        if(val["name"]==try_name):
            found=True
            operateHelper(x,cnt+1)
            break;
    if not found:
        sys.stderr.write("hello")
        qbo.operate(try_name);
    
def operate():
    global qbo
    initBackend()
    operateHelper('intermediateBag',0)
    endBackend()

def renameBagHelper(x,cnt):

    try_name=x+('' if cnt==0 else str(cnt))
    for obj in qbo.BagDict2:
        if(obj["name"]==try_name):
            return renameBagHelper(x,cnt+1)
    return try_name

def renameBag(x,newname):
    global qbo
    initBackend()
    for i, obj in enumerate(qbo.BagDict2):
        if(obj["name"]==x):
            qbo.renameBag(i,x,renameBagHelper(newname,0))
    endBackend()

def viewData(x):
    global qbo
    initBackend()
    retval= qbo.viewData(x)
    endBackend()
    return retval

def printForm(x):
    global qbo
    initBackend()
    retval= qbo.printForm(x)
    endBackend()
    return retval

def finalize(table,finalSchema,initialCount,finalCount):
    initBackend()
    whereString = ""
    colString = ""
    colCount=0
    whereCount=0
    for i in finalSchema:
        if(colCount==0):
            colString = colString + i[0]
            colCount = colCount+1
        else:
            colString = colString + " , "+ i[0]
            colCount = colCount+1
        if(i[1]!=None):
            sys.stderr.write("^^^"+str(i[0])+"^^^"+str(i[1])+"^^^");
            if(whereCount == 0):
                whereString = ' where ' + i[0] + " like '" +i[1] +"'"
                whereCount = whereCount +1
            else:
                whereString = whereString + "," + i[0] + " like '" + i[1] + "'"
                whereCount = whereCount +1
    sys.stderr.write("Finalize whereString: "+whereString +" colString: " + colString);
    if(initialCount==finalCount):
        colString ="*"
    for index,i in enumerate(qbo.BagDict2):
        if(i["name"] == table):
            oldsql = i["sql"]+ ' as ' + table
            newsql = "select "+colString+" "+oldsql[oldsql.find("from"):]+whereString
#            sys.stderr.write("---  "+ oldsql+ " ----")
#            sys.stderr.write("---  "+ newsql+ " ----")
            qbo.BagDict2[index]["sql"] = newsql
            sys.stderr.write("---- > "+ str(qbo.BagDict2[index]["sql"])+ "<-------")
            endBackend()
            return
    endBackend()
            
    
def getOperations(): 
    global qbo,d
    initBackend()
    retval=qbo.OperationsList
    endBackend()
    return retval

