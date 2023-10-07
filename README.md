# scrapy_parser_pep

# Проект парсинга pep
### Описание
Перед Вами проект парсера документации PEP, реализованный на фреймворке Scrapy. Учебный проект Яндекс.Практикум.
Проект ставит перед собой цели автоматического получения данных документации.
Использовано:
* Python v.3.7.5 (https://docs.python.org/3.7/)
* Scrapy v2.5.1 (https://docs.scrapy.org/en/latest/index.html)
* SQL Alchemy v2.0.21 (https://docs.sqlalchemy.org/en/20/index.html)
* Flake 8 v.5.0.4 (https://buildmedia.readthedocs.org/media/pdf/flake8/stable/flake8.pdf)

### Установка:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/minigraph/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep

```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Обновите PIP, дабы избежать ошибок установки зависимостей:

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Документация парсера:
##### Запуск "паука" для сбора информации по PEP
Команда:
```bash
scrapy crawl pep
```
Пример вывода:
```bash
 ...
 'scheduler/enqueued/memory': 626,
 'start_time': datetime.datetime(2023, 10, 7, 15, 44, 31, 356386)}
2023-10-07 18:45:38 [scrapy.core.engine] INFO: Spider closed (finished)  
```

### Автор:
* Михаил Никитин
* * tlg: @minigraf 
* * e-mail: minigraph@yandex.ru; maikl.nikitin@yahoo.com;