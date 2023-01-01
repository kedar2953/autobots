from django.shortcuts import render
from .models import Student, Project, Team, TeamMember
from .serializers import StudentSerializer, ProjectSerializer, TeamSerializer, TeamMemberSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.response import Response
from rest_framework import status,viewsets

class StudentViewSet(viewsets.ViewSet):
    # GET all students
    def list(self,request):
        stu= Student.objects.all()
        serializer= StudentSerializer(stu,many=True)     
        return Response(serializer.data)
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
    # GET all students
    def list(self,request):
        stu= Project.objects.all()
        serializer= ProjectSerializer(stu,many=True)     
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

