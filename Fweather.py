from pygismeteo import Gismeteo

def GetWeather(mesInfo):
    sityName = mesInfo.text
    gismeteo=Gismeteo()
    if isinstance(sityName, str):
        search_results = gismeteo.search.by_query(sityName)
        city_id = search_results[0].id
        current = gismeteo.current.by_id(city_id)
        print(current.temperature.air.c, current.description.full,
              current.humidity.percent, current.cloudiness.percent)
        return sityName
    else:
        print(sityName)
        return sityName
