from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.Tweets_All.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
]
