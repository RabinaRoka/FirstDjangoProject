from django.db import models
class intro(models.Model):  #inherit .model
    intro_title=models.CharField(max_length=50)  #official field for model field reference django
    intro_desc=models.TextField()

# Create your models here.
