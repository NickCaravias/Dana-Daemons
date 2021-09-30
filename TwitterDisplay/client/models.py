from django.db import models

class Tweets(models.Model):
    tweet_text = models.CharField(max_length=300)
    tweet_date = models.DateTimeField('date tweeted')
    tweet_author = models.CharField(max_length=300)

