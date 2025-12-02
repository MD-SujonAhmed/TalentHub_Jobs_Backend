from django.urls import path
from.views import CompanyViewset,JobViewset,JobTypeViewset,CategoryViewset,ExperienceLevelViewset,SkillViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('company',CompanyViewset)
router.register('job',JobViewset)
router.register('jobType',JobTypeViewset)
router.register('category',CategoryViewset)
router.register('Experience',ExperienceLevelViewset)
router.register('skill',SkillViewset)
urlpatterns = router.urls
