# Космический Телеграм

Программа, которая раз в сутки высылает рандомную астрономическую картинку.

### Как установить

Для начала надо создать .env файл в директории программы.
Затем, взять API ключи и поместить их в него таким способом (ссылка - место откуда надо брать токен):
```
NASA_TOKEN=Токен Nasa (https://api.nasa.gov (раздел "Get Api Key"))
TELEGRAM_TOKEN=Токен телеграмм бота (https://telegram.me/BotFather (Создать Телеграм бота, гайд - https://way23.ru/регистрация-бота-в-telegram.html))
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
