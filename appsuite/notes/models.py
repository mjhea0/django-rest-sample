from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from django import forms

class Note(models.Model):
  owner = models.ForeignKey(User)
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=500)
  createTime = models.DateTimeField()


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # fields=["title","text","createTime"]
        exclude=["owner"]
        widgets = {
          'text': forms.Textarea(attrs={'cols':60,'rows':10, 'class':'form-control'}),
        }

class NoteResources(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = "note"
        authorization = Authorization()
