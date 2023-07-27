from django.shortcuts import render
from django.views.generic import ListView
import requests


class AnimeListView(ListView):
    model = None
    template_name = 'index.html'
    context_object_name = 'data'

    def get_queryset(self):
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
                data_list.append({'title': title, 'poster_url': poster_url, 'description': description, 'year': year,
                                  'title_orig': title_orig, 'genres': genres})
                unique_titles.add(title)  # Добавляем заголовок во множество
        return data_list


class SearchView(ListView):
    model = None
    template_name = 'index.html'
    context_object_name = 'data'

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        search_query = self.request.GET['search_query']
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
        return data_list
