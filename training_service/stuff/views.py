from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response
from .models import TopicCategory,Topic
from .serializers import TopicCategoryModelSerializer,TopicModelSerializer


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

