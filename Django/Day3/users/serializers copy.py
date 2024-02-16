from rest_framework.serializers import ModelSerializer
from .models import User


class MyInfoUserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"
    # fields = ("username", "email",)

class FeedUserSerializer(ModelSerializer):
  class Meta:
    madel = User # m'a'del / m'o'del  a 랑 o 랑 잘 보기 
    # fields = '__all__'
    fields = ("username", "email",)
    