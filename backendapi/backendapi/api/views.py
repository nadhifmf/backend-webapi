from django.http import JsonResponse


def home_api(request, *args, **kwargs):
    return JsonResponse({"message":"First message, Hello World!"})