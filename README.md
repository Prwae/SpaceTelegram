# Космический Телеграм

Программа, которая раз в сутки высылает рандомную астрономическую картинку.

### Как установить

Для начала надо создать .env файл в директории программы.
Затем, взять API ключи и поместить их в него таким способом (ссылка - место откуда надо брать токен):
```
NASA_TOKEN=Токен Nasa
TELEGRAM_TOKEN=Токен Телеграмм бота
TELEGRAM_CHANNEL=Телеграмм канал
```
Где достать:

1. Токен Nasa - https://api.nasa.gov (раздел "Get Api Key")
2. Токен Телеграмм бота - https://telegram.me/BotFather (Создать Телеграм бота, гайд - https://way23.ru/регистрация-бота-в-telegram.html)
3. Телеграмм канал - https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/ (Привязать бота; пункты "Создаем свой Телеграм-канал", "Добавляем бота в канал (или в чат)")

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Запуск скрипта через консоль:
```
python main.py
```

Все ;)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
