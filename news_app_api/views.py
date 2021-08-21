from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from news_app.models import Story, Comment, Job
from .serializers import StorySerializer, JobSerializer, CommentSerializer
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

class ItemsList(APIView):
    
    def get(self, request, item, format=None):
        if item == 'story':
            stories = Story.objects.all()
            serializer = StorySerializer(stories, many=True)
        elif item == 'job':
            jobs = Job.objects.all()
            serializer = JobSerializer(jobs, many=True)
        elif item == 'comment':
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, item, format=None):
        if item == 'story':
            serializer = StorySerializer(data=request.data)
        elif item == 'job':
            serializer = JobSerializer(data=request.data)
        elif item == 'comment':
            serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StoryDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)
    
    def put(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        story = self.get_object(pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class JobDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = JobSerializer(story)
        return Response(serializer.data)
    
    def put(self, request, pk):
        story = self.get_object(pk)
        serializer = JobSerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        story = self.get_object(pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = CommentSerializer(story)
        return Response(serializer.data)
    
    def put(self, request, pk):
        story = self.get_object(pk)
        serializer = CommentSerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        story = self.get_object(pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        

            
 