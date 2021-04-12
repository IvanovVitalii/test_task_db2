from django.urls import path
from .views import *

app_name = 'messages_db2'
urlpatterns = [
    path('create/', MessageCreateView.as_view()),
    path('list/', MessagesListView.as_view()),
    path('single/<int:pk>/', MessageDetailView.as_view()),
]
