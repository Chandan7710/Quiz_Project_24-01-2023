from rest_framework import viewsets
from rest_framework.response import Response
from quiz_app.models import Quiz_Category, QuestionModel, General_Knowledge, Leaderboard
from auth_app.models import User
from quiz_app.api.serializers import (QuizCategorySerializer, QuestionModelSerializer, 
                                    GeneralKnowledgeSerializer,
                                    QuestionAnswerSerializer, TakeQuizSerializer, LeaderboardSerializer)
from django.shortcuts import get_object_or_404
from rest_framework import status
from quiz_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from quiz_app.api.pagination import QuestionModelformVSPagination, QuizQuestionformVSPagination
from rest_framework import status, viewsets
import random
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly)

#Class For Quiz Category
class QuizCategoryformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        queryset = Quiz_Category.objects.all()
        serializer = QuizCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Quiz_Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuizCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        permission_classes = [IsAdminOrReadOnly]
        serializer = QuizCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def update(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        serializer = QuizCategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
#Class For Quiz Question
class QuestionModelformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def retrieve(self, request, pk=None):
        from rest_framework.pagination import PageNumberPagination
        queryset = QuestionModel.objects.filter(category=pk)
        paginator = QuestionModelformVSPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = QuestionModelSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = QuestionModelSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = QuestionModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = QuestionModel.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        serializer = QuestionModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Class For Quiz Leaderboard
class LeaderboardformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        queryset = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Leaderboard.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data=request.data
        serializer = QuestionModelSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = Leaderboard.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Leaderboard.objects.get(pk=pk)
        serializer = QuestionModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    
#Class For GeneralKnowledge
class GeneralKnowledgeformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        queryset = General_Knowledge.objects.all()
        today_topic = random.choice(queryset)
        serializer = GeneralKnowledgeSerializer(today_topic)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = General_Knowledge.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = GeneralKnowledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = General_Knowledge.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = General_Knowledge.objects.get(pk=pk)
        serializer = GeneralKnowledgeSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Class For Quiz Question and Answer
class QuestionAnswerformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        
        queryset = QuestionModel.objects.all()
        serializer = QuestionAnswerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        
        serializer = QuestionAnswerSerializer(data=request.data)
        if serializer.is_valid():        
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Class For Taking Quiz
class QuizQuestionformVS(viewsets.ViewSet):
    
    permission_classes = [IsReviewUserOrReadOnly]
    
    def create(self, request, pk = None):
        
        serializer = TakeQuizSerializer(data = request.data)
        
        leaderboard = Leaderboard.objects.all()
        users = User.objects.all()
        quiz_type = Quiz_Category.objects.filter(category=pk)

        if Leaderboard.objects.filter(request.user.username and request.Quiz_Category.quiz_category).exists():
            leader = Leaderboard.objects.update_or_create(user_name='user.username', quiz_type = quiz_type)
        
        # if leader.user_name and leader.quiz_name
        # if Leaderboard.objects.filter(user_name = cleaned_info['username']).exists():
        #     if User.objects.filter(email = cleaned_info['username']).exists():
        # num_results = User.objects.filter(email = cleaned_info['username']).count()
        
        if serializer.is_valid():
            
            id = serializer.validated_data['id']
            answer = serializer.validated_data['answer']
            question = QuestionModel.objects.get(pk=id)
            if question.answer == answer:
                return Response("Your Answer is correct", status=status.HTTP_201_CREATED)
            else:
                return Response("Your Answer is incorrect", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
