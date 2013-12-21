from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Note(models.Model):
	owner 		= models.ForeignKey(User)
	title 		= models.CharField(max_length=100)
	text 		= models.CharField(max_length=500)
	createTime 	= models.DateTimeField()


class NoteForm(ModelForm):
	class Meta:
		model = Note
		# fields=["title","text","createTime"]
		exclude=["owner"]
