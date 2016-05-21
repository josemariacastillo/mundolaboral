from bottle import route,default_app, get, post, template, request, static_file, response,redirect
#from requests_oauthlib import OAuth2Session
#from oauthlib.oauth2 import TokenExpiredError
import requests
import json
import unicodedata


headers = {'Authorization': 'Basic NGU5MzU0YzBiMWFlNGY3ZTlkNzU5MGE2NDMzM2YwMjI6RHU5eXpiQnd6M2JsUWhOeFRKZ0syckJUMWRjYUE0M0ZudnpDcTZDTVdRRjdoVERoaVg='}
re=requests.get('https://api.infojobs.net/api/1/offer',headers=headers)



@route('/')
def inicio():
  
  return template('index.tpl')

@route('/ofertas')
def ofertas():
	if re.status_code==200:
		dic=json.loads(re.text)
	return template('prueba.tpl',ofertas=dic)



@route('/resultado',method='POST') 
def resultado():
  busqueda=request.forms.get('busqueda')
  headers = {'Authorization': 'Basic NGU5MzU0YzBiMWFlNGY3ZTlkNzU5MGE2NDMzM2YwMjI6RHU5eXpiQnd6M2JsUWhOeFRKZ0syckJUMWRjYUE0M0ZudnpDcTZDTVdRRjdoVERoaVg='}
  payload = {'q':busqueda}
  r=requests.get('https://api.infojobs.net/api/1/offer',headers=headers,params=payload)
  if r.status_code==200:
    dic=json.loads(r.text)
    ciudades={}
    for i in dic["offers"]:
      ciudad = unicodedata.normalize('NFKD', i["city"]).encode('ascii','ignore')
      if ciudades.has_key(ciudad):
        lista = ciudades.get(ciudad)
      else:
        lista = []
      titulo = unicodedata.normalize('NFKD', i["title"]).encode('ascii','ignore')
      url = unicodedata.normalize('NFKD', i["link"]).encode('ascii','ignore')
      lista.append({'titulo':titulo, 'url':url})
      ciudades[ciudad]=lista
        
    datos=json.dumps(ciudades)

  else:
    print r.status_code
  return template('mapa.tpl',ci=ciudades)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')



# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
