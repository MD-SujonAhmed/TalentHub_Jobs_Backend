from django.db import models
from jobboard.models import Job
# Create your models here.
class JobApplication(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='application')
    full_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=20,blank=True , null=True)
    resume_file=models.FileField(upload_to='resumes/')
    applied_at=models.DateField(null=True,blank=True,auto_now_add=True)
    # status=models.CharField(max_length=20,default="pending")
    
    def __str__(self):
        return f"{self.full_name} applied for {self.phone}"