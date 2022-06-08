from django.db import models
from django.forms import EmailField

class Students(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  textarea = models.TextField(max_length=600)
