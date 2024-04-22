from django.db import models
from common.models import CommonModel

# Create your models here.

class Tweet(CommonModel):
    payload = models.CharField(max_length=180)
    users = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tweets',)    

    def __str__(self):
        return self.payload
    
    def Like_Count(self):
        return self.likes.count()
    

class Like(CommonModel):
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE, related_name='likes',)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='likes',)

    def __str__(self):
        return f'{self.user} likes {self.tweet}'