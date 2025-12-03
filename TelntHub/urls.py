
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('users.urls')),
    path('api/recruiter/',include('jobboard.urls')),
    path('api/',include('JobApplication.urls')),
    
]
