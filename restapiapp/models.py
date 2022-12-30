from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)

class Project(models.Model):
    proj_name=models.CharField(max_length=100)
    manager_name=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)

class Team(models.Model):
    team_name=models.CharField(max_length=50)
    team_start_date= models.DateField()
    team_end_date= models.DateField()
    team_lead=models.CharField(max_length=50)
    team_lead_email=models.EmailField()

class TeamMember(models.Model):
    team_name=models.CharField(max_length=50, default='team name')
    name=models.CharField(max_length=50)
    role=models.CharField(max_length=50)


    