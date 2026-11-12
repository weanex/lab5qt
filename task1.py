import os
import sys


def human_size(size_bytes: int) -> str:
    """Перевод байт в человекочитаемый вид (округление через round, переход через 1023)."""
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ"]
    value = float(size_bytes)
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value = value / 1024
        idx += 1
    return f"{round(value)}{units[idx]}"


def main() -> None:
    current_dir = os.getcwd()
    lines = []
    # сортируем для стабильного вывода
    for name in sorted(os.listdir(current_dir)):
        path = os.path.join(current_dir, name)
        if os.path.isfile(path):
            lines.append(f"{name} {human_size(os.path.getsize(path))}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()