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

# @method_decorator(csrf_exempt,name='dispatch')
# class StudentApi(View):
#     def get(self,request,*args, **kwargs):
#         json_data= request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             team=Student.objects.get(id=id)
#             serializer=StudentSerializer(team)
#             json_data=JSONRenderer().render(serializer)
#             return HttpResponse(json_data,content_type='application/json')
#             # return JsonResponse(serializer.data)

#         teams= Team.objects.all()
#         serializer= TeamSerializer(teams,many=True)
#         json_data= JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')


# ################################# CRUD Functions##############################

# CRUD Function for Student
@csrf_exempt
def student_api(request):
    if request.method=='GET':
        json_data= request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            team=Student.objects.get(id=id)
            serializer=StudentSerializer(team)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(serializer.data)
        teams= Student.objects.all()
        serializer= StudentSerializer(teams,many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='POST':
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer= StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created!'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        team=Student.objects.get(id=id)
        team.delete()
        res={'msg':'Team deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
# ---------------------------------------------------------------------------------------

# CRUD Function for team
@csrf_exempt
def team_api(request):
    if request.method=='GET':
        json_data= request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            team=Team.objects.get(id=id)
            serializer=TeamSerializer(team)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(serializer.data)
        teams= Team.objects.all()
        serializer= TeamSerializer(teams,many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='POST':
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer= TeamSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created!'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Team.objects.get(id=id)
        serializer=TeamSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        team=Team.objects.get(id=id)
        team.delete()
        res={'msg':'Team deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
# -----------------------------------------------------------------------------------

# CRUD function for team members
@csrf_exempt
def teammembers_api(request):
    if request.method=='GET':
        json_data= request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            team=TeamMember.objects.get(id=id)
            serializer=TeamMemberSerializer(team)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(serializer.data)
        teams= Team.objects.all()
        serializer= TeamSerializer(teams,many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='POST':
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer= TeamMemberSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created!'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=TeamMember.objects.get(id=id)
        serializer=TeamMemberSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        team=TeamMember.objects.get(id=id)
        team.delete()
        res={'msg':'Team deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
# ---------------------------------------------------------------------------

# GET all student data
def students_detail(request):
    # select model object
    stu=Student.objects.all()
    # convert to python dictionary  
    serializer=StudentSerializer(stu, many=True)
    # convert that python dec data to JSON
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# GET student one by one
def student_detail(request,pk):
    # select model object
    stu=Student.objects.get(id=pk)
    # convert to python dictionary  
    serializer=StudentSerializer(stu)
    # convert that python dec data to JSON
    # json_data= JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# create new entry in DB using POST request
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data= request.body
        # convert JSON data to Bytes
        stream= io.BytesIO(json_data)
        # convert stream of Bytes into Pythondata
        pythondata= JSONParser().parse(stream)
        # convert python data to complex data
        serializer= StudentSerializer(data=pythondata)
        # validate the data 
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created!'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
# UPDATE student
@csrf_exempt
def student_update(request):
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

# GET all project information
def projects_info(request):
    proj= Project.objects.all()
    serializer=ProjectSerializer(proj, many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

# GET one by one
def project_detail(request,pk):
    proj=Project.objects.get(id=pk)
    serializer=ProjectSerializer(proj)
    # json_data=JSONRenderer().render(serializer)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

#POST project
@csrf_exempt
def project_create(request):
    if request.method=='POST':
        json_data=request.body
        # convert json into stream of bytes
        stream= io.BytesIO(json_data)
        # convert stream into python data
        pythondata=JSONParser().parse(stream)
        # python data into complex data
        serializer=ProjectSerializer(data=pythondata)
        # validate the data
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Project added succesfully!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

# ---------------------------------------------------------------------------------
# GET all Teams
def teams_detail(request):
    teams= Team.objects.all()
    serializer= TeamSerializer(teams,many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

# # GET team one by one
# def team_detail(request,pk):
#     team=Team.objects.get(id=pk)
#     serializer=TeamSerializer(team)
#     # json_data=JSONRenderer().render(serializer)
#     # return HttpResponse(json_data,content_type='application/json')
#     return JsonResponse(serializer.data)

# #POST team
# @csrf_exempt
# def team_create(request):
#     if request.method=='POST':
#         json_data=request.body
#         # convert json into stream of bytes
#         stream= io.BytesIO(json_data)
#         # convert stream into python data
#         pythondata=JSONParser().parse(stream)
#         # python data into complex data
#         serializer=TeamSerializer(data=pythondata)
#         # validate the data
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Team added succesfully!'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data= JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

# # UPDATE team
# @csrf_exempt
# def team_update(request):
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Team.objects.get(id=id)
#         serializer=TeamSerializer(stu,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Team updated'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data= JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

# # DELETE Team
# @csrf_exempt
# def team_dlt(request):
#     if request.method=='DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         team=Team.objects.get(id=id)
#         team.delete()
#         res={'msg':'Team deleted'}
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')
# -------------------------------------------------------------------------

# GET all team members
def teammembers_detail(request):
    teams= TeamMember.objects.all()
    serializer= TeamMemberSerializer(teams,many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

# # GET team member one by one
# def teammember_detail(request,pk):
#     team=TeamMember.objects.get(id=pk)
#     serializer=TeamMemberSerializer(team)
#     # json_data=JSONRenderer().render(serializer)
#     # return HttpResponse(json_data,content_type='application/json')
#     return JsonResponse(serializer.data)

# #POST team member
# @csrf_exempt
# def teammember_create(request):
#     if request.method=='POST':
#         json_data=request.body
#         # convert json into stream of bytes
#         stream= io.BytesIO(json_data)
#         # convert stream into python data
#         pythondata=JSONParser().parse(stream)
#         # python data into complex data
#         serializer=TeamMemberSerializer(data=pythondata)
#         # validate the data
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Team added succesfully!'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data= JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

