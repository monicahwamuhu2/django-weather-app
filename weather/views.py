# Create your views here.
import requests
from django.shortcuts import render

def weather_home(request):
    city = request.GET.get('city', 'Nairobi')  # Default city
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()

    context = {
        'city': city,
        'temperature': weather_data['main']['temp'] if 'main' in weather_data else 'N/A',
        'weather': weather_data['weather'][0]['description'] if 'weather' in weather_data else 'N/A',
        'icon': weather_data['weather'][0]['icon'] if 'weather' in weather_data else 'N/A',
    }
    
    return render(request, 'weather/weather_home.html', context)
