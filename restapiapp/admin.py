from django.contrib import admin
from .models import Student,Project,Team,TeamMember
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