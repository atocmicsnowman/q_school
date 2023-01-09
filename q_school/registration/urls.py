from django.urls import path

from q_school.registration.views import (
    UsersView, PaxView, UserView, UsersUploadView, UserUploadView)


urlpatterns = [
    path('member/', UsersView.as_view(), name="members_management"),
    path('member/<int:user_id>', PaxView.as_view(), name="member_management"),
    path('membership_files/commit', UsersUploadView.as_view(), name="users_management_upload_commit"),
    path('membership_files/<int:region_id>', UserUploadView.as_view(), name="users_management_uploader"),
    path('users/', UserView.as_view(), name="user_list")
]
