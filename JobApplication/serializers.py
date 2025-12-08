from rest_framework import serializers
from .models import JobApplication
from jobboard .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields=['id','title']
class JobApplicationSerializer(serializers.ModelSerializer):
    
    job=JobSerializer(read_only=True)
    job_id=serializers.PrimaryKeyRelatedField( # agula Serilizerzers  add filed kora 
        queryset=Job.objects.all(),
        source='job',
        write_only=True
    )
    class Meta:
        model=JobApplication
        fields="__all__"
        read_only_fields = ['applied_at']
        
        