#!/usr/bin/env python

print "Content-type: text/html"
print
# print "<html><head><title>Situation snapshot</title></head>"
# print "<body><pre>"
# print "fff"
# objects=['Book_copy','Book_'];
# for object in objects:
# 	print object;
# print "</pre></body></html>"

print '''<!DOCTYPE html>
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
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
              <li class="dropdown">
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
              </li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    <hr />
    <h3>Tables</h3>
    <p>Click on a table to add a new bag</p>
    <div class="row">
    <!-- Put elements below with div class=col-md-2 to get wrapping in columns -->
      <!-- div class="col-md-2">
        <h2>Heading</h2>
        <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
        <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
      </div -->
      <div class="col-md-1">
	<div align="center">
	  <img src="/images/People.png" width="60px" height="60px" />
	  </div>
	<p align="center">Customers</p>
      </div>
      <div class="col-md-1">
	<div align="center">
	  <img src="/images/People.png" width="60px" height="60px" />
	  </div>
	<p align="center">Customers</p>
      </div>
      <div class="col-md-1">
	<div align="center">
	  <img src="/images/People.png" width="60px" height="60px" />
	  </div>
	<p align="center">Customers</p>
      </div>

    </div> <!-- /row -->
    <hr />
    <h3>Bags</h3>
    <p>Select one or two bags to perform operations</p>
    <div class="row">
      <div class="col-md-1">
	<div align="center" style="padding-top: 12px;">
	  <img src="/images/People.png" width="60px" height="60px" />
	  </div>
	<p align="center">Customers</p>
      </div>

      <div class="col-md-2">
	<div class="panel panel-default">
          <div class="panel-heading">
	    <div align="center" class="dropdown-toggle" data-toggle="dropdown">
	      <img src="/images/People.png" width="60px" height="60px" align="center"/>
	      
	      <button class="btn btn-info dropdown-toggle" data-toggle="dropdown" data-hover="dropdown"><b class="caret"></b></button>
		
	      <ul class="dropdown-menu" align="center">
		<li><a tabindex="-1" href="#">View data</a></li>
		<li class="divider"></li>
		<li><a tabindex="-1" href="#">Deselect</a></li>
		<li><a tabindex="-1" href="#">Delete</a></li>
              </ul>
	      <p align="center">Customers</p>
	    </div>
          </div>
	</div>

      </div>
      
    </div>
    <hr />
    <h3>Operations</h3>
    <p>Click on an operation for selected table(s)</p>
    <div class="row">
      
      <div class="col-md-1">
	<div align="center">
	  <img src="/images/People.png" width="60px" height="60px" align="center"/>
	  <p align="center">Operation2</p>
	</div>
      </div>

      <div class="col-md-1">
	<div align="center">
	  <img src="/images/People.png" width="60px" height="60px" align="center"/>
	  <p align="center">Operation1</p>
	</div>
      </div>
    </div>
    
    <!-- /div -->

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="/js/bootstrap.min.js"></script>
    
      <!-- <div class="dropdown theme-dropdown clearfix"> -->
      <!--   <a id="dropdownMenu1" href="#" role="button" class="sr-only dropdown-toggle" data-toggle="dropdown" > -->
      <!-- 	   >Dropdown <b class="caret"></b></a > -->
      <!--   <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1" > -->
      <!--     <li class="active" role="presentation"><a role="menuitem" tabindex="-1" href="#">Action</a></li> -->
      <!--     <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Another action</a></li> -->
      <!--     <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Something else here</a></li> -->
      <!--     <li role="presentation" class="divider"></li> -->
      <!--     <li role="presentation"><a role="menuitem" tabindex="-1" href="#">Separated link</a></li> -->
      <!--   </ul > -->
      <!-- </div> -->
    
      <!-- <div class="btn-group"> -->
      <!--   <button class="btn btn-primary dropdown-toggle" data-toggle="dropdown" data-hover="dropdown">Primary <span class="caret"></span></button> -->
      <!--    <class="dropdown-menu"> -->
      <!-- 	<ul> -->
      <!--     <li><a href="#">Action</a></li> -->
      <!--     <li><a href="#">Another action</a></li> -->
      <!--     <li><a href="#">Something else here</a></li> -->
      <!--     <li class="divider"></li> -->
      <!--     <li><a href="#">Separated link</a></li> -->
      <!--   </ul> -->
      <!-- </div> <\!-- .btn-group -\-> -->
      
      <!-- <a href="#" class="dropdown-toggle js-activated" data-toggle="dropdown">Contact <b class="caret"></b></a> -->


  </body>
</html>
'''
