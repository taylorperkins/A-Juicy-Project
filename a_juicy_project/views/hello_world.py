from flask import render_template

from a_juicy_project import app


@app.route('/hello_world/<name>')
def hello_world(name):
    return render_template('index/index.html', name=name)
