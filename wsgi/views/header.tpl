<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MundoLaboral</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="" />
<meta name="author" content="http://bootstraptaste.com" />
<!-- css -->
<link type="text/css" href="/static/css/bootstrap.min.css" rel="stylesheet" />
<link type="text/css" href="/static/css/fancybox/jquery.fancybox.css" rel="stylesheet">
<link type="text/css" href="/static/css/jcarousel.css" rel="stylesheet" />
<link type="text/css" href="/static/css/flexslider.css" rel="stylesheet" />
<link type="text/css" href="/static/css/style.css" rel="stylesheet" />


<!-- Theme skin -->
<link href="/static/skins/default.css" rel="stylesheet" />
<script src="https://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ=" crossorigin="anonymous"></script>



</head>
<body>
<div id="wrapper">
	<!-- start header -->
	<header>
        <div class="navbar navbar-default navbar-static-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="index.html">MundoLaboral</a>
                </div>
                <div class="navbar-collapse collapse ">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="/">Inicio</a></li>
                        <li class="dropdown">
                            <a class="dropdown-toggle " data-toggle="dropdown" data-hover="dropdown" data-delay="0" data-close-others="false">Geocalizar Ofertas<b class=" icon-angle-down"></b></a>
                            <ul class="dropdown-menu">
                                <li><form action="/resultado" method="post">
                                      Busqueda:<input name="busqueda" type="text" />
                                               <input value="resultado" type="submit"/>
                                           
                                    </form></li>
                               
                            </ul>
                        </li>
                        <li><a href="/ofertas">Lista de Ofertas</a></li>
                        
                    </ul>
                </div>
            </div>
        </div>
	</header>
	<!-- end header -->