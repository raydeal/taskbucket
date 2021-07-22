# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import UserTask

class UserTaskListView(ListView):
    model = UserTask


class UserTaskCreateView(CreateView):
    model = UserTask
    success_url = reverse_lazy('task-list')
    fields = ['user', 'location', 'title', 'description']


class UserTaskUpdateView(UpdateView):
    model = UserTask
    success_url = reverse_lazy('task-list')
    fields = ['user', 'location', 'status', 'title', 'description']


class UserTaskDeleteView(DeleteView):
    model = UserTask
    success_url = reverse_lazy('task-list')