File System Manager

CLI утилита для управления файлами.

Команды
- `python cli.py copy source dest` - Копировать файл.
  Пример: `python cli.py copy test.txt`
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

