from rest_framework import viewsets
from rest_framework.views import Response
from .models import TopicCategory,Topic,Question,Ask,Result
from .serializers import (
    TopicCategoryModelSerializer,
    TopicModelSerializer,
    QuestionModelSerializer,
    AskModelSerializer,
    ResultModelSerializer
)

from django.shortcuts import get_object_or_404
from authapp.models import User


class TopicCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = TopicCategory.objects.all()
    serializer_class = TopicCategoryModelSerializer

class TopicModelViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicModelSerializer

    def get(self, request, pk=None):
        topic = Topic.objects.filter(id=pk)
        serializer = TopicModelSerializer(topic, many=True)
        return Response(serializer.data)

class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer

    def get(self,request, pk=None):
        question = Question.objects.filter(id=pk)
        serializer = QuestionModelSerializer(question,many=True)
        return Response(serializer.data)

class AskModelViewSet(viewsets.ModelViewSet):
    queryset = Ask.objects.all()
    serializer_class = AskModelSerializer

    def get(self,request,pk=None):
        ask = Ask.objects.filter(id=pk)
        serializer = AskModelSerializer(ask,many=True)
        return Response(serializer.data)

class ResultModelViewSet(viewsets.ReadOnlyModelViewSet):
    def list(self,request):
        queryset = Result.objects.all()
        serializer = ResultModelSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Result.objects.filter(user=request.user)
        result = get_object_or_404(queryset,pk=pk)
        serializer = ResultModelSerializer(result)
        return Response(serializer.data)