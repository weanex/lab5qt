import os
import shutil
from datetime import datetime


def make_reserve_arc(source: str, dest: str) -> str:
    """
    Архивирует каталог source в каталог dest.
    Имя архива содержит дату и время до секунды.
    Возвращает путь созданного архива.
    """
    os.makedirs(dest, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_name = os.path.basename(os.path.normpath(source)) or "archive"
    archive_name = f"{base_name}_{timestamp}"
    archive_path = os.path.join(dest, archive_name)
    # make_archive сам добавит расширение .zip
    created = shutil.make_archive(archive_path, "zip", root_dir=source)
    return created

if __name__ == "__main__":
    print(make_reserve_arc("some_folder", "backups"))