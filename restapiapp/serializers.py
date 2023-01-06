from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model 
from rest_framework import serializers
from .models import Student, Project, Team, TeamMember

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
        # fields=['id','name','roll','city']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields="__all__"
        # fields=['team_name','team_start_date','team_end_date','team_lead','team_lead_email']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamMember
        fields="__all__"
        # fields=['team_name','name','role','email']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"
        # fields=['proj_name','proj_start_date','proj_end_date','manager_name','manager_email','status','desc']
