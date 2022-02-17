from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.IntegerField(blank=False)
    value = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.id) + " game: " + str(self.game_id) + " \ rate: " + str(self.value)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.IntegerField(blank=False)
    content = models.CharField(blank=False, max_length=2000)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)