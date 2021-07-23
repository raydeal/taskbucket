from django.urls import path

from .views import UserTaskCreateView, UserTaskDeleteView, UserTaskListView, UserTaskUpdateView

urlpatterns = [
    path("", UserTaskListView.as_view(), name="task-list"),
    path("task/add/", UserTaskCreateView.as_view(), name="task-add"),
    path("task/<int:pk>/", UserTaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", UserTaskDeleteView.as_view(), name="task-delete"),
]
