from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def index(request):
    if request.method =='GET':
        all_user = User.objects.all()
        serializer = UserSerializer(all_user,many=True)
        return JsonResponse({
            "Sucess": True,
            "Users": serializer.data,
        })

    elif request.method == 'POST':
        user_to_get = JSONParser().parse(request)
        serializer = UserSerializer(data = user_to_get)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "Sucess":True,
                "users":serializer.data,
            })
        return  JsonResponse(serializer.errors,status=400) 

