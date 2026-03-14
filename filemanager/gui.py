import io
import sys
import flet as ft
from fs_manager import (
    add_creation_date,
    analyze_sizes,
    copy_file,
    count_files,
    delete_path,
    search_files,
)

BG = "#0f1117"
SURFACE = "#1a1d27"
CARD = "#21253a"
ACCENT = "#5b7cf6"
ACCENT2 = "#7c5bf6"
SUCCESS = "#3ecf8e"
DANGER = "#f65b5b"
TEXT = "#e8eaf0"
MUTED = "#6b7280"
BORDER = "#2e3347"


def capture_stdout(func, *args, **kwargs):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    error = None
    result = None
    try:
        result = func(*args, **kwargs)
    except Exception as exc:
        error = str(exc)
    finally:
        sys.stdout = old
    return result, buf.getvalue(), error


class ToolCard(ft.Container):
    def __init__(self, title: str, icon: str, color: str, content: ft.Control):
        super().__init__()
        self.padding = 20
        self.border_radius = 14
        self.bgcolor = CARD
        self.border = ft.Border.all(1, BORDER)
        self.content = ft.Column(
            spacing=14,
            controls=[
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Container(
                            content=ft.Icon(icon, color=color, size=18),
                            bgcolor=f"{color}22",
                            padding=8,
                            border_radius=8,
                        ),
                        ft.Text(
                            title,
                            size=15,
                            weight=ft.FontWeight.W_600,
                            color=TEXT,
                        ),
                    ],
                ),
                content,
            ],
        )


class OutputBox(ft.Container):
    def __init__(self):
        self._placeholder = ft.Text(
            "Здесь появится результат выполнения операции...",
            size=12,
            color=MUTED,
            italic=True,
        )
        self._text = ft.Text("", size=13, color=TEXT, selectable=True)
        super().__init__(
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[self._placeholder, self._text],
                height=120,
            ),
            bgcolor=SURFACE,
            border_radius=12,
            padding=ft.Padding(left=16, right=16, top=12, bottom=12),
            border=ft.Border.all(1, BORDER),
            expand=True,
        )

    def show(self, message: str, is_error: bool = False) -> None:
        self._placeholder.visible = False
        self._text.value = message
        self._text.color = DANGER if is_error else SUCCESS
        self.border = ft.Border.all(1, DANGER if is_error else SUCCESS)
        self.update()


def path_field(hint: str, tooltip: str) -> ft.TextField:
    return ft.TextField(
        hint_text=hint,
        expand=True,
        bgcolor=SURFACE,
        border_color=BORDER,
        focused_border_color=ACCENT,
        color=TEXT,
        hint_style=ft.TextStyle(color=MUTED),
        border_radius=8,
        tooltip=tooltip,
    )


def labeled(label: str, control: ft.Control) -> ft.Column:
    return ft.Column(
        spacing=6,
        controls=[ft.Text(label, size=12, color=MUTED), control],
    )


def prow(field: ft.TextField, btn: ft.Control) -> ft.Row:
    return ft.Row(controls=[field, btn], spacing=6)


def action_btn(
        label: str,
        icon: str,
        color: str,
        handler,
        tooltip: str,
        text_color: str = "#ffffff",
) -> ft.Button:
    return ft.Button(
        content=ft.Row(
            spacing=8,
            tight=True,
            controls=[
                ft.Icon(icon, color=text_color, size=16),
                ft.Text(label, color=text_color, size=14),
            ],
        ),
        style=ft.ButtonStyle(
            bgcolor=color,
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.Padding(left=16, right=16, top=10, bottom=10),
        ),
        on_click=handler,
        tooltip=tooltip,
    )


def file_pick_btn(field: ft.TextField) -> ft.IconButton:
    async def on_click(_):
        picker = ft.FilePicker()
        files = await picker.pick_files()
        if files:
            field.value = files[0].path
            field.update()

    return ft.IconButton(
        icon=ft.Icons.UPLOAD_FILE,
        icon_color=ACCENT,
        tooltip="Выбрать файл через проводник",
        on_click=on_click,
    )


def dir_pick_btn(field: ft.TextField) -> ft.IconButton:
    async def on_click(_):
        picker = ft.FilePicker()
        path = await picker.get_directory_path()
        if path:
            field.value = path
            field.update()

    return ft.IconButton(
        icon=ft.Icons.FOLDER_OPEN,
        icon_color=ACCENT,
        tooltip="Выбрать папку через проводник",
        on_click=on_click,
    )


def file_or_dir_btns(field: ft.TextField) -> ft.Row:
    async def pick_file(_):
        picker = ft.FilePicker()
        files = await picker.pick_files()
        if files:
            field.value = files[0].path
            field.update()

    async def pick_dir(_):
        picker = ft.FilePicker()
        path = await picker.get_directory_path()
        if path:
            field.value = path
            field.update()

    return ft.Row(
        spacing=4,
        controls=[
            ft.IconButton(
                icon=ft.Icons.UPLOAD_FILE,
                icon_color=ACCENT,
                tooltip="Выбрать файл",
                on_click=pick_file,
            ),
            ft.IconButton(
                icon=ft.Icons.FOLDER_OPEN,
                icon_color=ACCENT,
                tooltip="Выбрать папку",
                on_click=pick_dir,
            ),
        ],
    )


def main(page: ft.Page) -> None:
    page.title = "File Manager"
    page.bgcolor = BG
    page.padding = 0
    page.scroll = ft.ScrollMode.ADAPTIVE

    output = OutputBox()

    def ok(msg: str) -> None:
        output.show(msg, is_error=False)

    def err(msg: str) -> None:
        output.show(f"Ошибка: {msg}", is_error=True)

    confirm = ft.AlertDialog(
        modal=True,
        title=ft.Text("Подтверждение удаления", color=TEXT),
        content=ft.Text("Вы уверены? Это действие необратимо.", color=MUTED),
        bgcolor=CARD,
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(confirm)

    src_f = path_field(
        "C:\\path\\to\\file.txt",
        "Файл-источник для копирования",
    )
    dst_f = path_field(
        "C:\\path\\to\\dest.txt (необязательно)",
        "Путь назначения; если пусто — добавится суффикс _copy",
    )

    def do_copy(_) -> None:
        src = src_f.value.strip()
        if not src:
            err("Укажите источник")
            return
        dst = dst_f.value.strip() or src + "_copy"
        _, _, e = capture_stdout(copy_file, src, dst)
        if e:
            err(e)
        else:
            ok(f"Скопировано:\n  {src}\n→ {dst}")

    copy_card = ToolCard(
        "Копировать файл",
        ft.Icons.COPY,
        ACCENT,
        ft.Column(
            spacing=12,
            controls=[
                labeled("Источник", prow(src_f, file_pick_btn(src_f))),
                labeled(
                    "Назначение (необязательно)",
                    prow(dst_f, file_pick_btn(dst_f)),
                ),
                action_btn(
                    "Копировать",
                    ft.Icons.COPY,
                    ACCENT,
                    do_copy,
                    "Скопировать файл в указанное место",
                ),
            ],
        ),
    )

    del_f = path_field(
        "C:\\path\\to\\target",
        "Файл или папка для удаления",
    )

    def confirmed(_) -> None:
        path = del_f.value.strip()
        confirm.open = False
        page.update()
        _, _, e = capture_stdout(delete_path, path)
        if e:
            err(e)
        else:
            ok(f"Удалено: {path}")

    def cancel(_) -> None:
        confirm.open = False
        page.update()

    confirm.actions = [
        ft.TextButton(
            "Отмена",
            on_click=cancel,
            style=ft.ButtonStyle(color=MUTED),
        ),
        action_btn(
            "Удалить",
            ft.Icons.DELETE_FOREVER,
            DANGER,
            confirmed,
            "Подтвердить удаление",
        ),
    ]

    def do_delete(_) -> None:
        if not del_f.value.strip():
            err("Укажите путь")
            return
        confirm.open = True
        page.update()

    delete_card = ToolCard(
        "Удалить файл / папку",
        ft.Icons.DELETE_OUTLINE,
        DANGER,
        ft.Column(
            spacing=12,
            controls=[
                labeled(
                    "Путь к файлу или папке",
                    ft.Row(
                        controls=[del_f, file_or_dir_btns(del_f)],
                        spacing=6,
                    ),
                ),
                action_btn(
                    "Удалить",
                    ft.Icons.DELETE_FOREVER,
                    DANGER,
                    do_delete,
                    "Безвозвратно удалить файл или папку",
                ),
            ],
        ),
    )

    header = ft.Container(
        content=ft.Row(
            spacing=14,
            controls=[
                ft.Container(
                    content=ft.Icon(
                        ft.Icons.FOLDER_SPECIAL, color=ACCENT, size=28
                    ),
                    bgcolor=f"{ACCENT}22",
                    padding=10,
                    border_radius=12,
                ),
                ft.Column(
                    spacing=2,
                    controls=[
                        ft.Text(
                            "File Manager",
                            size=22,
                            weight=ft.FontWeight.W_700,
                            color=TEXT,
                        ),
                        ft.Text(
                            "Управление файловой системой",
                            size=13,
                            color=MUTED,
                        ),
                    ],
                ),
            ],
        ),
        padding=ft.Padding(left=28, right=28, top=22, bottom=22),
        border=ft.Border(bottom=ft.BorderSide(1, BORDER)),
    )

    result_panel = ft.Container(
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Row(
                    spacing=8,
                    controls=[
                        ft.Icon(ft.Icons.TERMINAL, color=ACCENT, size=16),
                        ft.Text(
                            "Результат",
                            size=13,
                            color=TEXT,
                            weight=ft.FontWeight.W_600,
                        ),
                    ],
                ),
                output,
            ],
        ),
        bgcolor=CARD,
        border_radius=14,
        padding=16,
        border=ft.Border.all(1, BORDER),
    )

    grid = ft.ResponsiveRow(
        columns=12,
        spacing=16,
        run_spacing=16,
        controls=[],
    )

    body = ft.Container(
        content=ft.Column(
            spacing=20,
            controls=[result_panel, grid],
        ),
        padding=ft.Padding(left=28, right=28, top=20, bottom=20),
    )

    page.add(ft.Column(spacing=0, controls=[header, body], expand=True))


ft.run(main)
