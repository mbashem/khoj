import io

from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer

import io

from rest_framework.renderers import JSONRenderer

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)




def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg' : 'Data Inserted'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')



@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body;
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Data Inserted'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'data updated'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        stu = Student.objects.get(id=id)
        stu.delete()

        msg = {'msg' : 'data deleted'}

        json_data = JSONRenderer().render(msg)

        return HttpResponse(json_data, content_type='application/json')


