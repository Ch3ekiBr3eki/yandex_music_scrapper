# Yandex Music TOP 100 songs🎵 (Scrapper)
<p align="center">
      <img src="https://i.ibb.co/K5QHC1s/yandex-music.jpg" width="336">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/python-blue" alt="python">
   <img src="https://img.shields.io/badge/scraper-violet" alt="kaggle">
   <img src="https://img.shields.io/badge/beautifulsoup-red" alt="bs4"> 
</p>

[Yandex Chart Website Link](https://music.yandex.ru/chart)
## About
My project is based on analyzing the top 100 tracks from the popular music site Yandex.Music. My dataset contains the following columns: track name (name), track duration (track_len), track link (link), genre (genre), artist(s), chart position (chart), explicit content (Explicit_content), total number of monthly listens (monthly_listens_total) and total number of artist likes (artists_likes_total).

This project is an exploration of music data to gain valuable insights and analyze the popularity of music tracks on Yandex.Music. As part of this work, I have conducted the following steps:

Data Collection: First, I developed a script for automated data collection from the Yandex.Music website, which allowed me to obtain information about the top 100 tracks, including their titles, duration, genre, artists, and other characteristics.
Data analysis: The obtained data was subjected to analysis using various methods and tools. This stage included creating graphs, visualizing the data, and identifying the main trends in music preferences of Yandex.Music users.
Insights and conclusions: Based on the data analysis, I drew(ed) a number of key conclusions about the popularity of music tracks on the site. These findings can be useful for understanding current music trends and promotional strategies in the music market.
Next steps: My project can serve as a starting point for more in-depth research on users' music preferences, as well as for the development of recommendation systems and marketing strategies in the music industry.

Overall, this project demonstrates my data analysis skills and work with web scraping, as well as my ability to extract valuable insights from the collected data about music tracks on Yandex.Music.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Мой проект основан на анализе топ-100 треков с популярного музыкального сайта Яндекс.Музыка. В моем датасете содержатся следующие колонки: название трека (name), длительность трека (track_len), ссылка на трек (link), жанр (genre), исполнитель(и) (artist(s)), позиция в чарте (chart), наличие эксплицитного контента (Explicit_content), общее количество ежемесячных прослушиваний (monthly_listens_total) и общее количество лайков исполнителей (artists_likes_total).

Этот проект представляет собой исследование музыкальных данных с целью получения ценных инсайтов и анализа популярности музыкальных треков на Яндекс.Музыке. В рамках этой работы я провел(а) следующие шаги:

Сбор данных: Для начала, я разработал(а) скрипт для автоматизированного сбора данных с сайта Яндекс.Музыка, что позволило мне получить информацию о топ-100 треках, включая их названия, длительность, жанр, исполнителей и другие характеристики.
Анализ данных: Полученные данные были подвергнуты анализу с использованием различных методов и инструментов. Этот этап включал в себя создание графиков, визуализацию данных и выявление основных тенденций в музыкальных предпочтениях пользователей Яндекс.Музыки.
Инсайты и выводы: На основе анализа данных я сделал(а) ряд ключевых выводов о популярности музыкальных треков на сайте. Эти выводы могут быть полезными для понимания текущих музыкальных трендов и стратегий продвижения на музыкальном рынке.
Дальнейшие шаги: Мой проект может служить отправной точкой для более глубокого исследования музыкальных предпочтений пользователей, а также для разработки рекомендательных систем и маркетинговых стратегий в музыкальной индустрии.

В целом, данный проект демонстрирует мои навыки анализа данных и работу с веб-скрапингом, а также способность извлекать ценные знания из собранных данных о музыкальных треках на Яндекс.Музыке.

## Main functions
Collecting data about top 100 tracks from Yandex.Music site: The script performs queries to Yandex.Music site using specified parameters such as genre and chart. It extracts information about the most popular 100 tracks, including track title, duration, link, genre, artist(s), chart, presence of explicit content, monthly number of listens and total number of artist likes.

Track data processing: 
For each track extracted, the script collects the following information:

- Track title.
- Track duration.
- Link to the track.
- Genre of the track.
- The artist(s) of the track.
- The chart the track is in.
- Presence of explicit content.
- Monthly number of listens.
- Total number of likes by artist(s).

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Сбор данных о топ 100 треках с сайта Яндекс.Музыка: Скрипт выполняет запросы к сайту Яндекс.Музыка, используя заданные параметры, такие как жанр и чарт. Он извлекает информацию о самых популярных 100 треках, включая название трека, продолжительность, ссылку, жанр, исполнителя(ей), чарт, наличие эксплицитного контента, ежемесячное количество прослушиваний и общее количество лайков исполнителей.

Обработка данных о треках: 
Для каждого извлеченного трека скрипт собирает следующую информацию:

- Название трека.
- Продолжительность трека.
- Ссылку на трек.
- Жанр трека.
- Исполнителя(ей) трека.
- Чарт, в котором трек находится.
- Наличие эксплицитного контента.
- Ежемесячное количество прослушиваний.
- Общее количество лайков у исполнителей.


## Tech stack
- Python: A programming language for writing a script.
- Requests: A library for sending HTTP requests.
- BeautifulSoup: Library for parsing HTML code of web pages.
- re: A module for working with regular expressions.
- csv: A module for working with CSV files.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Python: Язык программирования для написания скрипта.
- requests: Библиотека для отправки HTTP-запросов.
- BeautifulSoup: Библиотека для парсинга HTML-кода веб-страниц.
- re: Модуль для работы с регулярными выражениями.
- csv: Модуль для работы с CSV файлами.

## Project usability  
Automation: The project allows you to automate the process of collecting data on vacancies, which saves time and reduces routine work.
Access to up-to-date information: The script allows you to quickly get up-to-date information about popular songs on Yandex Music.
Adaptability: You can customize search parameters (query text, region) and easily adapt the script to your needs.
Research analysis of the data has led to some interesting results, which can be found in the notebook here in the github or on the kaggle website. the link is at the bottom.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Автоматизация: Проект позволяет автоматизировать процесс сбора данных о вакансиях, что экономит время и уменьшает рутинную работу.
Доступ к актуальной информации: Скрипт позволяет быстро получить актуальную информацию о популярных треках на Яндекс Музыке.
Адаптируемость: Вы можете настроить параметры поиска (текст запроса, регион) и легко адаптировать скрипт под свои потребности.
Анализ полученных данных привел к интересным результатам, с которыми можно ознакомиться в notebook здесь, на github, или на сайте kaggle. ссылка внизу.

## Developers

- [Anton Belyaev]([GitHub Profile Link](https://github.com/Ch3ekiBr3eki))
- [Anton Belyaev]([Kaggle Profile Link](https://www.kaggle.com/antonbelyaevd))
- ([Kaggle Dataset Link](https://www.kaggle.com/datasets/antonbelyaevd/yandex-music-top-100-songs))
- ([Kaggle Notebook Link](https://www.kaggle.com/code/antonbelyaevd/an-introduction-to-yandex-music-top))
