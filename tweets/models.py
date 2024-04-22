from django.db import models
from common.models import CommonModel

# Create your models here.

class Tweet(CommonModel):
    payload = models.CharField(max_length=180)
    users = models.ForeignKey('users.User', on_delete=models.CASCADE)    

    def __str__(self):
        return self.payload
    

class Like(CommonModel):
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} likes {self.tweet}'