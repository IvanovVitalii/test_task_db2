from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Messages_db2 API",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="contact@messages.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'messages_db2'
urlpatterns = [
    path('create/', MessageCreateView.as_view()),
    path('list/', MessagesListView.as_view()),
    path('single/<int:pk>/', MessageDetailView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
