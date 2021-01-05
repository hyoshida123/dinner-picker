from django.urls import path
from api.endpoints import snippet_views
from api.endpoints import suggest_restaurants_endpoint
from api.endpoints.authentication import user_authentication_endpoint
from api.endpoints.settings import preference_settings_endpoint
from api.endpoints.group import group_endpoint
from api.endpoints.suggestion import suggestion_endpoint

"""

Notice that if you want to add a query param, you should use re_path

"""
urlpatterns = [
    # example snippets
    path('snippets', snippet_views.SnippetList.as_view()),
    path('snippets/<str:pk>', snippet_views.SnippetDetail.as_view()),

    # user activity
    # group CRUD
    path('group/creategroup', group_endpoint.CreateGroup.as_view()),
    path('group/joingroup', group_endpoint.JoinGroup.as_view()),
    path('group/leavegroup', group_endpoint.LeaveGroup.as_view()),
    path('group/viewGroupOfUser', group_endpoint.ViewGroupOfUser.as_view()),
    path('group/listAllGroups', group_endpoint.ListAllGroups.as_view()),
    path('group/get_groups_by_username', group_endpoint.GetGroupsByUsername.as_view()),
    path('group/list_users_in_group', group_endpoint.ListUsersInGroup.as_view()),

    # user authentication
    path('authentication/signup', user_authentication_endpoint.Signup.as_view()),
    path('authentication/listUsers', user_authentication_endpoint.GetUserList.as_view()),
    path('authentication/verifyUserLoggedIn', user_authentication_endpoint.VerifyUserLoggedIn.as_view()),
    path('authentication/getUserDetails', user_authentication_endpoint.ShowUserDetails.as_view()),

    # user settings
    path('settings/preference', preference_settings_endpoint.PreferenceSettings.as_view()),

    # restaurant suggestion
    path('suggestion/suggest', suggestion_endpoint.Suggest.as_view()),

    # restaurant suggestion prototype
    path('suggest_restaurant_views', suggest_restaurants_endpoint.SuggestRestaurants.as_view())
]