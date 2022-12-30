from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from restapiapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/<int:pk>',views.student_detail),
    path('studentinfo/',views.students_detail),
    path('studentcreate/',views.student_create),
    path('studentupdate/',views.student_update),
    path('student_api/',views.student_api),
    # path('student_api/',views.StudentApi.as_view()),
    # Project
    path('projectinfo/',views.projects_info),
    path('projectcreate/',views.project_create),
    path('projectinfo/<int:pk>',views.project_detail),
    # team
    path('teaminfo/',views.teams_detail),
    # path('teaminfo/<int:pk>',views.team_detail),
    # path('teamcreate/',views.team_create),
    # path('teamupdate/',views.team_update),
    # path('teamdlt/',views.team_dlt),
    path('team_api/',views.team_api),
    # team members
    path('teammemberinfo/',views.teammembers_detail),
    path('teammember_api/',views.teammembers_api),
    # path('teammemberinfo/<int:pk>',views.teammember_detail),
    # path('team_member_create/',views.teammember_create),
    

]
