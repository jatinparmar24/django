import requests
import pycountry
from django.shortcuts import render
from .form import CityForm
from decouple import config

def get_country_name(code):
    try:
        country = pycountry.countries.get(alpha_2=code)
        if country:
            return country.name
    except:
        pass
    return code  # fallback: return code if no match

def weather(request):
    weather_data = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = config('OPENWEATHER_API_KEY')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                full_country_name = get_country_name(data['sys']['country'])
                weather_data = {
                    'city': data['name'],
                    'country': full_country_name,
                    'temperature': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'wind_speed': data['wind']['speed'],
                    'description': data['weather'][0]['description'].title(),
                    'icon': data['weather'][0]['icon'],
                    'coordinates': f"{data['coord']['lat']}, {data['coord']['lon']}",
                }
            else:
                weather_data = {'error': 'City not found'}
    else:
        form = CityForm()

    return render(request, 'weather.html', {'form': form, 'weather_data': weather_data})
