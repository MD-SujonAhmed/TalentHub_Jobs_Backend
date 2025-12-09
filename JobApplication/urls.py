from django.urls import path
from.views import JobApplicationViewset
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers

router=DefaultRouter()
router.register('job-apply',JobApplicationViewset)

# Nested Operations ............      ..........      ..........      ........        
# job_router=routers.NestedDefaultRouter('job',lookup='job')
# job_router.register('applications',Application_usersViewset,basename='applications_users')
urlpatterns =router.urls 
