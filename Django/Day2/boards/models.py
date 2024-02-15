from django.db import models
from common.models import CommonModel
# Create your models here.

# 게시글
# - title
# - content
class Board(CommonModel): # CommonModel 이 이미 models.Model 을 가지고 있기 때문에 그냥 사용하면 된다
  title = models.CharField(max_length=30)
  content = models.TextField()
  writer = models.CharField(max_length=30)
  date = models.DateTimeField(auto_now_add=True)
  likes = models.PositiveIntegerField(default=0)
  reviews = models.PositiveIntegerField(default=0)
  
  user = models.ForeignKey('users.User',on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title