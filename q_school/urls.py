"""
main URL dispatcher
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('q_school.registration.urls')),
    path('geography/', include('q_school.geography.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
