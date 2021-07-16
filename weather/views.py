from urllib.error import HTTPError, URLError
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import json
import urllib



# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=34bfbe4ab1a9db91f76132c5e119e553').read()
        #xcept Http404 error
        try:
            source = source
        except HTTPError:
            data = f'Couldnt find your {city}'
        except URLError:
            data = ""
            
        # converting json data to a dictionary

        #assigning list od data to json file
        list_of_data = json.loads(source)
        #setting up the dictionary(mapping of dictionary)
        data = {
            "country_code" : str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lat']) +" "+ str(list_of_data['coord']['lon']),
            'temp' : str(list_of_data['main']['temp'])+ " k",
            'pressure' : str(list_of_data['main']['pressure']) + " hPa",
            'humidity' : str(list_of_data["main"]["humidity"]) + " %",
            #"dew_point": str(list_of_data['main']["dew_point"])
        }
        print(data)
    else:
        data = {

        }
    return render(request, "main/index.html", data)
        