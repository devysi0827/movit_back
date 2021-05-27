import re
from django.shortcuts import get_object_or_404
from .models import Review, ReviewComment
from .serializers import ReviewSerializer, ReviewCommentSerializer
from rest_framework import serializers
from rest_framework.decorators import api_view # ,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
# from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['GET', 'POST'])
def review_index_or_create(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
       
    elif request.method == "POST":
        print(1)
        print(request)
        print(request.data)
        print(2)
        serializer = ReviewSerializer(data = request.data)
        my_user =User.objects.filter(username=request.data["UserName"])
        # print(1)
        # print(request.data)
        print(my_user[0].email)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=my_user[0], nickname= my_user[0].nickname, username=request.data["UserName"], email=my_user[0].email)
            print(serializer.data)
            return Response(serializer.data, status= status.HTTP_201_CREATED)         

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == "PUT":
        print(111)
        serializer = ReviewSerializer(instance = review , data= request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review = review)
            return Response(serializer.data)

    elif request.method == "DELETE":
        write_user = Review.objects.filter(id=review.pk)
        my_user =User.objects.filter(username=request.data["UserName"])
        # print(request.data["UserName"])
        # print(write_user[0].username)
        # print(my_user[0])
        if str(my_user[0]) == str(write_user[0].username):
            review.delete()
            data = {
                "success" : True,
                "message" : "리뷰삭제"
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            data = {
                "success" : False,
                "message" : "리뷰삭제실패"
            }
            return Response(data)

@api_view(['GET','POST'])
def review_comment_index_or_create(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)

    if request.method == "GET":
        review_comments = ReviewComment.objects.filter(review_id = review_pk)
        serializer = ReviewCommentSerializer(review_comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        my_user =User.objects.filter(username=request.data["UserName"])
        print(11111)
        print(my_user)
        serializer = ReviewCommentSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=my_user[0],nickname= my_user[0].nickname, username=request.data["UserName"], email=my_user[0].email)
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
        write_user = ReviewComment.objects.filter(id=comment.pk)
        my_user =User.objects.filter(username=request.data["UserName"])
        print(write_user[0].username)
        print(my_user[0])
        if str(my_user[0]) == str(write_user[0].username):
            comment.delete()
            data = {
                "success" : True,
                "message" : "코멘트삭제"
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            data = {
                "success" : False,
                "message" : "코멘트삭제실패"
            }
            return Response(data)  

@api_view(['POST'])
def review_data(request):
    my_reviews =Review.objects.filter(username=request.data["UserName"])
    data = [] 
    for i in range(len(my_reviews)):
        review_json = {
            "nickname":my_reviews[i].nickname,
            "username":my_reviews[i].username,
            "email": my_reviews[i].email,
            "id":my_reviews[i].id,
            "title": my_reviews[i].title,
            "content":  my_reviews[i].content,
            "created_at": my_reviews[i].created_at,
            "updated_at": my_reviews[i].updated_at
            }
        data.append(review_json)
    return Response(data)