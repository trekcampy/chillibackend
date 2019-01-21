from .scraping import getChilliScovilleValues
from .models import ChilliHeat

def GetChilliScovilleValues():
    chilliList = []

    if ChilliHeat.objects.count() == 0:
        chilliScovilleValues = getChilliScovilleValues()
        for c in chilliScovilleValues:
            ChilliHeat.objects.create(chilli_type=c['name'], 
                                    scoville_value=c['scoville'])

    for c in ChilliHeat.objects.all():
            chilliList.append({ "name": c.chilli_type, 
                                "scoville" : c.scoville_value })

    return chilliList