from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model 
from rest_framework import serializers
from .models import Student, Project, Team, TeamMember

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['id','team_name','team_start_date','team_end_date','team_lead','team_lead_email']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamMember
        fields=['id','team_name','name','role','email']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id','proj_name','proj_start_date','proj_end_date','manager_name','manager_email','status','desc']
