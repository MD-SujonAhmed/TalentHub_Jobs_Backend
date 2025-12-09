from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import JobSerializer,CompanySerializer,jobTypeSerializer,CategorySerializer,SkillSerializer,ExperienceLevelSerializer,applicationUsers
from.models import Company,JobType,Job,Category,ExperienceLevel,Skill
from users.permissions import IsRecruiter
from JobApplication.models import JobApplication

# Create your views here.
class CompanyViewset(ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
   #  permission_classes=[IsRecruiter]

class JobViewset(ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
   #  permission_classes=[IsRecruiter]
    # def get_queryset(self):
    #    return  Job.objects.filter(job_id=self.kwargs[''])
   
    
    
class JobTypeViewset(ModelViewSet):
    queryset=JobType.objects.all()
    serializer_class=jobTypeSerializer
   #  permission_classes=[IsRecruiter
    

class CategoryViewset(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
   #  permission_classes=[IsRecruiter]
    
class ExperienceLevelViewset(ModelViewSet):
    queryset=ExperienceLevel.objects.all()
    serializer_class=ExperienceLevelSerializer
   #  permission_classes=[IsRecruiter]
    
class SkillViewset(ModelViewSet):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer
   #  permission_classes=[IsRecruiter]
    

class Application_usersViewset(ModelViewSet): # ae holo amier applications  user jono ........ ..
    # queryset=JobApplication.objects.all()
    serializer_class=applicationUsers
    
    def get_queryset(self):
        job_id=self.kwargs.get('job_pk')
        return JobApplication.objects.filter(job_id=job_id)
    