from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):

  user = FeedUserSerializer(read_only=True)
  # 리뷰가 피드에 자녀속성이기 때문에 리뷰에 셋을 붙여줘야 한다(역참조)
  # 리뷰는 많이 달리수있으니 매니 트루 해줘야 한다
  review_set = ReviewSerializer(many=True, read_only=True)

  class Meta:
    model = Feed
    fields = '__all__'
    # 현제 모델과 연결된 모델들까지 serialize/직렬화 해라
    # 피드 - 유저 모델 > 현제 코드는 피드 모델 객체를 직렬화 한다

    depth = 1 # 1 = True , 0 = False 
    # depth = 1 : 피드 모델 객체를 직렬화 하고 싶으면 depth = 1로 설정
