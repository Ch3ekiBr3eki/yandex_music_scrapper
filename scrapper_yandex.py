import requests
from bs4 import BeautifulSoup
import lxml
import time
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
yandex_link = 'https://music.yandex.ru/chart' # Ссылка на топ от яндекс музыки

def get_links(yandex_link):
    # Отправляем GET-запрос на сайт 
    res = requests.get(
        yandex_link,
        headers=headers
    )
    if res.status_code != 200:
        return  # Если запрос не успешен, завершаем функцию
    
    soup = BeautifulSoup(res.content, "lxml")  # Создаем объект BeautifulSoup для парсинга страницы

    try: # Итерируемся по всем песням на странице топ-100 песен и сохраняем ссылку на каждую песню
        if res.status_code == 200: 
            for a in soup.find_all('a',attrs={"class":"d-track__title deco-link deco-link_stronger"}): 
                yield f'https://music.yandex.ru/{a.attrs["href"]}'  # Возвращаем ссылку на вакансию. Не забываем добавить https://music.yandex.ru/
    except Exception as e:
        print(f"{e}")  # В случае ошибки выводим сообщение
    time.sleep(1)  # Добавляем небольшую задержку между запросами

def get_basic_info(yandex_link):
        # Отправляем GET-запрос на сайт 
    res = requests.get(
        yandex_link,
        headers=headers
    )
    if res.status_code != 200:
        return  # Если запрос не успешен, завершаем функцию
    
    soup = BeautifulSoup(res.content, "lxml")  # Создаем объект BeautifulSoup для парсинга страницы
    song_info_list = []  # Список для хранения информации о песнях

    try:
        if res.status_code == 200:
            # Находим все строки с информацией о песнях
            song_rows = soup.find_all('div', attrs={"class": "d-track typo-track d-track_selectable d-track_with-cover d-track_with-chart"})
            pos = 0
            for song_row in song_rows:
                song_info = {}  # Словарь для хранения информации о текущей песне
                
                # Извлекаем название трека
                song_info["title"] = song_row.find('a', attrs={"class": "d-track__title deco-link deco-link_stronger"}).text[2:-2]
                
                # Извлекаем длительность песни
                song_info["duration"] = song_row.find('span', attrs={"class": "typo-track deco-typo-secondary"}).text
                
                # Извлекаем топ в чарте, тк мы парсим треки по порядку, можем просто пронумеровать треки
                song_info["chart_position"] = 1 + pos
                
                # Добавляем информацию о песне в список
                song_info_list.append(song_info)
                # Обновляем счётчик
                pos += 1
    except Exception as e:
        print(f"Ошибка при извлечении информации: {e}")

    return song_info_list

def get_track(link):
    # Отправляем GET-запрос на страницу песни
    data1 = requests.get(
        url=link,
        headers=headers
    )
    if data1.status_code != 200:
        return  # Если запрос не успешен, завершаем функцию
    
    soup = BeautifulSoup(data1.content, "lxml")  # Создаем объект BeautifulSoup для парсинга страницы

    try:
        # Ищем жанр песни
        genre = soup.find(attrs={'d-link deco-link deco-link_mimic typo'}).text
    except:
        genre = []
    
    try:
        # Ищем исполнителя или исполнителей песни
        artist = [artist.text for artist in soup.find(attrs={"class":"d-artists"}).find_all("a",attrs={"class":"d-link deco-link"})]
    except:
        artist = []
    
    Explicit = 0
    try:
        # Ищем содержит ли песня explicit или нет 
        if soup.find("span", attrs={"d-explicit-mark d-explicit-mark--e d-explicit-mark--large"}):
            Explicit = 1
    except:
        pass

    try:
        # Ищем исполнителя или исполнителей песни
        artist_links = [f'https://music.yandex.ru{artist["href"]}' for artist in soup.find(attrs={"class":"d-artists"}).find_all("a", attrs={"class":"d-link deco-link"})]
    except:
        artist_links = []

    monthly_listen_total = 0
    artist_likes_total = 0

    # Пройдёмся по каждой ссылке отдельного исполнителя трека
    for i in range(len(artist_links)):
        data2 = requests.get(
            url=artist_links[i],
            headers=headers
        )

        if data2.status_code != 200:
            return

        artistsoup = BeautifulSoup(data2.content, "lxml")

        try: 
            # Найдём общее колличество месячных прослушиваний для исполнителей трека
            monthly_listen_text = artistsoup.find(attrs={"page-artist__summary typo deco-typo-secondary"}).text
            monthly_listen_text = monthly_listen_text.replace(' ', '')  # Убираем пробелы
            monthly_listen_text = monthly_listen_text.replace('слушателейзамесяц', '')  # Убираем "слушателейзамесяц"
            monthly_listen_text = monthly_listen_text.replace('слушателязамесяц', '') # Оказывается существует ещё и "слушателязамесяц", так что убираем и это тоже
            monthly_listen_text = monthly_listen_text.replace('слушательзамесяц', '') # Оказывается ещё и "слушательзамесяц" имеет место быть
            monthly_listen = int(monthly_listen_text)  # Преобразовываем оставшуюся строку в целое число
            monthly_listen_total += monthly_listen
        except:
            monthly_listen = 0
        
        try: 
            # Найдём общее колличество сердечк для исполнителей трека
            artist_likes = artistsoup.find(attrs={"d-button__label"}).text
            artist_likes = int(artist_likes.replace(' ', ''))  # Преобразовываем строку в целое число и убираем запятые
            artist_likes_total += artist_likes
        except:
            artist_likes = 0

    # Создаем словарь с данными о песни
    track = {
        "link": link,
        'genre': genre,
        'artist(s)': artist,
        'Explicit_content': Explicit,
        'monthly_listens_total': monthly_listen_total,
        'artists_likes_total': artist_likes_total,
    }
    return track

if __name__ == '__main__':
    links = list(get_links(yandex_link))  # Получаем список ссылок на каждый трек из топа
    song_info_list = get_basic_info(yandex_link) # Получаем список из словарей с базовой информацией о каждом треке из топ 100
    tracks = []
    combined_data = []

    # Итерируемся по ссылкам и выводим информацию о песнях  
    for link in links:
        track_info = get_track(link)  # Получаем данные о треках
        tracks.append(track_info)  # Добавляем данные в список
        time.sleep(1) # Добавим паузу между итерациями

    for song_info, track_info in zip(song_info_list, tracks):
        combined_data.append({
            "name": song_info["title"],
            "track_len": song_info["duration"],
            "link": track_info["link"],
            "genre": track_info["genre"],
            "artist(s)": track_info["artist(s)"],
            "chart": song_info["chart_position"],
            "Explicit_content": track_info["Explicit_content"],
            "monthly_listens_total": track_info["monthly_listens_total"],
            "artists_likes_total": track_info["artists_likes_total"]
        })

    # Задаем имена полей для CSV
    field_names = ["name", "track_len", "link", "genre", "artist(s)", "chart", "Explicit_content", "monthly_listens_total", "artists_likes_total"]

    # Открываем CSV файл для записи 
    with open('yandex_tracks_top100.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()  # Записываем заголовок

        for data in combined_data:
            writer.writerow(data)  # Записываем данные в файл
