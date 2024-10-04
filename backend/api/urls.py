from django.urls import path
from .views import ChatGPTAPIView

urlpatterns = [
    path('chatgpt/', ChatGPTAPIView.as_view(), name='chatgpt-api'),
]