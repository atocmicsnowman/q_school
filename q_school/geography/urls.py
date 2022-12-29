from django.urls import path

from q_school.geography.views import (
    RegionsView, RegionView)

urlpatterns = [
    path('region/', RegionsView.as_view(), name="add_region"),
    path('region/<int:region_index>', RegionView.as_view(), name="region_details"),
]