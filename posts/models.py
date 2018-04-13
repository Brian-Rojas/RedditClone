from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title
