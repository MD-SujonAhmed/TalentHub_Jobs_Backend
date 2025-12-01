from rest_framework import serializers
from.models import Company,JobType,Job,Category,ExperienceLevel,Skill

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Company
        fields="__all__"

class jobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobType
        fields="__all__"
        
class JobSerializer(serializers.ModelSerializer):
     class Meta:
         model=Job
         fields="__all__"
         
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields="__all__"
class ExperienceLevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ExperienceLevel
        fields="__all__"
class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Skill
        fields="__all__"
        