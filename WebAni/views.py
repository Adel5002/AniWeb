from django.shortcuts import render
import requests

def index(request):
    api_url = 'https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&types=anime-serial'
    response = requests.get(api_url)
    data = response.json()


    titles = [item.get('title') for item in data['results'] if 'title' in item]
    screenshots = [item.get('screenshots') for item in data['results'] if 'screenshots' in item]

    data_list = [{'title': title, 'screenshot': screenshot} for title, screenshot in zip(titles, screenshots)]


    context = {
        'data': data_list,
    }


    return render(request, 'index.html', context)