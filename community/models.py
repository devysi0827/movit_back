from django.db import models

# Create your models here.
class Review(models.Model):
    ## 트위터 모델!!!!!!
    # username 
    # like
    content = models.TextField()
    # hashtag 

class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')
    content = models.CharField(max_length=200)