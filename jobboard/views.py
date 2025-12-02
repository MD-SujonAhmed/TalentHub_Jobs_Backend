from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import JobSerializer,CompanySerializer,jobTypeSerializer,CategorySerializer,SkillSerializer,ExperienceLevelSerializer
from.models import Company,JobType,Job,Category,ExperienceLevel,Skill
# Create your views here.
class CompanyViewset(ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class JobViewset(ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    
class JobTypeViewset(ModelViewSet):
    queryset=JobType.objects.all()
    serializer_class=jobTypeSerializer

class CategoryViewset(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class ExperienceLevelViewset(ModelViewSet):
    queryset=ExperienceLevel.objects.all()
    serializer_class=ExperienceLevelSerializer
class SkillViewset(ModelViewSet):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer