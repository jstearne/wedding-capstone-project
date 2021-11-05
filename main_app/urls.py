from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('guestbook/', views.Guestbook.as_view(), name="guestbook"),
# Post CRUD functionality (Guestbook serves as READ)
    path('posts/new/', views.CreatePost.as_view(), name="create_post"),
    path('posts/<int:pk>/update', views.UpdatePost.as_view(), name="post_update"),
    path('posts/<int:pk>/delete', views.DeletePost.as_view(), name="post_delete"),
# remaining pages
    path('accommodations/', views.Accommodations.as_view(), name="accommodations"),
    path('schedule/', views.Schedule.as_view(), name="schedule"),
    path('photos/', views.Photos.as_view(), name="photos"),
    path('login/', views.Login.as_view(), name="login"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]