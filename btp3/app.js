var app=angular.module('qbo',[]);

app.controller('qbo_controller_1',function($scope,$http){
    top_scope=this;
    this.screen_no=1;
    this.all_tables=null;
    this.op_tables=null;
    this.test_variable = null;
    this.first_selected_table_name=null;
    this.first_selected_table=null;
    this.second_selected_table=null;
    this.operations_list = 'old1';
    this.showGranularity = 0;
    this.granularityForm = 'old';
    $scope.GranularityForm = {
	checked : {},
	value : {}};
    this.firstTableAttributes =null;
    this.secondTableAttributes = null;
    this.tableDetails=tableDetails;
    //tables_url='file:///home/lakshitarora/Desktop/qbo-browser/qbo-browser/btp3/getTables.html';//http://10.2.56.178:9999/cgi/getTables.py';
    tables_url='/getTables.html';//http://10.2.56.178:9999/cgi/getTables.py';
    this.the_data='initial';
    this.table_cols=[{'abcd':'efgh'}];//table_cols_global;
    this.todoText='initial todotext';
    $http({method: 'GET', url: tables_url}).
	success(function(data, status, headers, config) {
	    // this callback will be called asynch ronously
	    // when the response is available
	    top_scope.all_tables=data;
	    
	}).
	error(function(data, status, headers, config) {
	    alert('Backend connection failed');
	});

    second_table_url = "/getTableOperations.html";
	$http({method: 'GET', url: second_table_url}).
	success(function(data, status, headers, config) {
	    // this callback will be called asynchronously
	    // when the response is available
	    top_scope.op_tables=data;
	}).
	error(function(data, status, headers, config) {
	    top_scope.the_data='failed';
	});

    this.selectFirstTable=function(table_in){
	this.first_selected_table=table_in;
	this.first_selected_table_name=table_in.tablename;
	// so instead of above call, i will copy the hard coded data for now
	top_scope.showGranularity=0;
        this.firstTableAttributes = null;
	top_scope.second_table_options=top_scope.op_tables[table_in.tablename];
	this.screen_no+=1;// proceed to next screen
    };
    this.goBack=function(){
	this.screen_no-=1;
    }
    this.selectSecondTable=function(table){
	top_scope.showGranularity=0;
	this.second_selected_table=table;
	//TODO: need to change below from table.name to table.tablename
	this.second_selected_table_name=table.name;
	var first_table=top_scope.first_selected_table_name;
	this.todoText = top_scope.op_tables[first_table];
	this.secondTableAttributes = null;
	for(i =0 ; i< top_scope.op_tables[first_table].length;i++){
		//TODO: need to change below from table.name to table.tablename
		if(top_scope.op_tables[first_table][i].name === table.name)
			top_scope.operations_list= top_scope.op_tables[first_table][i].ops;
	}
	this.screen_no=3; //proceed to two-table operation selection screen
    }
    this.granularityFormVisibility = function(table,table_number){
	top_scope.showGranularity=top_scope.showGranularity==table_number ? 0 : table_number;
	top_scope.granularityForm = top_scope.tableDetails[table];
	var alreadyGranulared = true
	if(top_scope.showGranularity == 1 && top_scope.firstTableAttributes != null)
		top_scope.GranularityForm = top_scope.firstTableAttributes;
	else if (top_scope.showGranularity== 2 && top_scope.secondTableAttributes != null)
		top_scope.GranularityForm = top_scope.secondTableAttributes;
	else{
		top_scope.GranularityForm = {checked:{},value:{}};
		alreadyGranulared = false
	}
	for(i=0; i<top_scope.tableDetails[table].length ; i++){
		var colName = top_scope.tableDetails[table][i];
		top_scope.todoText = colName;
		if(!alreadyGranulared){
		top_scope.GranularityForm.checked[colName.name] = false;
		top_scope.GranularityForm.value[colName.name] = "";
		}
	}
	//top_scope.test_variable = top_scope.tableDetails[table];
    }
    $scope.selectGranularity=function(){
	top_scope.todoText='';    
    }
    $scope.changeGranularity=function(){
	if(top_scope.showGranularity == 1 )
		top_scope.firstTableAttributes = top_scope.GranularityForm;
	else if(top_scope.showGranularity == 2)
		top_scope.secondTableAttributes = top_scope.GranularityForm;  
	top_scope.todoText = "nicccce"; 
    }
});

var all_tables_trial=[{
    name: 'Table1',
    descr:'The one and only table',
},{
    name: 'Table2',
    descr:'The one and only table',
},{
    name: 'Table3',
    descr:'The one and only table',
},{
    name: 'Table4',
    descr:'The one and only table',
},{
    name: 'Table5',
    descr:'The one and only table',
}];

var op_tables=[{
    name:'Table 4',
    ops:['1_4_op1','1_4_op2','1_4_op3'],
},{
    name:'Table 5',
    ops: ['1_5_op1','1_5_op2']
}];

var tableDetails = {
	'Book_Copy' : [{name:'Book_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'ISBN', bool:0, toShow:1, defaultVal:"",},
		     {name:'isReference', bool:1, isSelected:1, defaultVal:"False",}],
	'Book_Type' : [{name:'ISBN', bool:0, toShow:1, defaultVal:"",},
		     {name:'BookAuthor', bool:0, toShow:1, defaultVal:"",},
		     {name:'BookEdition', bool:0, toShow:1, defaultVal:"",},
		     {name:'BookName', bool:0, isSelected:1, defaultVal:"",}],
	'Customer' :  [{name:'Customer_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'name', bool:0, toShow:1, defaultVal:"",},
		     {name:'email', bool:0, toShow:1, defaultVal:"",},
		     {name:'roll_no', bool:0, isSelected:1, defaultVal:"",}],
	'Issue'    :  [{name:'Issue_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'Book_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'Issue_date', bool:0, toShow:1, defaultVal:"",},
		     {name:'expiry_date', bool:0, toShow:1, defaultVal:"",},
		     {name:'Staff_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'Customer_ID', bool:0, isSelected:1, defaultVal:"",}],
	'Returns'  : [{name:'Book_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'Issue_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'Returns_Date', bool:0, toShow:1, defaultVal:"",},
		     {name:'Staff_ID', bool:0, isSelected:1, defaultVal:"",}],
	'Staff'    : [{name:'Staff_ID', bool:0, toShow:1, defaultVal:"",},
		     {name:'name', bool:0, toShow:1, defaultVal:"",},
		     {name:'email', bool:0, toShow:1, defaultVal:"",},
		     {name:'phone_number', bool:0, isSelected:1, defaultVal:"",}]};
