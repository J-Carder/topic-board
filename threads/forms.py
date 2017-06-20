from django import forms

from .models import Topic, Message


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'text', 'description']
        labels = {'text': 'Topic', 'name': 'Name', 'description': 'Description'}


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'text']
        labels = {'text': 'Message', 'name': 'Name'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}