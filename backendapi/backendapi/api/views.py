import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from product.models import Product

def home_api(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return JsonResponse(data)
