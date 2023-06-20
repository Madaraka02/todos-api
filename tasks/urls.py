from django.urls import path
from tasks.views import TaskListAPIView,TaskDetailAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
]