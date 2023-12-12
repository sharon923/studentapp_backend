from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from students.serializer import StudentSerializer
from students.models import StudentModel
from django.db.models import Q

# Create your views here.
@csrf_exempt 
def viewAll(request):
    if request.method == "POST":
        studet_list = StudentModel.objects.all()
        serialized_data = StudentSerializer(studet_list, many=True)
        return HttpResponse(json.dumps(serialized_data.data))

@csrf_exempt   
def addStudent(request):
    if request.method == "POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check= StudentSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"succsess"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
    
@csrf_exempt 
def searchStudent(request):
    if request.method == "POST":
        recieved_data  = json.loads(request.body)
        print(recieved_data)
        getadmn = recieved_data["admno"]
        print(getadmn)
        data = list(StudentModel.objects.filter(Q(admno__icontains = getadmn)).values())
        return HttpResponse(json.dumps(data))
    
@csrf_exempt 
def deleteStudent(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"status":"student deleted"}))
    


