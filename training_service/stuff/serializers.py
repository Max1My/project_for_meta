from rest_framework.serializers import ModelSerializer
from .models import TopicCategory,Topic,Question,Ask


class TopicCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = TopicCategory
        fields = '__all__'

class TopicModelSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AskModelSerializer(ModelSerializer):
    class Meta:
        model = Ask
        fields = '__all__'