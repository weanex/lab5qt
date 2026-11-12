import os
import sys


def human_size(size_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    value = float(size_bytes)
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value /= 1024
        idx += 1
    return f"{round(value)}{units[idx]}"


def dir_total_size(path: str) -> int:
    total = 0
    try:
        for entry in os.scandir(path):
            try:
                if entry.is_file(follow_symlinks=False):
                    total += entry.stat(follow_symlinks=False).st_size
                elif entry.is_dir(follow_symlinks=False):
                    total += dir_total_size(entry.path)
            except (OSError, PermissionError):
                continue
    except (OSError, PermissionError):
        pass
    return total


def main() -> None:
    root = sys.argv[1] if len(sys.argv) > 1 else "."

    results = []  # (size, path)
    # обходим все подкаталоги, включая сам root
    for dirpath, dirnames, filenames in os.walk(root):
        try:
            total = 0
            for f in filenames:
                try:
                    total += os.path.getsize(os.path.join(dirpath, f))
                except OSError:
                    pass
            for d in dirnames:
                try:
                    total += dir_total_size(os.path.join(dirpath, d))
                except OSError:
                    pass
            results.append((total, dirpath))
        except OSError:
            continue

    results.sort(key=lambda x: x[0], reverse=True)
    for size, path in results[:10]:
        name = os.path.basename(path.rstrip(os.sep)) or path
        print(f"{name} - {human_size(size)}")


if __name__ == "__main__":
    main()