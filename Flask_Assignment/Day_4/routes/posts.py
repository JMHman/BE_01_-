from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
  posts_blp = Blueprint('posts',__name__,description='posts api', url_prefix='/posts')

  @posts_blp.route('/', methods=['GET','POST'])
  def posts():
    cursor = mysql.connection.cursor()
    #게시글 조회
    if request.method == 'GET':
      set = "SELECT * FROM posts"
      cursor.execute(set)
      
      posts = cursor.fetchall() # 전체 데이터 조회
      cursor.close()

      post_list = []

      for post in posts:
        post_list.append({
          'id': post[0],
          'title': post[1],
          'content': post[2] # create_at는 타임스탬프기 때문에 때로 신경 쓸 필요가 없다
        })
      
      return jsonify(post_list)
    
    # 게시글 생성
    elif request.method == 'POST':
      title = request.json.get('title')
      content = request.json.get('content')

      if not title or not content:
        abort(400, message="title or content can't be empty")

      sql = "INSERT INTO posts(title, content) VALUES(%s,%s)"
      cursor.execute(sql, (title, content))
      mysql.connection.commit()
      
      return jsonify({"msg":"successfully created post data" , "title":title , "content":content}), 201
    
  # 1개의 게시글만 조회하고 싶은 경우
  # 게시글 수종 및 삭제
  @posts_blp.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
  def post(id):
    cursor = mysql.connection.cursor()
    spl = f"SELECT * FROM posts WHERE id = {id}"
    cursor.execute(spl)
    post = cursor.fetchone()
    
    if request.method == 'GET':

      if not post:
        abort(404, message=f'post {id} not found')
      # return jsonify(post)
      return ({
        'id': post[0],
        'title': post[1],
        'content': post[2]
      })
    elif request.method == 'PUT':
      # data = request.json
      # title = data['title']
      # content = data['content']

      title = request.json.get("title")
      content = request.json.get("content")

      if not title or not content:
        abort(400, message="not found title or content")

      if not post:
        abort(404, message=f'post {id} not found')

      sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"
      cursor.execute(sql,(title, content,id))
      # sql = f"UPDATE posts SET title = {title}, content = {content} WHERE id = {id}"
      # cursor.execute(sql)
      mysql.connection.commit()

      return jsonify({"msg":"successfully updated post data", "title":title, "content":content}), 201
    
    elif request.method == 'DELETE':
      if not post:
        abort(404, message=f'post {id} not found')
      sql = f"DELETE FROM posts WHERE id = {id}"
      cursor.execute(sql)
      mysql.connection.commit()

      return jsonify({"msg":"successfully deleted post data"}), 201
  
  return posts_blp


# 몰입 - 황농문 교수님