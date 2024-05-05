from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserList.as_view()),
    path("password", views.ChangePassword.as_view()),
    path("login", views.LogIn.as_view()),
    path("logout", views.LogOut.as_view()),
    path("<int:pk>", views.UserDetail.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
]

# GET,POST /api/v1/users: See all users
# PUT /api/v1/users/password: Change password of logged in user.
# POST /api/v1/users/login: Log user in
# POST /api/v1/users/logout: Log user out
# GET /api/v1/users/<int:pk>: See user profile
# GET /api/v1/users/<int:pk>/tweets: See tweets by a user
