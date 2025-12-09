from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from.serializers import JobApplicationSerializer
from .models import JobApplication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from users.permissions import IsCandidate
# Create your views here.
class JobApplicationViewset(ModelViewSet):
    queryset=JobApplication.objects.all()
    serializer_class=JobApplicationSerializer
    
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filter_fields=['company','job_type','location']
    search_fields=['title','ExperienceLevel']
    OrderingFilter=['salary','deadline']
    # permission_classes=[IsCandidate]