
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('users.urls')),
    path('api/recruiter/',include('jobboard.urls')),
    path('api/',include('JobApplication.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)