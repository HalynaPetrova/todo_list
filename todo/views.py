from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from todo.models import Tag, Task


class TaskListView(generic.ListView):
    template_name = "todo/task_list.html"
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskStatusView(View):
    def post(self, request, pk: int = id(__obj=Task)) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.done_mark = not task.done_mark
        task.save()
        return redirect(reverse("todo:task-list"))


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
