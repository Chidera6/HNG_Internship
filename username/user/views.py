from django.http import JsonResponse


# Create your views here.

def index(request):
    return JsonResponse({"slackUsername": "Chidera Onumajuru",
        "backend": True,
        "age": 26,
        "bio": "I am a Backend Developer,proficient in the use of Python,Flask framework,Postgresql and Django framework."})
