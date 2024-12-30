import requests

# Ваш API-ключ (зарегистрируйтесь на newsapi.org для получения ключа)
API_KEY = 'c82e74538af0484fa90679c4ca00e5bc'
BASE_URL = 'https://newsapi.org/v2/everything'

def fetch_news(keyword):
    # Параметры запроса
    params = {
        'q': keyword,
        'apiKey': API_KEY,
        'language': 'ru',  # Новости на русском (опционально)
        'sortBy': 'publishedAt'  # Сортировка по времени публикации
    }
    
    # Отправка запроса к API
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        
        # Если есть статьи, отображаем их
        if articles:
            for idx, article in enumerate(articles[:10], start=1):  # Ограничение до 10 новостей
                print(f"{idx}. Заголовок: {article['title']}")
                print(f"   Источник: {article['source']['name']}")
                print(f"   Время публикации: {article['publishedAt']}")
                print(f"   Ссылка: {article['url']}\n")
            return articles
        else:
            print("Новостей по вашему запросу не найдено.")
    else:
        print("Ошибка при получении новостей:", response.status_code)

def save_to_file(articles, filename="news_results.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, article in enumerate(articles[:10], start=1):
            file.write(f"{idx}. Заголовок: {article['title']}\n")
            file.write(f"   Источник: {article['source']['name']}\n")
            file.write(f"   Время публикации: {article['publishedAt']}\n")
            file.write(f"   Ссылка: {article['url']}\n\n")
    print(f"Результаты сохранены в файл {filename}")

if __name__ == "__main__":
    keyword = input("Введите ключевое слово или категорию для поиска новостей: ")
    news = fetch_news(keyword)
    if news:
        save_option = input("Хотите сохранить результаты в файл? (да/нет): ").strip().lower()
        if save_option == "да":
            save_to_file(news)
