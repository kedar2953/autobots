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
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]
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

