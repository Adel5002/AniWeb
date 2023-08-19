from django.shortcuts import render
from django.views.generic import ListView, DetailView
import requests
from django.core.paginator import Paginator



def AnimeDetail(request, ide):
    url = "https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true"
    response = requests.get(url)
    data = response.json()

    data_list = {}
    unique_titles = set()

    print(ide)

    for item in data['results']:
        if item['id'] == ide:
            title = item.get('title')
            poster_url = item['material_data']['poster_url']
            description = item['material_data'].get('description')
            genres = item['material_data'].get('genres')
            year = item.get('year')
            title_orig = item.get('title_orig')
            print(title)
            print(ide)
            if title not in unique_titles:
                data_list.update({'title': title, 'poster_url': poster_url, 'description': description, 'year': year,

                                  'title_orig': title_orig, 'genres': genres})
                unique_titles.add(title)
            print(ide)

    return render(request, 'detail.html', data_list)


# class AnimeDetail(DetailView):
#     model = None  # Замените на вашу модель
#     template_name = 'detail.html'
#
#     def get(self, request, ide):
#         url = "https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true"
#         response = requests.get(url)
#         data = response.json()
#
#         for item in data['results']:
#             if item['id'] == ide:
#                 title = item.get('title')
#                 if 'material_data' in item:
#                     poster_url = item['material_data']['poster_url']
#                     description = item['material_data'].get('description')
#                     ide = item['material_data'].get('id')
#                     genres = item['material_data'].get('genres')
#                 else:
#                     poster_url = None
#                     description = None
#                     genres = None
#                     ide = None
#
#
#
#                 year = item.get('year')
#                 title_orig = item.get('title_orig')
#
#                 context = {
#                     'title': title,
#                     'poster_url': poster_url,
#                     'description': description,
#                     'year': year,
#                     'ide': ide,
#                     'title_orig': title_orig,
#                     'genres': genres
#                 }
#
#                 return render(request, self.template_name, context)


class AnimeListView(ListView):
    model = None
    template_name = 'index.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        page = self.request.GET.get('page')
        if page:
            api_url = f'https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true&page={page}'
        else:
            api_url = f'https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true&page_url={page}'



        response = requests.get(api_url)
        data = response.json()
        context['next_page'] = data.get('next_page')
        context['prev_page'] = data.get('prev_page')
        context['current_page'] = api_url


        return context

    def get_queryset(self):

        page = self.request.GET.get('page')
        if page:
            api_url = f'https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true&page={page}'
        else:
            api_url = 'https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true'

        response = requests.get(api_url)
        data = response.json()

        data_list = []
        unique_titles = set()

        for item in data['results']:
            ide = item.get('id')
            title = item.get('title')
            if 'material_data' in item:
                poster_url = item['material_data']['poster_url']
                description = item['material_data'].get('description')
                genres = item['material_data'].get('genres')
            else:
                poster_url = None
                description = None
                genres = None

            year = item.get('year')
            title_orig = item.get('title_orig')
            if title not in unique_titles:
                data_list.append({'title': title, 'poster_url': poster_url, 'description': description, 'year': year,

                                  'title_orig': title_orig, 'genres': genres, 'ide': ide})
                unique_titles.add(title)

        return data_list



class SearchView(ListView):
    model = None
    template_name = 'index.html'
    context_object_name = 'data'

    def get_queryset(self):
        search_query = self.request.GET['search_query']
        api_url = f'https://kodikapi.com/search?token=56a40dfa2b3c22e9f8252a8d6cc78b54&types=anime&with_material_data=true&title={search_query}'
        response = requests.get(api_url)
        data = response.json()

        data_list = []

        unique_titles = set()

        for item in data['results']:
            ide = item.get('id')
            title = item.get('title')
            poster_url = item['material_data']['poster_url']
            description = item['material_data'].get('description')
            year = item.get('year')
            title_orig = item.get('title_orig')
            genres = item['material_data'].get('genres')
                    # Проверяем, не было ли уже такого заголовка в списке
            if title not in unique_titles:
                data_list.append({'title': title, 'poster_url': poster_url, 'description': description, 'year': year, 'title_orig': title_orig, 'genres': genres, 'ide': ide})
                unique_titles.add(title)  # Добавляем заголовок во множество
        return data_list
