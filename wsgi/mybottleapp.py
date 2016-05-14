from bottle import route,request, default_app, template, run, static_file, error
import requests
import json

headers = {'Authorization': 'Basic NGU5MzU0YzBiMWFlNGY3ZTlkNzU5MGE2NDMzM2YwMjI6RHU5eXpiQnd6M2JsUWhOeFRKZ0syckJUMWRjYUE0M0ZudnpDcTZDTVdRRjdoVERoaVg='}
r=requests.get('https://api.infojobs.net/api/1/offer',headers=headers)


@route('/')
def inicio():
	return template('index.tpl')
@route('/ofertas')
def ofertas():
	if r.status_code==200:
		dic=json.loads(r.text)
	return template('prueba.tpl',ofertas=dic)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')



# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
