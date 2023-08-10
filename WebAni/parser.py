import requests

def get_api_data(myId):
    api_url = "https://kodikapi.com/list?token=56a40dfa2b3c22e9f8252a8d6cc78b54&limit=100&types=anime&with_material_data=true"
    response = requests.get(api_url)
    data = response.json()

    for result in data['results']:
        if result['id'] == myId:
            # Выводим нужные данные из найденного объекта
            print("Название:", result['title'])
            print("Год:", result['year'])
            # и т.д.
            return

    # Если айдишник не найден
    print("Данные не найдены")

# Пример вызова функции с айдишником 97101
get_api_data('movie-97101')