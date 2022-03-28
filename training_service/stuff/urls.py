from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicCategoryModelViewSet,TopicModelViewSet,QuestionModelViewSet

from .views import (
    TopicCategoryModelViewSet,
    TopicModelViewSet,
    QuestionModelViewSet,
    AskModelViewSet,
    ResultModelViewSet,
)

router = DefaultRouter()

router.register('categories',TopicCategoryModelViewSet)
router.register('topics', TopicModelViewSet)
router.register('questions', QuestionModelViewSet)
router.register('ask',AskModelViewSet)
router.register('result/<int:pk>/', ResultModelViewSet.as_view({'get': 'retrieve'}))

urlpatterns = [
    path('api/', include(router.urls)),
    ]