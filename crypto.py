import requests
import time

def get_crypto_data(filter_name=None, filter_price=None):
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=15&page=1&sparkline=false"
        response = requests.get(url)
        
        # Проверка статуса ответа от API
        if response.status_code != 200:
            print("Ошибка при запросе данных.")
            return []

        data = response.json()  # Получаем данные в формате JSON
        filtered_data = []  # Список для отфильтрованных данных

        # Фильтрация по имени
        if filter_name:
            filter_name_lower = filter_name.lower()  # Преобразуем фильтр в нижний регистр для нечувствительности к регистру
            for coin in data:
                coin_name = coin["name"].lower()  # Имя криптовалюты в нижнем регистре
                if filter_name_lower in coin_name:  # Если имя криптовалюты содержит фильтр
                    filtered_data.append(coin)  # Добавляем в результат
            data = filtered_data  # Обновляем данные с учетом фильтра по имени

        # Фильтрация по цене
        if filter_price:
            filtered_data = []  # Новый список для отфильтрованных данных
            for coin in data:
                # Если текущая цена криптовалюты больше, чем заданный фильтр, добавляем её в новый список
                if coin["current_price"] > filter_price:
                    filtered_data.append(coin)  # Добавляем криптовалюту в список
            data = filtered_data  # Обновляем данные с учетом фильтра по цене

        return data  # Возвращаем отфильтрованные данные

    except Exception as e:
        print(f"Ошибка: {e}")
        return []

def display_data(data):
    if not data:
        print("Нет данных для отображения.")
        return

    for coin in data:
        print(f"Имя: {coin['name']}, Символ: {coin['symbol']}")
        print(f"Цена: ${coin['current_price']}, Рыночная капитализация: ${coin['market_cap']}")
        print(f"Объём: ${coin['total_volume']}, Изменение за 24ч: {coin['price_change_percentage_24h']}%")
        print("-" * 30)

def main():
    name_filter = input("Фильтр по имени (оставьте пустым для пропуска): ")
    price_filter_input = input("Фильтр по минимальной цене (оставьте пустым для пропуска): ")
    
    # Преобразуем введенную цену в число (если введена)
    if price_filter_input:
        try:
            price_filter = float(price_filter_input)
            print(f"Фильтр по цене установлен: {price_filter}")
        except ValueError:
            print("Ошибка: введено некорректное значение для фильтра по цене.")
            price_filter = None
    else:
        price_filter = None  # Если фильтр не задан, устанавливаем его как None

    while True:
        data = get_crypto_data(name_filter, price_filter)  # Получаем данные с учетом фильтров
        display_data(data)  # Отображаем отфильтрованные данные
        print("Обновление через 30 секунд...")
        time.sleep(30)  # Ждем 30 секунд перед следующим запросом

if __name__ == "__main__":
    main()
