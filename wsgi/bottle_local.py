from bottle import run
import os
os.environ['OPENSHIFT_REPO_DIR']="mundolaboral"
import mybottleapp
run(host='0.0.0.0', port=8080, debug=True)