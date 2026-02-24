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


