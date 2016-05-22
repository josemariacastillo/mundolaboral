% include('header.tpl', title='MundoLaboral ')
<div class="row">
	<div class="col-md-10 col-md-offset-1">
<div class="row">
%for index, i in enumerate(ofertas["offers"]):
	%if index%3==0:
		%if index != 0:
			</div>
		%end
		<div class="row">
	%end
<div class="col-md-4" >
	<div class="box-gray">
       	<div class="box-gray">
			<h3><a href="{{i["author"]["uri"]}}" target="_blank">{{i["title"]}}</a></h3>
			<p><b>Estudios:</b> {{i["study"]["value"]}}</p>
			<p><b>Empresa:</b> {{i["author"]["name"]}}</p>
			<p><b>Jornada:</b> {{i["workDay"]["value"]}}</p>
			<p><b>Experiencia:</b> {{i["experienceMin"]["value"]}}</p>
			<p><b>Tipo de Contrato:</b> {{i["contractType"]["value"]}}</p>
			<p><b>Categoría:</b> {{i["category"]["value"]}}</p>
			<p><b>Requerimientos:</b> {{i["requirementMin"]}}</p>
			<p><b>Salario Máximo:</b> {{i["salaryMax"]["value"]}}</p>
		</div>
	</div>
</div>	

%end
	</div>
</div>
</div>
</div>
% include('footer.tpl')
