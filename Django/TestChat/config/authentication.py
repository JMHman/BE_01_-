from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from users.models import User
from rest_framework.exceptions import AuthenticationFailed

class JWTAuthentication(BaseAuthentication):
  def authenticate(self, request):
    token = request.headers.get("jwt-auth") # jwt token 은 해더, 페이로드, 시그니처데이터가 들어간다.
    
    if not token:
      return None
    
    # decoded = jwt.decode(token,
    #           settings.SECRET_KEY,
    #           algorithms=['HS256']) # 여러가지 얼고리즘이 있지만, HS256 이 업계 표준
    
    # print("decoded",decoded)
    
    # user_id = decoded.get('id')
    # user = User.objects.get(id=user_id)
    # return (user, None)
    
    
    try:  # 토큰을 확인한 후 다양한 오류 결과(예외처리)를 보여주기 위한 코드
      decoded = jwt.decode(token, 
                            settings.SECRET_KEY, 
                            algorithms=["HS256"])
      user_id = decoded.get("id")

      if not user_id:
        raise AuthenticationFailed("Invalid Token")

      user = User.objects.get(id=user_id)
      return (user, None)
    
    # 예외처리 코드들
    except jwt.ExpiredSignatureError: 
        raise AuthenticationFailed("Token has expired")
    except jwt.DecodeError:
        raise AuthenticationFailed("Error decoding token")
    except User.DoesNotExist:
      raise AuthenticationFailed("User not found")