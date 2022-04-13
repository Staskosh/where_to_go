# Куда пойти — Москва глазами туриста

Сайт о самых интересных местах в Москве.

[Демка сайта](https://stkosh.pythonanywhere.com/).

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите разработческий сервер

```
python3 manage.py runserver
```

Создайте суперпользователя
```
python3 manage.py createsuperuser 
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Наполнение сайта
Для заполнения сайта данными перейдите в [админ панель](127.0.0.1:8000/admin), введите имя и пароль суперпользователя.
Вы увидите ![стартовую страницу](/where_to_go/static/img/.gitbook/assets/django-admin.png)
В правом верхнем углу ADD PLACE -> Заполните необходимые поля -> нажмите кнопку SAVE в правом нижнем углу.
Вы также можете воспользоваться командой
```
python3 manage.py load_place http://адрес/файла.json
```
и загружать данные о местах на сайт через терминал.
Примеры файлов можно найти по [ссылке](https://github.com/devmanorg/where-to-go-places)

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](/where_to_go/static/img/.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

