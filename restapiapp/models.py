from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)

class Project(models.Model):
    proj_name=models.CharField(max_length=100)
    proj_start_date= models.DateField()
    proj_end_date= models.DateField()
    manager_name=models.CharField(max_length=20)
    manager_email=models.EmailField()
    status=models.BooleanField()
    desc=models.CharField(max_length=200)

class Team(models.Model):
    # team_id=models.AutoField(primary_key=True)
    team_name=models.CharField(max_length=50)
    team_start_date= models.DateField()
    team_end_date= models.DateField()
    team_lead=models.CharField(max_length=50)
    team_lead_email=models.EmailField()

    def __srt__(self):
        return self.team_name

class TeamMember(models.Model):
    # team_name=models.ForeignKey(Team, on_delete=models.CASCADE)
    team_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    email=models.EmailField()