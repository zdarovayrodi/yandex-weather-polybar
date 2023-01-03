# Yandex Weather module for Polybar

Этот проект является основой для Ваших конфигов.

## Setting up
1. Заходим на [личный кабинет разработчика](https://developer.tech.yandex.ru/services/), выбираем "Яндекс Погода" и получаем API ключ.
1. Получаем данные о широте и долготе.

Теперь в `main.py` вставим полученные ранее данные:
```python3
TOKEN = 'token'
LAT = '11.111111'  # latitude
LON = '22.222222' # longitude
LANG = 'ru_RU'    # answer language
```

## Usage
В конфиге `polybar` (чаще всего он находится в `~/config/polybar/config.ini`) добавляем следующее:
```ini

modules_right = ... weather ...

[module/weather]
type = custom/script
interval = 30
format = <label>
format-foreground = ${colors.foreground}
format-background = ${colors.background}
exec = python3 -u <PATH_TO_PYTHON_FILE>
tail = true
```

> Значение `interval = 30` нужно в связи с ограничением Яндекса 50 запросов/день, не протестировано.

## Styling
Для настройки под Ваши нужды существует документация, с примером `response`.

В моей версии скрипта отображается сначала реальная текущая температура, температура по ощущениям и статус погоды (_rain, snow, overcast, ..._).