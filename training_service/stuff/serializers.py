from rest_framework.serializers import ModelSerializer
from .models import TopicCategory,Topic


class TopicCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = TopicCategory
        fields = '__all__'

class TopicModelSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'