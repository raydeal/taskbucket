from django.urls import path

from .views import UserTaskListView

urlpatterns = [
     path('', UserTaskListView.as_view()),
]
