from django.db import models

from django.contrib.auth.models import User

class Note(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=500)
	createTime = models.DateTimeField()


