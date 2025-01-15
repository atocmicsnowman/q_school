"""
main URL dispatcher
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from q_school.views import redirect_to_user_page

urlpatterns = [
    path('', redirect_to_user_page),
    path('admin/', admin.site.urls),
    path('registration/', include('q_school.registration.urls')),
    path('geography/', include('q_school.geography.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
