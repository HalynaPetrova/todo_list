from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done_mark = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["-datetime", "done_mark"]

    def __str__(self):
        return self.content
