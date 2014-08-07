var app=angular.module('qbo',[]);

app.controller('qbo_controller_1',function(){
    this.screen_no=1;
    this.all_tables=all_tables;
    this.first_selected_table_name=null;
    this.first_selected_table=null;
    this.selectFirstTable=function(table_in){
	this.first_selected_table=table_in;
	this.first_selected_table_name=table_in.name;
	// $http({method: 'GET', url: '/someUrl'}).
	//     success(function(data, status, headers, config) {
	// 	// this callback will be called asynchronously
	// 	// when the response is available
	//     }).
	//     error(function(data, status, headers, config) {
	// 	// called asynchronously if an error occurs
	// 	// or server returns response with an error status.
	//     });
	
	// so instead of above call, i will copy the hard coded data for now
	this.second_table_options=op_tables;
	this.screen_no+=1;
    };
    this.goBack=function(){
	this.screen_no-=1;
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
