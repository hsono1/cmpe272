#!/usr/bin/env python

from flask import Flask, render_template, request
from flask_appcache import Appcache
# import config
import requests
import json


app = Flask(__name__)
app.secret_key = "mysecretkey"

appcache = Appcache(app)
appcache.add_folder("static", base="/static")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/auth")
def auth():
    res = requests.post('https://api.inbenta.io/v1/auth', data={"secret": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0IjoiaHNvbm9fY2hhdGJvdF9lbiJ9.Tq8OnCaYckr2jOscr78bQnYUaZcy3ICL3Y7bONFMItO3acKPIjPjVlYhxIK8i7EpNyGj132BT_w-o3umBNgz8A"}, headers={'x-inbenta-key':'ftVsa1WaLaXDX4BSBD5+0vmqogToTo1g+3FxXwcg2Bs='})
    print('res', res.json())
    if res.status_code == 200:
        return json.dumps(res.json())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)