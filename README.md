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
- `python filemanager/cli.py copy source dest` - Копировать файл.
  Пример: `python filemanager/cli.py copy test.txt`
- `python filemanager/cli.py delete path` - Удалить файл/папку.
  Пример: `python filemanager/cli.py delete folder_name`
- `python filemanager/cli.py count path` - Посчитать файлы в папке (вкл. вложенные).
  Пример: `python filemanager/cli.py count .`
- `python filemanager/cli.py search path pattern` - Поиск по regex.
  Пример: `python filemanager/cli.py search . "\.txt$"`
- `python filemanager/cli.py add_date path --recursive` - Добавить дату создания в имя.
  Пример: `python filemanager/cli.py add_date folder --recursive`
- `python filemanager/cli.py analyse path` - Анализ размеров.
  Пример: `python filemanager/cli.py analyse .`

Help: `python filemanager/cli.py --help`






