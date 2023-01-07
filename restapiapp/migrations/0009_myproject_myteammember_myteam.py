# Generated by Django 4.1.4 on 2023-01-07 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapiapp', '0008_remove_team_team_id_team_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('proj_id', models.AutoField(primary_key=True, serialize=False)),
                ('proj_name', models.CharField(max_length=100)),
                ('proj_start_date', models.DateField()),
                ('proj_end_date', models.DateField()),
                ('manager_name', models.CharField(max_length=20)),
                ('manager_email', models.EmailField(max_length=254)),
                ('status', models.BooleanField()),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyTeamMember',
            fields=[
                ('team_member_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MyTeam',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=50)),
                ('team_start_date', models.DateField()),
                ('team_end_date', models.DateField()),
                ('team_lead', models.CharField(max_length=50)),
                ('team_lead_email', models.EmailField(max_length=254)),
                ('proj_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapiapp.myproject')),
            ],
        ),
    ]
