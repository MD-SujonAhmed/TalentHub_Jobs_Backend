from django.urls import path,include
from.views import CompanyViewset,JobViewset,JobTypeViewset,CategoryViewset,ExperienceLevelViewset,SkillViewset,Application_usersViewset
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router=DefaultRouter()
router.register('company',CompanyViewset)
router.register('job',JobViewset)
router.register('jobType',JobTypeViewset)
router.register('category',CategoryViewset)
router.register('Experience',ExperienceLevelViewset)
router.register('skill',SkillViewset)
job_router=routers.NestedDefaultRouter(router,'job',lookup='job')
job_router.register('applications',Application_usersViewset,basename='applications_users')


urlpatterns = [
    path('',include(router.urls)),
    path('',include(job_router.urls)),
    ]
