from django.db import models

#Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=50)

class Job(models.Model):
    name = models.CharField( max_length=255)
    place = models.CharField( max_length=255)
    type = models.CharField( max_length=255)
    Category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    salary = models.CharField(max_length=255)

class Application(models.Model):
    job_id = models.ForeignKey("candidate.Job", on_delete=models.CASCADE)
    candidate_name = models.CharField( max_length=255)
    candidate_email = models.EmailField( max_length=255)
    resume_url = models.URLField( max_length=2000)