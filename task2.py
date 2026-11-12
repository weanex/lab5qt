import sys
import zipfile


def human_size(size_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    value = float(size_bytes)
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value /= 1024
        idx += 1
    return f"{round(value)}{units[idx]}"


def print_zip_tree(zip_path: str) -> None:
    with zipfile.ZipFile(zip_path) as zf:
        infos = zf.infolist()
        if not infos:
            return

        # строим дерево: множество всех путей-каталогов и файлов
        entries = {}  # path -> is_dir
        for info in infos:
            name = info.filename.rstrip("/")
            if not name:
                continue
            parts = name.split("/")
            # регистрируем все промежуточные каталоги
            for i in range(1, len(parts)):
                dir_path = "/".join(parts[:i])
                entries[dir_path] = True
            if info.is_dir():
                entries[name] = True
            else:
                entries[name] = False

        # размеры файлов
        sizes = {}
        for info in infos:
            if not info.is_dir():
                sizes[info.filename.rstrip("/")] = info.file_size

        # группируем по родителю
        from collections import defaultdict
        children = defaultdict(list)
        for path, is_dir in entries.items():
            parent, _, leaf = path.rpartition("/")
            children[parent].append((leaf, is_dir, path))

        def walk(parent: str, depth: int) -> None:
            items = sorted(children.get(parent, []), key=lambda x: (not x[1], x[0]))
            for leaf, is_dir, full in items:
                indent = "  " * depth
                if is_dir:
                    print(f"{indent}{leaf}")
                    walk(full, depth + 1)
                else:
                    print(f"{indent}{leaf} {human_size(sizes.get(full, 0))}")

        walk("", 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    print_zip_tree(sys.argv[1])