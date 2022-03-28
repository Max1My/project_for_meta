from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicCategoryModelViewSet,TopicModelViewSet,QuestionModelViewSet

router = DefaultRouter()
router.register('categories',TopicCategoryModelViewSet)
router.register('topics/',TopicModelViewSet)
router.register('questions/', QuestionModelViewSet)

app_name = 'authapp'
urlpatterns = [
    path('categories/',TopicCategoryModelViewSet.as_view()),
    path('topics/',TopicModelViewSet.as_view()),
    path('question/',QuestionModelViewSet.as_view())
]