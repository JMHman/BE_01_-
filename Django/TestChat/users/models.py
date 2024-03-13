from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  is_business = models.BooleanField(default=False)
  grade = models.CharField(max_length=10, default= 'C')

  def __str__(self):
    return self.username
  
# class User(models.Model):
#   name = models.CharField(max_length=30) # 이
#   description = models.TextField() # 긴 문자열
#   age = models.PositiveIntegerField(null=True)
#   gender = models.CharField(max_length=6)

#   def __str__(self):
#     # return self.name
#     return f'{self.name} / {self.age}살'
  
