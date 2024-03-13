from django.db import models
from common.models import CommonModel
from users.models import User
from reviews.models import Review
# Create your models here.
#  제목(title), 내용(content), 작성자(user)
# Feed 와 User 의 관계
# User = [Feed,Feed,Feed,...,Feed] O
# Feed = [User,User,User] X
# User : Feed = 1 : N

class Feed(CommonModel):

  def default_title():
    return User.objects.first().username if User.objects.exists() else "Default Title"
  title = models.CharField(max_length=30,default=default_title)
  # content = models.CharField(max_length=200)
  
  user = models.ForeignKey('users.User', on_delete=models.CASCADE)
  reviews = models.ForeignKey(Review, related_name='feed_reviews', on_delete=models.SET_NULL, null=True)
