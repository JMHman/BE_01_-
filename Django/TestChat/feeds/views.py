from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
from .serializers import FeedSerializer, FeedListSerializer

# Create your views here.

# api/v1/feeds [POST]



class Feeds(APIView):
  # 전체 게시글 데이터 조회 
  def get(self, request):
    feeds = Feed.objects.all()

    # 객체 -> json (시리얼 라이즈)
    serializer = FeedSerializer(feeds, many=True) # 필즈는 데이터가 많을거기 때문에 매니=트루를 한다.
    
    return Response(serializer.data)
  
  def post(self, request):
    # Feed.objects.create()
    # 역직렬화 (클라이언트가 보내준 json => object)
    serializer = FeedSerializer(data=request.data)
    
    if serializer.is_valid(): # save 를 사용하기 위해서는 is_valid 가 필요하다
    # 데이터가 성공적이로 생성이 되었는지 보여주기 위한 코드
      feed = serializer.save(user=request.user)
      serializer = FeedSerializer(feed)
      # print("post serializer", serializer)

      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
    # 그냥 저장만 하고 된건지만 간단히 확인할떄 코드
    # serializer.save(user=request.user)
    # return Response('success/저장 완료',)

# class FeedList(APIView):
#   def get(self, request):
#     feeds = Feed.objects.all()
#     serializer = FeedListSerializer(feeds, many=True)
#     return Response(serializer.data)
class FeedList(APIView):
  def get(self, request):
    feeds = Feed.objects.all()
    serializer = FeedSerializer(feeds, many=True)
    return Response(serializer.data)





from rest_framework.exceptions import NotFound

class FeedDetail(APIView):
  def get_object(self, feed_id):
    try:
      return Feed.objects.get(id=feed_id)
      # 둘다 사용가능
      # feed = Feed.objects.get(id=feed_id)
      # return feed
    except Feed.DoesNotExist:
      raise NotFound

  def get(self, request, feed_id): # 클래스 안에 함수에는 셀프를 붙여줘야 한다.
    feed = self.get_object(feed_id)
    # feed (object) => json => serializer

    serializer = FeedSerializer(feed)
    # print(serializer)
    
    return Response(serializer.data)