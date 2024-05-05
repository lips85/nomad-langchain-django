# UsernameAuthentication라는 이름의 authentication class를 빌드하세요.
# UsernameAuthentication 는 반드시 BaseAuthentication에서 extend 되어야 합니다.
# X-USERNAME 헤더를 사용하는 유저를 찾으세요.

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class UsernameAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("X-USERNAME")

        if not username:
            return None

        try:
            user = User.objects.get(username=username)
            return (user, None)

        except User.DoesNotExist:
            raise AuthenticationFailed(f"No user {username}")
