from django.contrib import admin
from .models import Student,Project,Team,TeamMember,MyProject,MyTeam,MyTeamMember
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','proj_name','manager_name','desc']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['id','team_name','team_start_date','team_end_date','team_lead','team_lead_email']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display=['id','team_name','name','role']
# ///////////////////////////////////////////////////////////////////
class MyTeamAdmin(admin.ModelAdmin):
    list_display=['team_name','team_start_date','team_end_date','team_lead','team_lead_email','proj_name']
admin.site.register(MyTeam,MyTeamAdmin)

class MyTeamMemberAdmin(admin.ModelAdmin):
    list_display=['team_name','name','role']
admin.site.register(MyTeamMember,MyTeamMemberAdmin)

class MyProjectAdmin(admin.ModelAdmin):
    list_display=['proj_name','manager_name','desc']
admin.site.register(MyProject,MyProjectAdmin)
# @admin.register(MyProject)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display=['proj_name','manager_name','desc']

# @admin.register(MyTeam)
# class TeamAdmin(admin.ModelAdmin):
#     list_display=['team_name','team_start_date','team_end_date','team_lead','team_lead_email','proj_name']

# @admin.register(MyTeamMember)
# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display=['team_name','name','role']