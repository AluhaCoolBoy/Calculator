from django.db import models

class Project(models.MODEL):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	pictures = models.ImageField(upload_to = "images/")
# Create your models here.
