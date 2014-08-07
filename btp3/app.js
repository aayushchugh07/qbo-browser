var app=angular.module('qbo',[]);

app.controller('qbo_controller_1',function(){
    this.screen_no=1;
    this.tables=all_tables;
    this.first_selected_table=''
    this.selectTable=function(table_name){
	this.screen_no%=2;
	this.screen_no+=1;
	if(this.screen_no==1){
	    this.first_selected_table=table_name;
	    
	}
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
},{
    name: 'Table2',
},{
    name: 'Table3',
},{
    name: 'Table4',
},{
    name: 'Table5',
}];

var op_tables=[{
    name:'Table 4',
    ops:['1_4_op1','1_4_op2','1_4_op3'],
},{
    name:'Table 5',
    ops: ['1_5_op1','1_5_op2']
}];
