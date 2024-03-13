from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.authentication import TokenAuthentication # 사용자 인증 (추가)
from rest_framework.permissions import IsAuthenticated # 권한 부여 (추가)

# Create your views here.
# api/v1/users [POST] => user 생성 API
class Users(APIView):
  def post(self, request):
    # password => 검증을 하고 해쉬화해서 저장 필요
    # the other => 비밀번호 외 다른 데이터들
    
    password = request.data.get('password')
    serializer = MyInfoUserSerializer(data=request.data)

    try:
      validate_password(password)
    except:
      raise  ParseError('Invalid password')
    
    if serializer.is_valid():
      user = serializer.save() # 새로운 유져 저장
      user.set_password(password)
      user.save()

      serializer = MyInfoUserSerializer(user)
      return Response(data=serializer.data)
    else:
      raise ParseError(serializer.errors)

# api/v1/users/myinfo ['GET','PUT']
# users/views.py


class MyInfo(APIView):
    authentication_classes = [TokenAuthentication] # 추가
    permission_classes = [IsAuthenticated] # 추가
    
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)

    # update
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

from django.contrib.auth import authenticate, login
from rest_framework import status
# api/v1/users/login
class Login(APIView):
  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
      raise ParseError()
    
    user = authenticate(request, username=username, password=password)
    
    if user:
      login(request, user)
      return Response(status=status.HTTP_200_OK)
    else:
      return Response(status=status.HTTP_403_FORBIDDEN)



from django.contrib.auth import logout
    # api/v1/users/login
class Logout(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    print("header : ",request.headers)
    logout(request)

    return Response(status=status.HTTP_200_OK)

from django.conf import settings
import jwt

class JWTLogin(APIView):
  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
      raise ParseError()
    
    user = authenticate(request, username=username, password=password)

    if user:
      payload = { "id":user.id , "username":user.username }
      
      token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm='HS256' # 넣어도 되고 안넣어도 되는 부분, 구분을 위해 이번엔 넣음
      )

      return Response({'token' : token})
    
from config.authentication import JWTAuthentication
class UserDtailView(APIView):
  # authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self, request):
    user = request.user

    return Response({"id": user.id,"username": user.username})
  

  

  
  