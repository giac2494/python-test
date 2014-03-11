from django.shortcuts import render
from enrolment.models import student
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime as d
from django.utils.timezone import utc

@csrf_exempt
def home(request):
    if request.method == 'POST':
        body = request.body
        content = json.loads(body)
        stud = student(f_name=content['f_name'],l_name=content['l_name'])
        stud.save()
        return HttpResponse(status=200)
    elif request.method == 'GET':
        #leggiamo da db e ritorniamo al client
        stud = student.objects.all()
        list_student = [{'f_name':s.f_name,'l_name':s.l_name,'time':str(s.time)}for s in stud]
        resp = json.dumps(list_student)
        return HttpResponse(resp, content_type='application/json')