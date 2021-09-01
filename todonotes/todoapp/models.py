from django.db import models
from usersapp.models import MyUsersModel


class ProjectModel(models.Model):
    name = models.CharField(max_length=64, unique=True)
    users = models.ManyToManyField(MyUsersModel)
    repo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class NoteModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUsersModel, on_delete=models.PROTECT)
    remark = models.TextField
    created_day = models.DateField(auto_now_add=True)
    updated_day = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

