from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    # path('blog/', views.PostAbout.as_view(), name='post_about'),
    path('about/', views.PostAbout.as_view(), name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
