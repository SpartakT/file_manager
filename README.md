File System Manager

CLI утилита для управления файлами.

Команды
- `fm copy source dest` - Копировать файл.
  Пример: `fm copy test.txt`
- `fm delete path` - Удалить файл/папку.
  Пример: `fm delete folder_name`
- `fm count path` - Посчитать файлы в папке (вкл. вложенные).
  Пример: `fm count .`
- `fm search path pattern` - Поиск по regex.
  Пример: `fm search . "\.txt$"`
- `fm add_date path --recursive` - Добавить дату создания в имя.
  Пример: `fm add_date folder --recursive`
- `fm analyse path` - Анализ размеров.
  Пример: `fm analyse .`

Help: `fm --help`






Для проверки
- `python cli.py copy source dest` - Копировать файл.
  Пример: `fm copy test.txt`
- `python cli.py delete path` - Удалить файл/папку.
  Пример: `python cli.py delete folder_name`
- `python cli.py count path` - Посчитать файлы в папке (вкл. вложенные).
  Пример: `python cli.py count .`
- `python cli.py search path pattern` - Поиск по regex.
  Пример: `python cli.py search . "\.txt$"`
- `python cli.py add_date path --recursive` - Добавить дату создания в имя.
  Пример: `python cli.py add_date folder --recursive`
- `python cli.py analyse path` - Анализ размеров.
  Пример: `python cli.py analyse .`

Help: `python cli.py --help`




