from django.urls import path
from . import views as api_views

urlpatterns = [
    path("getLTP", api_views.getLTP, name= "getLTP")
    # path("user", cr_views.NormalUser_list, name="user"),
    # path("user/create", cr_views.Signup, name="signup"),
    # path("user/login", cr_views.LoginView, name='login'),
    # path("user/logout", cr_views.LogoutView, name='logout'),
    # path("user/isProfileDone", cr_views.isProfileDone, name='isProfileDone'),
    # path("user/updateProfile", cr_views.updateProfile, name='updateProfile'),
    # path("user/getProfile", cr_views.getProfile, name='getProfile'),
    # path("user/team", cr_views.createTeam, name='createTeam'),
    # path("user/getIdbyCrid", cr_views.getIdbyCrid, name='getIdbyCrid'),
    # path("user/getCrIdbyId", cr_views.getCrIdbyId, name='getCrIdbyId'),
    # path("user/getTeam", cr_views.getTeam, name="getTeam")

    # path("Normal", ydp_views.NormalUser_list, name="Normal"),
    # path("Event", ydp_views.Event_list, name="Event"),
    # path("Event_reg", ydp_views.Event_reg, name="Event_reg"),
    # path("Convo", ydp_views.ConvoUser_list, name="Convo"),

]

