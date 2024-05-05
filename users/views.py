from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError
from .models import User
from .serializers import UserSerializer
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout


# GET,POST /api/v1/users: See all users
class UserList(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# GET /api/v1/users/<int:pk>: See user profile
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        one_user = self.get_object(pk)
        serializer = UserSerializer(one_user)
        return Response(serializer.data)


# GET /api/v1/users/<int:pk>/tweets: See tweets by a user
class UserTweets(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user = self.get_object(pk)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


# PUT /api/v1/users/password: Change password of logged in user.
class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(
                {"성공": "비밀번호가 변경되었습니다."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"실패": "비밀번호가 일치하지 않습니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


# POST /api/v1/users/login: Log user in
class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response(
                {"성공": "로그인 되었습니다."},
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {"비밀번호 오류": "비밀번호가 일치하지 않습니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


# POST /api/v1/users/logout: Log user out
class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"로그아웃": "이용해주셔서 감사합니다."}, status.HTTP_200_OK)
