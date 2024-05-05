from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tweet
from users.models import User


# /api/v1/tweets: Test GET and POST methods
class Tweets_All_Test(APITestCase):

    Test_URL = "/api/v1/tweets/"
    Test_payload_1 = "First tweet"
    Test_payload_2 = "Second tweet"

    def setUp(self):
        self.user = User.objects.create_user(username="TestAdmin", password="123456")
        Tweet.objects.create(payload=self.Test_payload_1, user=self.user)
        Tweet.objects.create(payload=self.Test_payload_2, user=self.user)

    def test_get_all_tweets(self):
        response = self.client.get(self.Test_URL)
        data = response.json()
        print("=============================")
        print("ALL Tweets API GET확인 ")
        # HTTP 응답
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"HTTP_{response.status_code}입니다.",
        )
        print("응답 : HTTP_200_OK")

        # 내부 응답 결과 확인
        self.assertEqual(
            len(data),
            2,
            f"데이터가 {len(data)}개인데, 2개가 필요합니다.",
        )
        print("tweets 갯수 일치")

        self.assertEqual(
            data[0]["payload"],
            self.Test_payload_1,
            "payload가 일치하지 않습니다.",
        )
        print("tweets payload 일치")

        self.assertEqual(
            data[0]["user"],
            self.user.id,
            "user가 일치하지 않습니다.",
        )
        print("user 일치")
        print("=============================")

    def test_post_new_tweet(self):
        print("=============================")
        print("ALL Tweets API POST확인 ")
        new_tweet = {"payload": "New tweet", "user": self.user.id}
        response = self.client.post(self.Test_URL, new_tweet, format="json")
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            f"새로운 tweet을 가져오는 테스트의 응답은 HTTP_{response.status_code}입니다.",
        )
        print("응답 : HTTP_201_CREATED")

        self.assertEqual(
            new_tweet["payload"],
            data["payload"],
            "새로운 tweet의 payload가 일치하지 않습니다.",
        )
        print("payload 일치")

        self.assertEqual(
            new_tweet["user"],
            data["user"],
            "새로운 tweet의 user가 일치하지 않습니다.",
        )
        print("user 일치")
        print("=============================")


# /api/v1/tweets/<int:pk>: Test GET, PUT and DELETE methods
class Tweets_Detail_Test(APITestCase):
    Test_URL_Valid = "/api/v1/tweets/1"
    Test_URL_Invalid = "/api/v1/tweets/2"

    Test_payload = "First tweet"
    Change_payload = "Changed tweet"

    def setUp(self):
        self.user = User.objects.create_user(username="TestAdmin", password="123456")
        Tweet.objects.create(payload=self.Test_payload, user=self.user)

    def test_1_get_tweets_detail(self):
        response = self.client.get(self.Test_URL_Valid)
        data = response.json()
        print("=============================")
        print("Tweets Detail API GET확인(Valid URL) ")

        # HTTP 응답
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"tweet의 상세 정보를 가져오는 테스트의 응답은 HTTP{response.status_code}입니다.",
        )
        print("응답 : HTTP_200_OK")

        # 내부 응답 결과 확인
        self.assertEqual(
            data["payload"],
            self.Test_payload,
            "payload가 일치하지 않습니다.",
        )
        print("tweets payload 일치")

        self.assertEqual(
            data["user"],
            self.user.id,
            "user가 일치하지 않습니다.",
        )
        print("user 일치")
        print("=============================")

    def test_2_tweet_not_found(self):
        print("=============================")
        print("Tweets Detail API GET확인(Invalid URL) ")
        response = self.client.get(self.Test_URL_Invalid)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
            f"없는 tweet의 정보를 가져오는 테스트의 응답은 HTTP{response.status_code}입니다.",
        )
        print("응답 : HTTP_404_NOT_FOUND")
        print("=============================")

    def test_3_put_tweet(self):
        print("=============================")
        print("Tweets Detail API PUT확인 ")
        change_tweet = {"payload": self.Change_payload}
        response = self.client.put(self.Test_URL_Valid, change_tweet, format="json")
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            f"새로운 tweet을 가져오는 테스트의 응답은 HTTP_{response.status_code}입니다.",
        )
        print("응답 : HTTP_200_OK")

        self.assertEqual(
            change_tweet["payload"],
            data["payload"],
            "새로운 tweet의 payload가 일치하지 않습니다.",
        )
        print("payload 일치")
        print("=============================")

    def test_4_delete_tweet(self):
        print("=============================")
        print("Tweets Detail API DELETE확인 ")

        response = self.client.delete(self.Test_URL_Valid)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            f"tweet를 삭제하는 테스트의 응답은 HTTP_{response.status_code}입니다.",
        )
        print("응답 : HTTP_204_NO_CONTENT")
        print("=============================")
