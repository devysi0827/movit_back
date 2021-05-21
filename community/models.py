from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    ## 트위터 모델!!!!!!

    # like
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # hashtag 

class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')
    content = models.CharField(max_length=200)