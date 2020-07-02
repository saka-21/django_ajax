from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import (
  LikeButton,
)
app_name = 'app'

urlpatterns = [
#今回いいねボタンを設置するページ
url(r'^(?P[\w-]+)/$', views.LikePage, name="like_page"),
#いいね情報を格納するページ
url(r'^(?P[\w-]+)/like/$', LikeButton.as_view(), name='like_api'),
]