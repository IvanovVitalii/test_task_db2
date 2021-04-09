from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'messages_db2'
urlpatterns = [
    path('message/create/', MessageCreateView.as_view()),
    path('list/', MessagesListView.as_view()),
    path('message/deteil/<int:pk>/', MessageDetailView.as_view()),
]
