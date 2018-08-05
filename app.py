from flask import Flask, render_template,g, request, redirect, url_for
from redis import Redis
from flask_sqlalchemy import SQLAlchemy # 変更
from hamlish_jinja import HamlishExtension
from werkzeug import ImmutableDict
import os



class FlaskWithHamlish(Flask):
    jinja_options = ImmutableDict(
        extensions=[HamlishExtension]
    )
app = FlaskWithHamlish(__name__)
db_uri = os.environ.get('DATABASE_URL') or "postgresql://python:triple4649@pythonpostgres/python"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri # 追加
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) # 追加
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')
@app.route('/test')
def hello_world():
    return render_template('view/index.html') # 変更

@app.route('/regist_image')
def show_regist_image():
    return render_template('view/bas64.html') # 変更
    
    
@app.route('/imageentry', methods=['POST'])
def add_entry():
    from logic.mywebapp import add_Image_toDB
    add_Image_toDB(request.form)
    return redirect(url_for('show_regist_image'))
    
if __name__ == "__main__":
    #init()
    app.run(host="0.0.0.0", debug=True)

