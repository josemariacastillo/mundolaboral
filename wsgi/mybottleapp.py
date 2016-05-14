from bottle import default_app, get, post, template, request, static_file, response,redirect
import requests
import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError



client_id='4e9354c0b1ae4f7e9d7590a64333f022'
client_secret='Du9yzbBwz3blQhNxTJgK2rBT1dcaA43FnvzCq6CMWQF7hTDhiX'
redirect_uri = 'http://mundolaboral-josemccotaniesgn.rhcloud.com/callback'
scope = ['cv']
token_url = "https://www.infojobs.net/oauth/authorize"




@get('/listacv')
def get_token():
	if r.status_code==200:
		r="hola"
		
    return template('listacv.tpl',respuesta=r)


def token_valido():
  token=request.get_cookie("token", secret='some-secret-key')
  if token:
    token_ok = True
    try:
      oauth2 = OAuth2Session(client_id, token=token)
      r = oauth2.get('https://api.infojobs.net/api/1/curriculum')
    except TokenExpiredError as e:
      token_ok = False
  else:
    token_ok = False
  return token_ok

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
