from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from .models import TopicCategory,Topic,Question,Ask
from .serializers import (
    TopicCategoryModelSerializer,
    TopicModelSerializer,
    QuestionModelSerializer,
    AskModelSerializer,
)


class TopicCategoryModelViewSet(ModelViewSet):
    queryset = TopicCategory.objects.all()
    serializer_class = TopicCategoryModelSerializer

class TopicModelViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicModelSerializer

    def get(self, request, pk=None):
        topic = Topic.objects.filter(id=pk)
        serializer = TopicModelSerializer(topic, many=True)
        return Response(serializer.data)

class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer

    def get(self,request, pk=None):
        question = Question.objects.filter(id=pk)
        serializer = QuestionModelSerializer(question,many=True)
        return Response(serializer.data)

class AskModelViewSet(ModelViewSet):
    queryset = Ask.objects.all()
    serializer_class = AskModelSerializer

    def get(self,request,pk=None):
        ask = Ask.objects.filter(id=pk)
        serializer = AskModelSerializer(ask,many=True)
        return Response(serializer.data)