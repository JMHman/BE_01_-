from flask import Flask
from flask_smorest import Api
from db import db
import yaml
# from models.posts import Post # 타임스템프 적용 할줄 몰라서 워크벤치에서 만듬 ㅠㅠ

app = Flask(__name__)

# 데이터베이스 정보 유출을 막기위해 외부에 키값을 지정하여 사용 하는 코드
db_info = yaml.load(open('db.yaml'), Loader= yaml.FullLoader)
app.config['SQLALCHEMY_DATABASE_URI'] = db_info['database_uri']

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:4887@localhost/ozcoding'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

from routes.posts import post_blp

api.register_blueprint(post_blp)

from flask import render_template

@app.route('/')
def posting_page():
  return render_template('posts.html')

if __name__ == '__main__':
  with app.app_context():
    print("here?")
    db.create_all()
  
  app.run(debug=True)