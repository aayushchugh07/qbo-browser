var app=angular.module('qbo',[]);

app.controller('qbo_controller_1',function($scope,$http){
    top_scope=this;
    this.screen_no=1;
    this.all_tables=null;
    this.op_tables=null;
    this.test_variable = null;
    this.first_selected_table_name=null;
    this.second_selected_table_name=null;
    this.first_selected_table=null;
    this.second_selected_table=null;
    this.operations_list = 'old1';
    this.showGranularity = 0;
    this.granularityForm = 'old';
    this.GranularityForm = {
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
    this.db_data="Processing query.....";
    this.db_headers=[]
    this.screen_no_stack=[]
    this.record_count_text='Nothing Selected'; //for 'view data screen'
    this.operation_text=" (Nothing) " //for 'view data screen'
    this.allow_object_select=false;
    this.object_select_allowed_for=""; //name of table for which allow_object_select is true
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
	top_scope.goToNextScreen();// proceed to next screen
	this.todoText = this.tableDetails[table_in.tablename];
	for(i=0;i<this.tableDetails[table_in.tablename].length;i++){
		var colName = top_scope.tableDetails[table_in.tablename][i];
		this.GranularityForm.checked[colName.name] = true;
		this.GranularityForm.value[colName.name] = "";
	}
    };
    this.goBack=function(){
	next_screen=1;
	if(top_scope.screen_no_stack.length>0)
	    next_screen=top_scope.screen_no_stack.pop();
	top_scope.screen_no=next_screen;
    }
    this.goToScreen=function(next_screen){
	top_scope.screen_no_stack.push(top_scope.screen_no);
	top_scope.screen_no=next_screen;
    }
    this.goToNextScreen=function(){
	top_scope.screen_no_stack.push(top_scope.screen_no);
	top_scope.screen_no=top_scope.screen_no+1;
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
		if(top_scope.op_tables[first_table][i].name === table.name){
		        top_scope.operations_list=top_scope.op_tables[first_table][i].ops;
		}
	}
	for(i=0;i<this.tableDetails[table.name].length;i++){
		var colName = top_scope.tableDetails[table.name][i];
		this.GranularityForm.checked[colName.name] = true;
		this.GranularityForm.value[colName.name] = "";
	}
	top_scope.goToScreen(3); //proceed to two-table operation selection screen
    }
    this.granularityFormVisibility = function(table,table_number){
	top_scope.showGranularity=(top_scope.showGranularity==table_number ? 0 : table_number);
	top_scope.granularityForm = top_scope.tableDetails[table];
	//var alreadyGranulared = true
	/*if(top_scope.showGranularity == 1 && top_scope.firstTableAttributes != null)
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
	}*/
	//top_scope.test_variable = top_scope.tableDetails[table];
    }
    $scope.selectGranularity=function(){
	top_scope.todoText='';    
    }
    this.updateHeaders=function(){
	//remove the headers for which no data exists in any row
	to_keep={};
	for(column_no in top_scope.db_headers){
	    to_keep[top_scope.db_headers[column_no]]=false;
	}
	for(data_point_no in top_scope.db_data){
	    data_point=top_scope.db_data[data_point_no];
	    for(column in to_keep)
		if(data_point[column])to_keep[column]=true;
	}
	var db_headers=[];
	for(column in to_keep){
	    if(to_keep[column])
		db_headers.push(column);
	}
	top_scope.db_headers=db_headers;
    }
    this.selectOneObject=function(tuple_data){
	table_name=top_scope.object_select_allowed_for;
	db_headers=top_scope.db_headers;
	for (var header_i=0;header_i<db_headers.length;header_i++){
	    var key=db_headers[header_i];
	    top_scope.GranularityForm.value[key]=tuple_data[key];
	    top_scope.GranularityForm.checked[key]=true;
	}
	var table_number;
	if(table_name==top_scope.first_selected_table_name)table_number=1;
	else table_number=2;
	top_scope.showGranularity=0; //because granularityFormVisibility will toggle the granularity
	top_scope.granularityFormVisibility(table_name,table_number);
	top_scope.goBack();
	
	
    }
    this.clearGranularity=function(){
	var formvals=top_scope.GranularityForm.value;
	for (valkey in formvals){
	    formvals[valkey]="";
	}
	var formchecked=top_scope.GranularityForm.checked;
	for (checkedkey in formchecked){
	    formchecked[checkedkey]=true;
	}
    }
    this.selectOperation=function(operation_name,operation_desc_){
	query_url="/cgi/new_query.py?queryname="+operation_name;
	top_scope_new=this;
	this.todoText = "yoyo";
	$http({method: 'GET', url: query_url}).
	success(function(data, status, headers, config) {
	    // this callback will be called asynch ronously
	    // when the response is available

	    top_scope.db_data=data;
	    top_scope.db_headers=[];
	    // updating table headers for displaying db_data


	    var local_data = [];
	    for(i=0;i<data.length;i++){
		local_dict = {};
		var to_keep = 1;
		for(key in top_scope.GranularityForm.value){
		    if(key in data[i])
				if(top_scope.GranularityForm.value[key]!= "" && -1==data[i][key].search(new RegExp(top_scope.GranularityForm.value[key],"i"))){
					//top_scope.todoText = data[i];
					to_keep=0;
				}
		}
	        if(to_keep){
			for(key in top_scope.GranularityForm.checked)
				if(key in data[i])
					if(top_scope.GranularityForm.checked[key]==true)
						local_dict[key] = data[i][key];
			local_data.push(local_dict);
		}
		//top_scope.todoText = data[i];
	    }
	    if(local_data.length>0){
		var data_point=local_data[0];
		for (column in data_point){
		    if(column!="_is_shown"){
			top_scope.db_headers.push(column);
		    }
		}
	    }
	    top_scope.updateHeaders();
	    top_scope.db_data=local_data;
	    top_scope.record_count_text="Total "+String(top_scope.db_data.length);
	    top_scope.operation_text=operation_desc_;
	    // update allow_object_select, for selecting object-level instead of class-level. 
	    // first search in list HACK!
	    tables_list=['Book_Type','Book_Copy','Customer','Issue','Returns','Staff'];
	    top_scope.allow_object_select=false;
	    for(var ti=0;ti<tables_list.length;ti++){
		if(operation_name==tables_list[ti]){
		    top_scope.allow_object_select=true;
		    top_scope.object_select_allowed_for=operation_name;
		}
	    }
	    top_scope.goToScreen(4);
	}).
	error(function(data, status, headers, config) {
	    alert('Query failed');
	});
    };
    $scope.changeGranularity=function(){
	//if(top_scope.showGranularity == 1 )
	  //  top_scope.firstTableAttributes = top_scope.GranularityForm;
	//else if(top_scope.showGranularity == 2)
	  //  top_scope.secondTableAttributes = top_scope.GranularityForm;  
	top_scope.todoText = "nicccce"; 
    };
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
