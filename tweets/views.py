from rest_framework.viewsets import ModelViewSet
from .serializers import TweetSerializer
from .models import Tweet


class Tweets_All(ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


# class Tweets_All(APIView):
#     def get_object(self):
#         tweets = Tweet.objects.all()
#         return tweets

#     def get(self, request):
#         serializer = TweetSerializer(self.get_object(), many=True)
#         return Response(serializer.data)


# Mission:
# ModelSerializer 사용을 위해. 모든 serializers 를 Refactor 하세요.
# APIView 사용을 위해. 모든 views 를 Refactor 하세요.
