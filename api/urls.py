from django.urls import path
from .views import *

urlpatterns = [
    path('fr_request/', Fr_Request.as_view()),
    path('fr_response/', Fr_Response.as_view()),
    path('fr_remove/', Fr_Remove.as_view()),
    path('grp_request/', Grp_Request.as_view()),
    path('grp_response/', Grp_Response.as_view()),
    path('grp_create/', Grp_Create.as_view()),
    path('grp_exit/', Grp_Exit.as_view()),
    path('retrieve_message/', RetrieveMessage.as_view()),
    path('grp_admin_create/', Make_Admin.as_view()),
    path('grp_admin_remove/', Remove_Admin.as_view()),
    path('grp_member_remove/', Remove_Member.as_view()),
    path('friends/', GetFriends.as_view()),
    path('groups/', GetGroups.as_view()),
    path('requests/', GetRequests.as_view()),
    path('profile/<username>/', ProfileView, name="profile"),
    path('profileUpdate/', ProfileUpdate.as_view(), name="ProfileUpdate"),
    path('groupMemberList/', GroupMemberList.as_view(), name="GroupMemberList")
]
