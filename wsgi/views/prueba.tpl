% include('header.tpl', title='Temperaturas ')
%for i in ofertas["offers"]:
			<h2>Titulo:{{i["title"]}}</h2>
			<p>Estudios:{{i["study"]["value"]}}</p>
			<p>URL:{{i["author"]["uri"]}}</p>
			<p>Empresa:{{i["author"]["name"]}}</p>
			<p>Salario:{{i["salaryPeriod"]["value"]}}</p>
			<p>Jornada:{{i["workDay"]["value"]}}</p>
			<p>Experiencia:{{i["experienceMin"]["value"]}}</p>
			<p>Tipo de Contrato:{{i["contractType"]["value"]}}</p>
			<p>Categoría:{{i["category"]["value"]}}</p>
			<p>Requerimientos:{{i["requirementMin"]}}</p>
			<p>Salario Máximo:{{i["salaryMax"]["value"]}}</p>
%end
% include('footer.tpl')