from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('blog/', views.PostCategory.as_view(), name="post_category"),
    path('category.html', views.category, name='category'),
    path('about.html', views.about, name='about'),
]
