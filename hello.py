from __future__ import print_function
import os
import uuid
from flask import Flask, render_template
from cfenv import AppEnv
import time
from pprint import pformat


env = AppEnv()
app = Flask(__name__)

start = time.time()

from flask import request

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def hello():
    now = time.time()
    uptime = now-start
    m, s = divmod(uptime, 60)
    uptime = "%02dm%02ds" % (m, s)
    return render_template("index.html",index=env.index,uptime=uptime)

@app.route('/exit')
def exit():
    now = time.time()
    uptime = now-start
    m, s = divmod(uptime, 60)
    uptime = "%02dm%02ds" % (m, s)
    shutdown_server()
    return render_template("exit.html",index=env.index,uptime=uptime)

@app.route('/env')
def showenv():
    return render_template("env.html",env=os.environ)

@app.route('/port')
def port():
    return env.port

@app.route('/index')
def index():
    return env.index

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=env.port)
