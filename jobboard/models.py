from django.db import models
from JobApplication.models import JobApplication 

# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=20)
    location=models.CharField(max_length=100,blank=True,null=True)
    description=models.CharField(max_length=10,blank=True,null=True)
    

class JobType(models.Model):
    job_type=[
        ('Remote','remote'),
        ('onsite','onsite'),
        ('hybrid','hybrid'),
    ]
    job_type=models.CharField(max_length=10,choices=job_type,default='job-type')
class Job(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(blank=True,null=True)
    Workplace_choices = [
        ('office', 'office'),
        ('home', 'home'),
    ]
    Workplace=models.CharField(max_length=10,choices=Workplace_choices,default='office')
    deadline=models.DateField(null=True,blank=True)
    companies=models.ManyToManyField(Company,related_name='companies')
    job_type=models.ForeignKey(JobType,on_delete=models.CASCADE)
    salary=models.CharField(max_length=10,blank=True,null=True)
    Vacancy=models.CharField(max_length=10,blank=True,null=True)
    applications_user=models.ForeignKey(JobApplication,on_delete=models.CASCADE,related_name='application_users',null=True)
    
    
class Category(models.Model):
    name=models.CharField(blank=True,null=True)
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='category')

class ExperienceLevel(models.Model):
    ExperienceLevel_name=[
        ('Fresher','fresher'),
        ('Mid','Mid'),
        ('Senior','senior'),
    ]
    ExperienceLevel=models.CharField(max_length=20,choices=ExperienceLevel_name,default='Fresher')
class Skill(models.Model):
    name=models.CharField(max_length=100)
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='skill')
