from graphene_django.forms.mutation import DjangoModelFormMutation
from django import  forms
from .models import *

class CreateCommentsForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('text',)

class CreatePostsForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ('comments',)

class CreateCoursresForm(forms.ModelForm):
    class Meta:
        model = coursres
        fields = ('name',)

class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = video
        fields = ('url',)

class CreateDocumentForm(forms.ModelForm):
        class Meta:
            model = document
            fields = ('name','attatchment',)

class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = quiz
        fields = ('coursre',)

class CreateQuestionsForm(forms.ModelForm):
    class Meta:
        model = questions
        fields = ('quiz','text',)

class CreateAnswersForm(forms.ModelForm):
    class Meta:
        model = answers
        fields = ('question','text',)
