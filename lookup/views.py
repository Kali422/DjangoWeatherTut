from django.shortcuts import render


# Create your views here.
# This is views

def home(request):
    import json, requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=F4F232C9-A2C1-41FA-BAF0-CA014E6B118F")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == 'Good':
            category_color = "good"

        elif api[0]['Category']['Name'] == 'Moderate':
            category_color = "moderate"
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
            category_color = "usg"
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == 'Hazardous':
            category_color = "hazardous"

        # http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-02-06&distance=5&API_KEY=F4F232C9-A2C1-41FA-BAF0-CA014E6B118F

        return render(request, 'home.html', {'api': api, 'category_color': category_color})

    else:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-02-06&distance=5&API_KEY=F4F232C9-A2C1-41FA-BAF0-CA014E6B118F")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == 'Good':
            category_color = "good"

        elif api[0]['Category']['Name'] == 'Moderate':
            category_color = "moderate"
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
            category_color = "usg"
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == 'Hazardous':
            category_color = "hazardous"

        # http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-02-06&distance=5&API_KEY=F4F232C9-A2C1-41FA-BAF0-CA014E6B118F

        return render(request, 'home.html', {'api': api, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
