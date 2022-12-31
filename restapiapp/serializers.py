from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student, Project, Team, TeamMember

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

    # field level validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError("Seat full!")
        return value

class ProjectSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    proj_name=serializers.CharField(max_length=100)
    proj_start_date= serializers.DateField()
    proj_end_date= serializers.DateField()
    manager_name=serializers.CharField(max_length=20)
    manager_email=serializers.EmailField()
    status=serializers.BooleanField()
    desc=serializers.CharField(max_length=200)

    def create(self, validate_data):
        return Project.objects.create(**validate_data)

class TeamSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    team_name=serializers.CharField(max_length=50)
    team_start_date= serializers.DateField()
    team_end_date= serializers.DateField()
    team_lead=serializers.CharField(max_length=50)
    team_lead_email=serializers.EmailField()

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.team_name=validated_data.get('team_name',instance.team_name)
        instance.team_start_date=validated_data.get('team_start_date',instance.team_start_date)
        instance.team_end_date=validated_data.get('team_end_date',instance.team_end_date)
        instance.team_lead=validated_data.get('team_lead',instance.team_lead)
        instance.team_lead_email=validated_data.get('team_lead_email',instance.team_lead_email)
        instance.save()
        return instance

class TeamMemberSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    team_name=serializers.CharField(max_length=50)
    name=serializers.CharField(max_length=50)
    role=serializers.CharField(max_length=50)
    email=serializers.EmailField()

    def create(self, validated_data):
        return TeamMember.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.team_name=validated_data.get('team_name',instance.team_name)
        instance.name=validated_data.get('name',instance.name)
        instance.role=validated_data.get('role',instance.role)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance
