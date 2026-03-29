# File System Manager

CLI утилита и графический интерфейс для управления файлами.

## Требования

- Python >= 3.6

## Установка
```bash
pip install .
```

---

## Запуск GUI
```bash
fm-gui
# или
python filemanager/gui.py
```

В интерфейсе доступны все операции: копирование, удаление, подсчёт, поиск, добавление даты и анализ размеров.  
Пути к файлам и папкам можно вводить вручную или выбрать через встроенный проводник.

---

## Запуск CLI
```bash
fm --help
```

### Команды

| Команда | Описание |
|---|---|
| `fm copy <source> [dest]` | Копировать файл. Если `dest` не указан — создаётся `<source>_copy` |
| `fm delete <path>` | Удалить файл или папку |
| `fm count [path]` | Посчитать файлы в папке, включая вложенные (по умолчанию `.`) |
| `fm search [path] <pattern>` | Поиск файлов по regex (по умолчанию `.`) |
| `fm add_date <path> [--recursive]` | Добавить дату создания к имени файла/папки |
| `fm analyse [path]` | Анализ размеров файлов и папок (по умолчанию `.`) |

### Примеры
```bash
fm copy report.txt backup/report.txt
fm copy report.txt                    
fm delete old_folder
fm count ./src
fm search . "\.py$"
fm add_date ./docs --recursive
fm analyse .
```

---

## Структура проекта
```
filemanager/
├── cli.py          # CLI-интерфейс
├── gui.py          # GUI на Flet
└── fs_manager.py   # Основная логика
config.py           # Цветовая схема GUI
```