from django.shortcuts import render
from .models import Student, Project, Team, TeamMember, MyProject,MyTeam,MyTeamMember
# from .serializers import StudentSerializer, ProjectSerializer, TeamSerializer, TeamMemberSerializer
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.response import Response
from rest_framework import status,viewsets
# AUTH
from .customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
import datetime
from django.core.mail import send_mail


class MyTeamViewSet(viewsets.ViewSet):
    # GET all students
    def list(self,request):
        stu= MyTeam.objects.all()
        serializer= MyTeamSerializer(stu,many=True)  
        # context={
        #     'stu':stu
        # }   
        # return render(request,'index_2.html',context)
        return Response(serializer.data)
    # GET specific student
    def retrieve(self, request, pk=None):
        team_id=pk
        if team_id is not None:
            team=MyTeam.objects.get(team_id=team_id)
            serializer=MyTeamSerializer(team)  
            return Response(serializer.data)
    # POST student
    def create(self, request):
        serializer=MyTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE totally
    def update(self,request, pk):
        id=pk
        stu=MyTeam.objects.get(pk=id)
        serializer=MyTeamSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # UPDATE partial
    def partial_update(self,request, pk):
        id=pk
        stu=MyTeam.objects.get(pk=id)
        serializer=MyTeamSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def destroy(self,request,pk):
        id=pk
        stu=MyTeam.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})

class MyProjectViewSet(viewsets.ViewSet):
    # GET all students
    def list(self,request):
        stu= MyProject.objects.all()
        serializer= MyProjectSerializer(stu,many=True)  
        context={
            'stu':stu
        }   
        return render(request,'index_2.html',context)
        # return Response(serializer.data)
    # GET specific student
    def retrieve(self, request, pk=None):
        team_id=pk
        if team_id is not None:
            team=MyProject.objects.get(team_id=team_id)
            serializer=MyProjectSerializer(team)  
            return Response(serializer.data)
    # POST student
    def create(self, request):
        serializer=MyProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE totally
    def update(self,request, pk):
        id=pk
        stu=MyProject.objects.get(pk=id)
        serializer=MyProjectSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # UPDATE partial
    def partial_update(self,request, pk):
        id=pk
        stu=MyProject.objects.get(pk=id)
        serializer=MyProjectSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def destroy(self,request,pk):
        id=pk
        stu=MyProject.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})

class MyTeamMemberViewSet(viewsets.ViewSet):
    # GET all students
    def list(self,request):
        stu= MyTeamMember.objects.all()
        serializer= MyTeamMemberSerializer(stu,many=True)  
        # context={
        #     'stu':stu
        # }   
        # return render(request,'index_2.html',context)
        return Response(serializer.data)
    # GET specific student
    def retrieve(self, request, pk=None):
        team_id=pk
        if team_id is not None:
            team=MyTeamMember.objects.get(team_id=team_id)
            serializer=MyTeamMemberSerializer(team)  
            return Response(serializer.data)
    # POST student
    def create(self, request):
        serializer=MyTeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE totally
    def update(self,request, pk):
        id=pk
        stu=MyTeamMember.objects.get(pk=id)
        serializer=MyTeamMemberSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # UPDATE partial
    def partial_update(self,request, pk):
        id=pk
        stu=MyTeamMember.objects.get(pk=id)
        serializer=MyTeamMemberSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def destroy(self,request,pk):
        id=pk
        stu=MyTeamMember.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})


# ////////////////////////////////////////////////////////////////////////////////////
class StudentViewSet(viewsets.ViewSet):
    # GET all students
    def list(self,request):
        stu= Student.objects.all()
        serializer= StudentSerializer(stu,many=True)  
        context={
            'stu':stu
        }   
        return render(request,'index_2.html',context)
        # return Response(serializer.data)
    # GET specific student
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            team=Student.objects.get(id=id)
            serializer=StudentSerializer(team)  
            return Response(serializer.data)
    # POST student
    def create(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE totally
    def update(self,request, pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # UPDATE partial
    def partial_update(self,request, pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def destroy(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})

# ///////////////////////TEAM//////////////////
class TeamViewSet(viewsets.ViewSet):
    # GET all students
    def list(self,request):
        stu= Team.objects.all()
        serializer= TeamSerializer(stu,many=True)  
        context={
            # 'stu':serializer.data
            'stu':stu
        }   
        print(context)
        # return render(request,'index_2.html',context)
        return Response(serializer.data)
    # GET specific student
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            team=Team.objects.get(id=id)
            serializer=TeamSerializer(team)  
            return Response(serializer.data)
    # POST student
    def create(self, request):
        serializer=TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE totally
    def update(self,request, pk):
        id=pk
        stu=Team.objects.get(pk=id)
        serializer=TeamSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # UPDATE partial
    def partial_update(self,request, pk):
        id=pk
        stu=Team.objects.get(pk=id)
        serializer=TeamSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def destroy(self,request,pk):
        id=pk
        stu=Team.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})

# ///////////////////////TEAM MEMBER//////////////////
class TeamMemberViewSet(viewsets.ViewSet):
    # GET all students
    def list(self,request):
        stu= TeamMember.objects.all()
        serializer= TeamMemberSerializer(stu,many=True)     
        return Response(serializer.data)
    # GET specific student
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            team=TeamMember.objects.get(id=id)
            serializer=TeamMemberSerializer(team)  
            return Response(serializer.data)
    # POST student
    def create(self, request):
        serializer=TeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE totally
    def update(self,request, pk):
        id=pk
        stu=TeamMember.objects.get(pk=id)
        serializer=TeamMemberSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # UPDATE partial
    def partial_update(self,request, pk):
        id=pk
        stu=TeamMember.objects.get(pk=id)
        serializer=TeamMemberSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def destroy(self,request,pk):
        id=pk
        stu=TeamMember.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})

# ///////////////////////Project//////////////////
class ProjectViewSet(viewsets.ViewSet):
    # Custom AUTH
    # authentication_classes=[CustomAuthentication]
    # permission_classes=[IsAuthenticated]
    # GET all students
    def list(self,request):
        stu= Project.objects.all()
        serializer= ProjectSerializer(stu,many=True)  
        context={
            'stu':stu
        }   
        # return render(request,'index_2.html',context)   
        return Response(serializer.data)
    # GET specific student
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            team=Project.objects.get(id=id)
            serializer=ProjectSerializer(team)  
            return Response(serializer.data)
    # POST student
    def create(self, request):
        serializer=ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE totally
    def update(self,request, pk):
        id=pk
        stu=Project.objects.get(pk=id)
        serializer=ProjectSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # UPDATE partial
    def partial_update(self,request, pk):
        id=pk
        stu=Project.objects.get(pk=id)
        serializer=ProjectSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def destroy(self,request,pk):
        id=pk
        stu=Project.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'})



#  ------------------------------------------FUNCTIONS FOR MAIL AND FTECHING UPDATES------------------------------------------------------------------------------

# ------------------THIS IS FOR HOME PAGE FUNCTION FOR FETCHING DATA FROM API-------------------

def home_page(request):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    # mail_send_time = time(14 , 20 , 00 ,00)
    # print("sending time of the mail:" , mail_send_time)
     
    print("-----------")
    print("the current time is:" , current_time)
    url = "http://127.0.0.1:8000/team_member_api"
    req = requests.get(url) 
    response = req.json()
    print("the length of API is" , len(response))
    print("this is  home page running")
    email_list = []
    for item in response:
        email = item['email']
        print(email)
        email_list.append(email)
    print("printing the list of the email")
    print(email_list)
    url2 = "http://127.0.0.1:8000/project_api/"
    req2 = requests.get(url2)
    response2 = req2.json()
    print("this is UPDATE PART")
    print("the length of updates API is" , len(response2))
    length = len(response2)
    print(response2)
    update_of_project=response2[-1]['desc']
    print("in home_page")
    print("the update of the project is: " , update_of_project)
    # print("SENDING MAIL ")
    # for i in email_list:
    #     send_mail("this is subject of email" ,
    #     update_of_project , 
    #     'vedz0786@gmail.com',
    #     [i] , 
    #     fail_silently=False
    #     )
    # print("MAIL SENT")
    return HttpResponse(response)


# ------------------------------THIS IS FUNCTION TO SEND MAILS-----------------------

def sending_email():
    url = "http://127.0.0.1:8000/team_member_api/"
    req = requests.get(url) 
    response = req.json()
    print("the length of API is in sending mail function ==>>" , len(response))
    print("this is  home page running")
    email_list = []
    for item in response:
        email = item['email']
        print(email)
        email_list.append(email)
    print("printing the email list in sending mail function == >> " , email_list)
    url2 = "http://127.0.0.1:8000/project_api/"
    req2 = requests.get(url2)
    response2 = req2.json()
    print("this is UPDATE PART")
    print("the length of updates API is" , len(response2))
    length = len(response2)
    print(response2)
    update_of_project=response2[-1]['desc']
    print("the update of the project is in sending mail function ===>>: " , update_of_project)
    print("in sending_email")
    print("sending mail")
    for i in email_list:
        send_mail(
            #   subject=
            "This is Testing mail",
            # messageto be sent
            update_of_project,
            # mail to be sent from 
            "settings.EMAIL_HOST_USER",
            # mail to be sent to
            [i],
            fail_silently=False
        )
    print("mail sent")
    return HttpResponse("MAIL SENT")

