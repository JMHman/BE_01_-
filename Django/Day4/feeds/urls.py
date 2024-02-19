from django.urls import path
from . import views

urlpatterns = [
  path('', views.Feeds.as_view()),
  path("list", views.FeedList.as_view()),
  path('<int:feed_id>', views.FeedDetail.as_view())
]