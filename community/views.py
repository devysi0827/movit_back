from django.shortcuts import get_object_or_404
from .models import Review, ReviewComment
from .serializers import ReviewSerializer, ReviewCommentSerializer
from rest_framework import serializers
from rest_framework.decorators import api_view # ,permission_classes
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def review_index_or_create(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
       
    elif request.method == "POST":
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)        

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ReviewSerializer(instance = review , data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review = review)
            return Response(serializer.data)

    elif request.method == "DELETE":
        review.delete()
        data = {
            "success" : True,
            "message" : "리뷰삭제"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

########################################
@api_view(['GET','POST'])
def review_comment_index_or_create(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method == "GET":
        review_comments = ReviewComment.objects.all()
        serializer = ReviewCommentSerializer(review_comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ReviewCommentSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
            return Response(serializer.data, status= status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_comment_detail_or_update_or_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk = review_pk)
    comment = get_object_or_404(ReviewComment, pk = comment_pk)

    if request.method == "GET":
        serializer = ReviewCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ReviewCommentSerializer(instance = comment, data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(comment = comment)
            return Response(serializer.data)

    elif request.method == "DELETE":
        comment.delete()
        data = {
            "success" : True,
            "message" : "comment 삭제완료"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)    