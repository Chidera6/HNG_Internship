from django.http import JsonResponse,HttpResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt

"""
def index():
    return JsonResponse({"slackUsername": "Chidera Onumajuru",
        "backend": True,
        "age": 26,
        "bio": "I am a Backend Developer,proficient in the use of Python,Flask framework,Postgresql and Django framework."})
"""
@csrf_exempt
def calculate(request):
    if request.method == "POST":
        new_data = loads(request.body.decode())
        x = ["add","addition","sum","plus"]
        for a in x:
            if a in new_data["operation_type"]:
                result = new_data["x"] + new_data["y"]
                a = "addition"
                num = a

        x = ["minus","subtraction","subtract","remove"]
        for a in x:
            if a in new_data["operation_type"]:
                result = new_data["x"] - new_data["y"]
                a = "subtraction"
                num = a

        x = ["multiply","multiplication","product","times"]
        for a in x:
            if a in new_data["operation_type"]:    
                result = new_data['x'] * new_data["y"]  
                a = "multiplication"
                num = a 

        return JsonResponse({
        'slackUsername':'Chidera Onumajuru',
        'operation_type':num,
        'result':result},safe=False)

