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
        if "add" in new_data["operation_type"] or "addition" in new_data["operation_type"]:
            result = new_data["x"] + new_data["y"]
        elif new_data["operation_type"] == "subtraction" or "subtract" in new_data["operation_type"]:
            result = new_data["x"] - new_data["y"]
        else:
            result = new_data['x'] * new_data["y"]   
        return JsonResponse({
            'slackusername':'Chidera Onumajuru',
            'operation_type':new_data["operation_type"],
            'result':result},safe=False)

