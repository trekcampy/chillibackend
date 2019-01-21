from django.http import HttpResponse
from django.http import JsonResponse
from .GetChillis import GetChilliScovilleValues

def chillilist(request):
    chilliList =  GetChilliScovilleValues()
    return JsonResponse(chilliList,safe=False)
