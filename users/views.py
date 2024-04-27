from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from rest_framework.exceptions import NotFound


class UserTweetViewSet(ModelViewSet):
    serializer_class = TweetSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        try:
            user = User.objects.get(pk=pk)
            return Tweet.objects.filter(user=user)
        except User.DoesNotExist:
            raise NotFound

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
