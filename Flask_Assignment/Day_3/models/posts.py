from db import db
# 기회가 되면 모듈로 사용하는 법을 배워서 만들어 보자. 테이블 이름은 바꿔야 함
class Post(db.Model):
  __tablename__ = "posts"

  id = db.Column(db.Integer, primary_key=True) # 게시글 번호, 자동 증가
  title = db.Column(db.String(100), unique=True, nullable=False) # 게시글 제목, null 안됨
  content = db.Column(db.Text) # 게시글 내용 비어있어도 됨
  # create_at = db.Column(db.TIMESTAMP) # TIMESTAMP, 기본값 CURRENT_TIMESTAMP 이렇게 만들고 싶은데 아직 사용 법 모름
