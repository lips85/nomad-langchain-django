from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tweets.as_view()),
    path("<int:pk>", views.TweetDetail.as_view()),
]

# GET/POST /api/v1/tweets: See all tweets

# GET,PUT,DELETE /api/v1/tweets/<int:pk>: See a tweet
