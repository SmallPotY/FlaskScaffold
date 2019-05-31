# -*- coding:utf-8 -*-
from flask import render_template

from application import app
# from web.controllers.wx import wx
# from web.controllers.admin.login import route_admin
# from web.controllers.backstage import api

# app.register_blueprint(wx, url_prefix='/wx')
# app.register_blueprint(api, url_prefix='/api')
# app.register_blueprint(route_admin, url_prefix='/')


@app.route('/')
def index():
    return render_template('index.html')
