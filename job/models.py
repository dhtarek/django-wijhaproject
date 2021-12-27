from django.db import models

# Create your models here.
JOB_TYPE = (
    ('FULL Time','Full time'),
    ('Part time','Part time'),
)

class Job (models.Model):
    title = models.TextField(max_length=100)
   #location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length = 1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 1)
    
