from rest_framework import serializers
from .models import Review, ReviewComment


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('user',)

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        exclude = ('review','user',)