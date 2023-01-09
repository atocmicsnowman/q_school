from django.urls import path

from q_school.geography.views import (
    RegionsView, RegionView, RegionViewSet, AreaOfOperationView)


urlpatterns = [
    path('region/', RegionsView.as_view(), name="region_management"),
    path('region/<int:region_index>', RegionView.as_view(), name="region_details"),
    path('area-of-operation/', AreaOfOperationView.as_view(), name="area_of_operation_list"),
    path('area-of-operation/<int:ao_index>', AreaOfOperationView.as_view(), name="area_of_operation_details"),
    path('api/region', RegionViewSet.as_view(), name="api_region_view_set")
]