from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Model Object  - Single Student Object 
# fucntion based view 
def student_detail(request,pk):
    stu = Student.objects.get(id=pk) 
    # print(stu)
    #this is the model obeject 
    serializer =  StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # serialized data for storing serializ variable (python object) ----
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # serialized data converting for json object ----
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data)
    # sending respose for the client


# fucntion based view 
# Query Set -- All Student Data
def student_list(request):
    stu = Student.objects.all()
    print(stu)
    #this is the model obeject 
    serializer =  StudentSerializer(stu,many=True)
    print(serializer)
    print(serializer.data)
    # serialized data for storing serializ variable (python object) ----
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    # serialized data converting for json object ----
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)
    # sending respose for the client