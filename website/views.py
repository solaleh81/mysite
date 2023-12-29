from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse('http-test')

def json_test(request):
    return JsonResponse({'name': 'solale'})