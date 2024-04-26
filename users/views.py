from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer
from tweets.models import Tweet
from tweets.serializers import UserTweetSerializer


class UserTweetsViewset(ModelViewSet):
    serializer_class = UserTweetSerializer
    queryset = Tweet.objects.all()
    pk_field = "user_id"
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Tweet.objects.all()
    #     user = self.request.query_params.get("user", None)
    #     if user is not None:
    #         queryset = queryset.filter(user=user)
    #     return queryset


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# class UserTweets(APIView):
#     def get_object(self, pk):
#         try:
#             user = User.objects.get(pk=pk)
#             tweets = Tweet.objects.filter(user=user)
#             return tweets
#         except User.DoesNotExist:
#             raise NotFound

#     def get(self, request, pk):
#         serializer = TweetSerializer(self.get_object(pk), many=True)
#         return Response(serializer.data)
