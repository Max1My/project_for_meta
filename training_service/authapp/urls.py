from django.urls import path

from .views import RegistrationAPIView,LoginAPIView,UserRetrieveUpdateAPIView

app_name = 'authapp'
urlpatterns = [
    path('client/',UserRetrieveUpdateAPIView.as_view()),
    path('clients/create/', RegistrationAPIView.as_view()),
    path('clients/login/', LoginAPIView.as_view()),
]