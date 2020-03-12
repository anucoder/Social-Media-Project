from django.conf.urls import url,include
from posts import views

app_name = "posts"

urlpatterns = [
                url(r'^new/',views.CreatePost.as_view(),name='create'),
]
