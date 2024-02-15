from flask import request, jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models.posts import Post

post_blp = Blueprint('posts',__name__,description='Operaions on posts', url_prefix='/posts')

@post_blp.route('/')
class PostList(MethodView):
  def get(self):
    posts = Post.query.all()

    return jsonify([{'id':post.id,
                'title':post.title,
                'content':post.content} for post in posts])
  
  def post(self):
    data = request.json
    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'msg': 'Good, posting'}), 201
  
@post_blp.route('/<int:post_id>')
class BoardResource(MethodView):
  def get(self,post_id):
    post = Post.query.get_or_404(post_id)

    return jsonify({'id':post.id,
                    'title':post.title,
                    'content':post.content})

  def put(self, post_id):
    post = Post.query.get_or_404(post_id)
    data = request.json

    post.title = data['title']
    post.content = data['content']

    db.session.commit()

    return jsonify({'msg':'Yse!! update post'}), 201

  def delete(self, post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return jsonify({'msg':'Oh,No... delete post'}), 204
  

