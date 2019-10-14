from django.db import models
from django import forms

# Create your models here.
class users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=264, unique=True)
    entity = models.CharField(max_length=264, unique=True)
    role = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name
        return self.entity
        return self.role

class posts(models.Model):
    comments = models.ManyToManyField('comments')

    def __str__(self):
        return str(self.comments)

class comments(models.Model):
    text = models.CharField(max_length=26, unique=True)

    def __str__(self):
        return self.text

class coursres(models.Model):
    name = models.CharField(max_length=264, unique=True)

class video(models.Model):
    url = models.CharField(max_length=264)

class document(models.Model):
    name = models.CharField(max_length=264, null=True)
    attatchment = models.FileField()

class quiz(models.Model):
    coursre = models.ForeignKey('coursres',on_delete=models.CASCADE,)

class questions(models.Model):
    quiz = models.ForeignKey('quiz',on_delete=models.CASCADE,)
    text = models.CharField(max_length=26, unique=True)

class answers(models.Model):
    question = models.ForeignKey('questions',on_delete=models.CASCADE,)
    text = models.CharField(max_length=26, unique=True)
    is_correct=models.BooleanField(default=False)
