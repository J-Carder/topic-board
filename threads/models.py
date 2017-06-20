from django.db import models


class Topic(models.Model):

    name = models.CharField(max_length=20, default='Anonymous')
    text = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Message(models.Model):
    topic = models.ForeignKey(Topic)

    name = models.CharField(max_length=20, default='Anonymous')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


