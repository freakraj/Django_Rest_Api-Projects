from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view()
# def hello_word(request):
#     return Response({'msg':'HELLO Word'})

# Create your views here.
# @api_view(['GET'])
# def hello_word(request):
#     return Response({'msg':'HELLO Word'})

@api_view(['GET','POST'])
def hello_word(request):
    if request.method == "GET":
        print(request.data)
        return Response({'msg':'this is the Get Request'})

    if request.method == "POST":
        print(request.data)
        return Response({'msg':'this is the post request','data':request.data})

    