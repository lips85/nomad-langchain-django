from django.urls import path
from . import views

urlpatterns = [
    path(
        "<int:pk>/tweets",
        views.UserTweetsViewset.as_view(
            {
                "get": "retrieve",
                "post": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "",
        views.UserViewset.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
]
