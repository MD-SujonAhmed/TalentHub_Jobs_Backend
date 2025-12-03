from django.urls import path
from.views import JobApplicationViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('job-apply',JobApplicationViewset)
urlpatterns = router.urls
