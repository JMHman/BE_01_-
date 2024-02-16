"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from feeds import views

urlpatterns = [
    # 개발시에는 api/v1/ 을 붙여준다
    path("admin/", admin.site.urls),
    path("api/v1/feeds/", include("feeds.urls")), 
    path("api/v1/users/", include("users.urls")),
    path("api/v1/reviews/", include("reviews.urls")),


    # path('admin/', admin.site.urls),
    # path('feeds/',include('feeds.urls')),

    # 아래처럼 여기에 적어도 되지만 위처럼 코드를 짜고 feeds 폴더에 생성해서 지금처럼 적어도 된다.
    # path("feeds/", views.show_feed),
    # path("feeds/all", views.all_feed),
    # path("feeds/<int:feed_id>/<str:feed_content>/", views.one_feed),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
