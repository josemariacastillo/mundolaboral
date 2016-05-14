from bottle import route,request, default_app, template, run, static_file, error
import requests
import json

headers = {'Authorization': 'Basic NGU5MzU0YzBiMWFlNGY3ZTlkNzU5MGE2NDMzM2YwMjI6RHU5eXpiQnd6M2JsUWhOeFRKZ0syckJUMWRjYUE0M0ZudnpDcTZDTVdRRjdoVERoaVg='}
r=requests.get('https://api.infojobs.net/api/1/offer',headers=headers)



@route('/ofertas')
def ofertas():

	if r.status_code==200:
		dic=json.loads(r.text)
	return template('prueba.tpl',ofertas=dic)
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='localhost', port=8080, debug=True)


