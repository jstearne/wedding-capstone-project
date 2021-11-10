from django.urls import path
from . import views

urlpatterns = [
    # notes on name=""
    path('', views.Home.as_view(), name="home"),
    path('guestbook/', views.Guestbook.as_view(), name="guestbook"),
# Post CRUD functionality (Guestbook serves as READ)
    path('guestbook/new/', views.CreatePost.as_view(), name="guestbook_create"),
    path('guestbook/<int:pk>/update/', views.UpdatePost.as_view(), name="guestbook_update"),
    path('guestbook/<int:pk>/delete', views.DeletePost.as_view(), name="guestbook_delete"),
# remaining pages
    path('accommodations/', views.Accommodations.as_view(), name="accommodations"),
    path('schedule/', views.Schedule.as_view(), name="schedule"),
    path('photos/', views.Photos.as_view(), name="photos"),

    # new add, rsvp via a new template page. Must be called with object pk referencing the user
    path('guestbook/rsvp/<int:pk>', views.GuestRsvp.as_view(), name="rsvp"),

    path('login/', views.Login.as_view(), name="login"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]