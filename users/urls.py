from django.urls import path
from . import views

urlpatterns = [
    path("",views.UserViewset.as_view({"get": "list","post": "create",}),),
    path("<int:pk>/tweets/",
        views.UserTweetViewSet.as_view({'get': 'list',},),
    )
]
