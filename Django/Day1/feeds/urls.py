from django.urls import path
from . import views

urlpatterns = [
  path("", views.show_feed), 
  path("all", views.all_feed),
  path("<int:feed_id>/<str:feed_content>/", views.one_feed)
  ] 
# config.urls.py 파일에 기본 url을 'feed/' 로 지정했기 떄문에 
# '/' 없이 나머지 링크만 적어주면 된다.