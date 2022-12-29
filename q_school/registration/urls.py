from django.urls import path

from q_school.registration.views import (
    CoreView, UserView)


urlpatterns = [
    path('member/', CoreView.as_view(), name="add_pax"),
    path('users/', UserView.as_view(), name="user_list")
]
