import requests
api_key = "eff5e08eaced0078b09e3bd199f3d73a"
def fetch_weather_data(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        
        else:
            print(f"Ошибка: Сервер вернул статус-код {response.status_code}.")
    
    except Exception as err:
        print(f"Произошла ошибка: {err}")
    return None

def display_weather(data, city, option=None):
    if not data:
        print(f"Не удалось получить данные для города {city}.")
        return

    try:
        weather = data['weather'][0]["main"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        wind_speed = data["wind"]["speed"]

        print(f"Погода в городе {city}: {weather}")
        print(f"Температура: {temp}°C")
        print(f"Влажность: {humidity}%")
        print(f"Скорость ветра: {wind_speed} м/с")

        options = {
            "temperature": f"Температура: {temp}°C",
            
            "humidity": f"Влажность: {humidity}%",
            "wind": f"Скорость ветра: {wind_speed} м/с"
        }

        if  option in options:
            print(options[option])
        elif option:
            print(f"Неизвестный параметр: {option}")
    except KeyError as e:
        print(f"Ошибка: отсутствует ключ {e} в данных ответа API.")

def main():
    city = input("Введите название города: ")
    option = input("Введите параметр (temperature, density, humidity, wind) или оставьте пустым для всех данных: ").lower()
    data = fetch_weather_data(city)
    display_weather(data, city, option)

if __name__ == '__main__':
    main()

