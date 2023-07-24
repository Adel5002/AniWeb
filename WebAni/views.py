from django.shortcuts import render
import requests

def index(request):
    api_url = 'https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true'
    response = requests.get(api_url)
    data = response.json()

    data_list = []

    unique_titles = set()

    for item in data['results']:
        title = item.get('title')
        poster_url = item['material_data']['poster_url']
        description = item['material_data'].get('description')
        genres = item['material_data'].get('genres')
        year = item.get('year')
        title_orig = item.get('title_orig')
        # Проверяем, не было ли уже такого заголовка в списке
        if title not in unique_titles:
            data_list.append({'title': title, 'poster_url': poster_url, 'description': description, 'year': year, 'title_orig': title_orig, 'genres': genres})
            unique_titles.add(title)  # Добавляем заголовок во множество

    context = {
        'data': data_list,
    }

    return render(request, 'index.html', context)


def search(request):
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        api_url = f'https://kodikapi.com/search?token=56a40dfa2b3c22e9f8252a8d6cc78b54&types=anime&with_material_data=true&title={search_query}'
        response = requests.get(api_url)
        data = response.json()

        data_list = []

        unique_titles = set()

        for item in data['results']:
            title = item.get('title')
            poster_url = item['material_data']['poster_url']
            description = item['material_data'].get('description')
            year = item.get('year')
            title_orig = item.get('title_orig')
            genres = item['material_data'].get('genres')
            # Проверяем, не было ли уже такого заголовка в списке
            if title not in unique_titles:
                data_list.append({'title': title, 'poster_url': poster_url, 'description': description, 'year': year, 'title_orig': title_orig, 'genres': genres})
                unique_titles.add(title)  # Добавляем заголовок во множество
        context = {
            'data': data_list,
        }

        return render(request, 'index.html', context)
    return render(request, 'index.html')