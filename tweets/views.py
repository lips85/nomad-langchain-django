from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TweetSerializer
from .models import Tweet
from rest_framework.exceptions import NotFound


class Tweets(APIView):
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            tweet = serializer.save()
            return Response(
                TweetSerializer(tweet).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class TweetDetail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user_tweets = self.get_object(pk)
        serializer = TweetSerializer(user_tweets)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        user_tweets = self.get_object(pk)
        serializer = TweetSerializer(
            user_tweets,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(
                TweetSerializer(updated_tweet).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        user_tweets = self.get_object(pk)
        user_tweets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GET/POST /api/v1/tweets: See all tweets

# GET,PUT,DELETE /api/v1/tweets/<int:pk>: See a tweet
