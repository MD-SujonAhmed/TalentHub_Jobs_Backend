from rest_framework import serializers
from.models import Company,JobType,Job,Category,ExperienceLevel,Skill
from JobApplication.models import JobApplication

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Company
        fields="__all__"

class jobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobType
        fields="__all__"
        
class JobSerializer(serializers.ModelSerializer):
    application_count=serializers.SerializerMethodField() # this is model new feild add korsa 
    class Meta:
         model=Job
         fields="__all__"
    def get_application_count(self,obj):
        return obj.applications.count()

         
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
    

class applicationUsers(serializers.ModelSerializer): # applicaiton users jono dese 
    
    class Meta:
        model=JobApplication
        fields="__all__"