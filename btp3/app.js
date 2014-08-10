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
    //tables_url='file:///home/lakshitarora/Desktop/qbo-browser/qbo-browser/btp3/getTables.html';//http://10.2.56.178:9999/cgi/getTables.py';
    tables_url='http://localhost:8000/getTables.html';//http://10.2.56.178:9999/cgi/getTables.py';
    this.the_data='initial';
    $http({method: 'GET', url: tables_url}).
	success(function(data, status, headers, config) {
	    // this callback will be called asynchronously
	    // when the response is available
	    top_scope.all_tables=data;
	    
	}).
	error(function(data, status, headers, config) {
	    top_scope.the_data='failed';
	});

    second_table_url = "http://localhost:8000/getTableOperations.html";
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
	this.first_selected_table_name=table_in.name;
	
	// so instead of above call, i will copy the hard coded data for now
	
        
	top_scope.second_table_options=top_scope.op_tables[table_in.name];
	this.screen_no+=1;// proceed to next screen
    };
    this.goBack=function(){
	this.screen_no-=1;
    }
    this.selectSecondTable=function(table){
	this.second_selected_table=table;
	this.second_selected_table_name=table.name;
	for(i =0 ; i< top_scope.op_tables[table.name].length;i++){
		if(top_scope.op_tables[table.name][i].name === table.name)
			top_scope.operations_list= top_scope.op_tables[table.name][i].ops;
	}

	this.screen_no=3; //proceed to two-table operation selection screen
    }
});

/* 
// this is from the demo code, it is useless  
var gems=[{
    name: 'Dodecahedron',
    price: 2.95,
    description: 'The one and only gem',
    canPurchase: false,
},{
    name: 'Dodecahedron',
    price: 2.95,
    description: 'The one and only gem',
    canPurchase: true,
}];
*/

var all_tables=[{
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
